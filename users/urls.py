from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("signup/", views.signup, name="signup"),
    path("my_page/", views.my_page, name="my_page"),
    path(
        "remove_favorite/<int:favorite_id>/",
        views.remove_favorite,
        name="remove_favorite",
    ),
]
