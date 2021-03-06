from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader
from pyecharts import Bar, Pie, Page
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
    # 倒入包
    data = pd.read_csv('csv_files/%s/number_count.csv'%city)
    # 读取数据

    configure(global_theme='vintage')
    # 设置主题

    attr = data["地区"].tolist()
    v1 = data["数量"].tolist()
    # 数据处理

    bar = Bar(title="%s各区域二手房数量分布条形图"%city_dict[city], width=1500, height=600)
    bar.add("数量",
            attr,
            v1,
            mark_point=["max", "min"],
            xaxis_label_textsize=12,
            mark_point_textcolor='#000',
            xaxis_rotate=45,
            mark_point_symbol="pin", )
    pie = Pie("%s各区域二手房数量分布饼状图"%city_dict[city], title_pos="left", width=1500, height=800)
    pie.add(
        "",
        attr,
        v1,
        radius=[40, 80],
        label_text_color=None,
        is_label_show=True,
        legend_orient="vertical",
        legend_pos="right",
        is_toolbox_show=False
    )

    page = Page()
    page.add_chart(bar)
    page.add_chart(pie)
    return page