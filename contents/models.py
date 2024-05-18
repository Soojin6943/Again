from django.db import models


class Content(models.Model):
    title = models.CharField(max_length=30, null=True, blank=True)
    content = models.CharField(max_length=50, null=True, blank=True)
    organization_name = models.CharField(max_length=30, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    type_of_people = models.CharField(max_length=100, null=True, blank=True)
    number_of_people = models.IntegerField(max_length=500, null=True, blank=True)
    week=models.CharField(max_length=10, null=True, blank=True)
    money=models.CharField(max_length=10, null=True, blank=True)
    start_date = models.CharField(max_length=10, null=True, blank=True)
    end_date = models.CharField(max_length=10, null=True, blank=True)
    enroll_start_date = models.CharField(max_length=10, null=True, blank=True)
    enroll_end_date = models.CharField(max_length=10, null=True, blank=True)
    eduW = models.CharField(max_length=50, null=True, blank=True)
    how = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=30, null=True, blank=True)
    etc = models.CharField(max_length=50, null=True, blank=True)
    content_link = models.URLField(default="")
    tags = models.ManyToManyField(
        "contents.HashTag", verbose_name="해시태그 목록", null=True, blank=True
    )
    search_count = models.IntegerField(default=0)

    # 콘텐츠 이름 표기
    def __str__(self):
        return self.title


class HashTag(models.Model):
    name = models.CharField("태그명", max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name
