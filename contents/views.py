from django.shortcuts import render, redirect, get_object_or_404
from contents.models import Content, HashTag
from django.core.paginator import Paginator
from users.models import FavoriteContent
from django.contrib.auth.decorators import login_required


def content_list(request):
    contents = Content.objects.all().order_by("-search_count")  # 검색횟수 내림차순
    tags = HashTag.objects.all()
    search_query = request.GET.get("q")

    if search_query:
        contents = contents.filter(title__icontains=search_query)
    # 페이징

    paginator = Paginator(contents, 2)
    page_number = request.GET.get("page")
    page_contents = paginator.get_page(page_number)

    context = {
        "page_contents": page_contents,
        "search_query": search_query,
        "tags": tags,
    }
    if not request.user.is_authenticated:
        return render(request, "contents/content_list.html", context)
    return render(request, "contents/logined_content_list.html", context)


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

    paginator = Paginator(contents_with_tag, 2)
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

    # if request.user.is_authenticated:
    if FavoriteContent.objects.filter(user=user, content=content).exists():
        FavoriteContent.objects.filter(user=user, content=content).delete()
    else:
        FavoriteContent.objects.create(user=user, content=content)
    return redirect("content", id=content_id)
    # else:
    #     return redirect("/users/login/")
