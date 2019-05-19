import pandas as pd


def make_city_list():
    city_df=pd.read_csv('csv_files/total_city/city_df.csv')
    city_list=city_df["city"].tolist()
    return city_list

def city_short_name():
    city_df = pd.read_csv('csv_files/total_city/city_df.csv')
    city_short_name_list = city_df["short_name"].tolist()
    return city_short_name_list

def make_city_dict():
    city_short_name_list=city_short_name()
    city_list=make_city_list()
    city_dict=dict(zip(city_short_name_list,city_list))
    return city_dict

