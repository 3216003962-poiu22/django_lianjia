"""lianjia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from echarts.views import mainpage
from echarts import number_count_views,region_price_views,layout_type_views,unit_total_table_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', mainpage),
    url(r'^(.*?)/number_count/',number_count_views.index),
    url(r'^(.*?)/region_price/',region_price_views.index),
    url(r'^(.*?)/layout_type/',layout_type_views.index),
    url(r'^(.*?)/unit_total_table/',unit_total_table_views.index),

]