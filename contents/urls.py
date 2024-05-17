from django.urls import path
from contents.views import content_list, content, tags_list, add_favorite

urlpatterns = [
    path("content_list/", content_list, name="content_list"),
    path("content/<int:id>", content, name="content"),
    path("tags_list", tags_list, name="tags_list"),
    path("add_favorite/<int:content_id>", add_favorite, name="add_favorite"),
]
