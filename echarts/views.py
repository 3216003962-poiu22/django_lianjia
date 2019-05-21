# 此页页用于主页编辑
import pandas as pd
from django.shortcuts import render
from echarts.number_count_views import index as number_count_views_index
from echarts.city_info import city_short_name, make_city_dict


def mainpage(request):

    city_dict = make_city_dict()
    return render(request, 'mainpage/mainpage.html', {"city_dict": city_dict})


def index(request, city):
    city_short_name_list = city_short_name()
    if city in city_short_name_list:
        return number_count_views_index(request, city)
