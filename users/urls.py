from django.urls import path
from users.views import login_view, logout_view, signup, my_page, remove_favorite

urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("signup/", signup, name="signup"),
    path("mypage/", my_page, name="my_page"),
    path(
        "remove_favorite/<int:favorite_content_id>/",
        remove_favorite,
        name="remove_favorite",
    ),
]
