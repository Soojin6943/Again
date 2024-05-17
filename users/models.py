from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from contents.models import HashTag, Content


class User(AbstractUser):
    profile_image = models.ImageField(
        "프로필 이미지", upload_to="users/profile", blank=True
    )
    short_description = models.TextField("소개글", blank=True)


class FavoriteTag(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    tag = models.ForeignKey(HashTag, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s Favorite Tag: {self.tag.name}"


class FavoriteContent(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s Favorite Content: {self.content.title}"
