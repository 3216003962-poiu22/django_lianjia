from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader
from pyecharts import Bar, Pie, Page
import pandas as pd
from pyecharts import configure


REMOTE_HOST = "https://pyecharts.github.io/assets/js"


def index(request,city):
    template = loader.get_template('echarts/pyecharts.html')
    plot = make_plot(city)
    context = dict(
        myechart=plot.render_embed(),
        host=REMOTE_HOST,
        script_list=plot.get_js_dependencies()
    )

    return HttpResponse(template.render(context, request))


def make_plot(city):

    # 倒入包
    data = pd.read_csv('csv_files/%s/groupby_region_df.csv'%city)
    # 读取数据

    configure(global_theme='vintage')
    # 设置主题

    X_axis = data["地区"].tolist()
    v1 = data["每平方米单价(单位:元)"].tolist()
    v2 = data["总价(单位:万元)"].tolist()
    bar1 = Bar(title="%s各区域二手房单价分布条形图"%city, width=1500, height=600)
    bar1.add("单价",
             X_axis,
             v1,
             mark_point=["max", "min"],
             mark_line=['average'],
             mark_point_textcolor='#000',
             xaxis_rotate=45,
             mark_point_symbol="pin", )
    bar2 = Bar(title="%s各区域二手房总价分布条形图"%city, width=1500, height=600)
    bar2 = bar2.add("总价",
                    X_axis,
                    v2,
                    mark_point=["max", "min"],
                    mark_line=['average'],
                    xaxis_rotate=45,
                    mark_point_textcolor='#000',
                    mark_point_symbol="pin", )
    page = Page()
    page.add_chart(bar1)
    page.add_chart(bar2)
    return page