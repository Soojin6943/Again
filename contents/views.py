from django.shortcuts import render, redirect, get_object_or_404
from contents.models import Content, HashTag
from django.core.paginator import Paginator
from users.models import FavoriteContent
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.template.loader import render_to_string
from difflib import SequenceMatcher


def similar_contents_by_title(content_title, all_contents):
    similar_contents = []

    for content in all_contents:
        similarity = SequenceMatcher(None, content_title, content.title).ratio()
        if similarity > 0.3:  # 유사도 임계값 설정
            similar_contents.append((content, similarity))

    # 유사도 순으로 정렬 (내림차순)
    similar_contents.sort(key=lambda x: x[1], reverse=True)

    # 유사도 값 제거하고 콘텐츠만 반환
    return [content for content, similarity in similar_contents]


def content_list(request):
    contents = Content.objects.all().order_by("title")
    tags = HashTag.objects.all()
    search_query = request.GET.get("q")

    if search_query:
        contents = contents.filter(title__icontains=search_query)

    similar_contents = []
    if request.user.is_authenticated:
        favorite_contents = FavoriteContent.objects.filter(user=request.user)
        favorite_content_ids = favorite_contents.values_list("content_id", flat=True)

        if favorite_content_ids:
            favorite_content_titles = [
                content.title
                for content in Content.objects.filter(id__in=favorite_content_ids)
            ]

            # 모든 콘텐츠 중에서 유사한 콘텐츠 찾기
            all_contents = Content.objects.exclude(id__in=favorite_content_ids)
            for title in favorite_content_titles:
                similar_contents.extend(similar_contents_by_title(title, all_contents))

            # 중복 제거
            similar_contents = list(set(similar_contents))
            # 검색 횟수 순으로 정렬
            similar_contents.sort(key=lambda x: x.search_count, reverse=True)

    # 추천 콘텐츠 페이징
    similar_paginator = Paginator(similar_contents, 5)  # 페이지당 5개 콘텐츠
    similar_page_number = request.GET.get("similar_page")
    similar_page_contents = similar_paginator.get_page(similar_page_number)

    top_contents = Content.objects.all().order_by("-search_count")[:10]

    # 페이징
    paginator = Paginator(contents, 10)
    page_number = request.GET.get("page")
    page_contents = paginator.get_page(page_number)

    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        data = {
            "page_contents": render_to_string(
                "contents/content_items.html", {"page_contents": page_contents}
            ),
            "similar_page_contents": render_to_string(
                "contents/similar_content_items.html",
                {"similar_page_contents": similar_page_contents},
            ),
        }
        return JsonResponse(data)

    context = {
        "page_contents": page_contents,
        "search_query": search_query,
        "tags": tags,
        "similar_page_contents": similar_page_contents,
        "top_contents": top_contents,
    }

    return render(request, "contents/content_list.html", context)


def content(request, id):
    content = get_object_or_404(Content, id=id)

    content.search_count += 1
    content.save()

    context = {"content": content}
    return render(request, "contents/content.html", context)


def tags_list(request):
    tag_name = request.GET.get("tag")
    tag = get_object_or_404(HashTag, name=tag_name)
    contents_with_tag = tag.content_set.all()

    paginator = Paginator(contents_with_tag, 10)
    page_number = request.GET.get("page")
    page_contents = paginator.get_page(page_number)

    context = {
        "tag": tag,
        "page_contents": page_contents,
    }
    return render(request, "contents/tags_list.html", context)


@login_required
def add_favorite(request, content_id):
    user = request.user
    content = get_object_or_404(Content, pk=content_id)

    if FavoriteContent.objects.filter(user=user, content=content).exists():
        FavoriteContent.objects.filter(user=user, content=content).delete()
    else:
        FavoriteContent.objects.create(user=user, content=content)
    return redirect("content", id=content_id)
