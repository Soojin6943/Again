from django.shortcuts import render, redirect


def index(request):
    if request.user.is_authenticated:
        return render(request, "logined_index.html")
    return render(request, "index.html")
