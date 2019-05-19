# 此页页用于主页编辑
import pandas as pd
from django.shortcuts import render
from echarts.number_count_views import index as number_count_views_index
from echarts.city_info import city_short_name

def mainpage(request):
    return render(request, 'mainpage/mainpage.html')



def index(request, city):
    city_short_name_list=city_short_name()
    if city in city_short_name_list:
        return number_count_views_index(request, city)


