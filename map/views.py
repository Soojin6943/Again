from django.shortcuts import render
from contents.models import Content
from django.conf import settings
import csv


# Create your views here.
def map(request):
    mapList = Content.objects.all()
    organizations = mapList.values_list("organization_name", flat=True).distinct()
    context = {
        "mapList": mapList,
        "organizations": organizations,
        "kakao_map_api_key": settings.KAKAO_MAP_API_KEY,
    }
    return render(request, "map.html", context)


def detail(request, category):
    mapList = Content.objects.filter(svcProvNm=category)
    context = {
        "category": category,
        "centerLat": mapList[0].latitude,
        "centerLon": mapList[0].longitude,
        "mapList": mapList,
    }
    return render(request, "map.html", context)


def bulk_import(request):
    CSV_PATH = "static/test3.csv"

    with open(CSV_PATH, newline="", encoding="utf-8") as csvfile:
        data_reader = csv.DictReader(csvfile)
        for row in data_reader:
            Content.objects.create(
                title=row["강좌명/과정명"],
                content=row["강좌내용"],
                organization_name=row["운영기관명"],
                location=row["위치/장소"],
                type_of_people=row["교육대상자"],
                number_of_people=row["강좌정원수"],
                week=row["차수"],
                money=row["수강료"],
                start_date=row["교육시작일"],
                end_date=row["교육종료일"],
                enroll_start_date=row["접수시작일"],
                enroll_end_date=row["접수마감일"],
                eduW=row["교육방법"],
                how=row["접수방법"],
                phone_number=row["운영기관연락처"],
                etc=row["선정방법구분"],
                content_link=row["홈페이지 주소"],
                # tags=row['태그']
            )
        return
