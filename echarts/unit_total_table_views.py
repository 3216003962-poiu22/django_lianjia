from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader
from pyecharts import Bar, Page
import pandas as pd
from pyecharts import configure
from echarts.city_info import make_city_dict

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
    city_dict = make_city_dict()
    data = pd.read_csv('csv_files/%s/unit_table.csv'%city)

    configure(global_theme='vintage')

    attr = data.area1.tolist()
    table_name = data.columns.tolist()[1:]

    unit_bar = Bar("%s单价堆叠图(单位：元)"%city_dict[city], width=1200, height=500,title_top=20)

    for i in range(len(table_name)):
        name = table_name[i]
        values = data[table_name[i]].tolist()
        unit_bar.add(name, attr, values, is_stack=True, xaxis_rotate=45, )

    data = pd.read_csv('csv_files/%s/total_table.csv'%city)

    configure(global_theme='vintage')

    attr = data.area1.tolist()
    table_name = data.columns.tolist()[1:]

    total_bar = Bar("%s总价堆叠图(单位：万元)"%city_dict[city], width=1200, height=500,title_top=20)

    for i in range(len(table_name)):
        name = table_name[i]
        values = data[table_name[i]].tolist()
        total_bar.add(name, attr, values, is_stack=True, xaxis_rotate=45, )

    page = Page()
    page.add_chart(unit_bar)
    page.add_chart(total_bar)
    return page
