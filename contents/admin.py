from django.contrib import admin
from contents.models import Content, HashTag
from django.db.models import ManyToManyField
from django.forms import CheckboxSelectMultiple


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "content",
        "organization_name",
        "location",
        "type_of_people",
        "number_of_people",
        "start_date",
        "end_date",
        "enroll_start_date",
        "enroll_end_date",
        "phone_number",
        "content_link",
    ]
    formfield_overrides = {
        ManyToManyField: {"widget": CheckboxSelectMultiple},
    }


@admin.register(HashTag)
class HashTagAdmin(admin.ModelAdmin):
    pass
