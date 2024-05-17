from django.shortcuts import render, redirect, get_object_or_404
from users.forms import LoginForm, SignupForm
from django.contrib.auth import authenticate, login, logout
from users.models import User, FavoriteTag, FavoriteContent
from django.core.paginator import Paginator


def login_view(request):
    if request.user.is_authenticated:
        return redirect("/contents/content_list/")

    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect("/contents/content_list")
            else:
                form.add_error(None, "입력한 사용자가 존재하지 않습니다.")

        context = {"form": form}
        return render(request, "users/login.html", context)
    else:
        form = LoginForm()
        context = {"form": form}
        return render(request, "users/login.html", context)


def logout_view(request):
    logout(request)
    return redirect("/users/login/")


def signup(request):
    if request.method == "POST":
        form = SignupForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/contents/content_list/")
    else:
        form = SignupForm()

    context = {"form": form}
    return render(request, "users/signup.html", context)


def my_page(request):
    user = request.user
    favorite_contents = FavoriteContent.objects.filter(user=user)

    paginator = Paginator(favorite_contents, 2)
    page_number = request.GET.get("page")
    page_contents = paginator.get_page(page_number)

    context = {
        "user": user,
        "favorite_contents": favorite_contents,
        "page_contents": page_contents,
    }
    if request.user.is_authenticated:
        return render(request, "users/my_page.html", context)
    return render(request, "users/login.html")


def remove_favorite(request, favorite_content_id):
    if request.method == "POST":
        favorite_content = FavoriteContent.objects.get(pk=favorite_content_id)
        favorite_content.delete()
    return redirect("my_page")
