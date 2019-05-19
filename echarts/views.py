# 此页页用于主页编辑

from django.shortcuts import render
from echarts.number_count_views import index as number_count_views_index


def mainpage(request):
    return render(request, 'mainpage/mainpage.html')


def get_city(request, url_city):
    return render(request, 'echarts/pyecharts.html', {'string': str(url_city)})


def index(request, city):
    if city == "dg":
        return number_count_views_index(request, city)
    if city == "gz":
        return number_count_views_index(request, city)
