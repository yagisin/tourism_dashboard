import pandas as pd
import streamlit as st
from st_files_connection import FilesConnection
import altair as alt

from module import preprocessing

# Settings wide mode
st.set_page_config(layout="wide")

# Settings color
line_color = '#1168ad'

area_color_maping = {
    '草津町': '#1f662e',
    '渋川市': '#f4d002',
    '中之条町': '#1168ad' 
}

height = 400

url_pref = 'https://raw.githubusercontent.com/yagisin/tourism_dashboard/main/data/prefecture.csv'
url_city = 'https://raw.githubusercontent.com/yagisin/tourism_dashboard/main/data/city.csv'

df_pref = pd.read_csv(url_pref)
df_city = pd.read_csv(url_city)

df_pref = preprocessing.run_prefecture(df_pref)
df_city = preprocessing.run_city(df_city)


# Row1 Plot 群馬県観光来訪者数
chart = alt.Chart(df_pref).mark_line(size=2, point=True).encode(

    x=alt.X(
        'year_month:T',
        title=None,
        axis=alt.Axis(format='%B')
    ),

    y=alt.Y(
        'population:Q',
        title=None,
        scale=alt.Scale(domain=[0, 3000000])
    ),
    
).transform_filter(
    alt.datum.prefecture == '群馬県'
).properties(title='観光来訪者数: 群馬県', height=height)

st.altair_chart(chart, use_container_width=True)

# Row2 Plot 中之条町観光訪者数
chart = alt.Chart(df_city).mark_line(size=2, point=True).encode(
    x=alt.X(
        'year_month:T',
        title=None,
        axis=alt.Axis(format='%B')
    ),

    y=alt.Y(
        'population:Q',
        title=None,
        scale=alt.Scale(domain=[0, 80000]),
        axis=alt.Axis(values=list(range(0, 80001, 20000)))
    ),

).transform_filter(
    alt.datum.area == '中之条町'
).properties(title='観光来訪者数: 中之条町', height=height)

st.altair_chart(chart, use_container_width=True)

# Row3 Plot 中之条町、渋川市、草津町観光来訪者数
chart = alt.Chart(df_city).mark_line(size=2, point=True).encode(

    x=alt.X(
        'year_month:T',
        title=None,
        axis=alt.Axis(format='%B')
    ),

    y=alt.Y(
        'population:Q',
        title=None,
        scale=alt.Scale(domain=[0, 200000]),
        axis=alt.Axis(values=list(range(0, 200001, 50000)))
    ),

    color=alt.Color(
        'area:N',
        scale=alt.Scale(domain=list(area_color_maping.keys()), range=list(area_color_maping.values())),
        title=None,
        legend=alt.Legend(orient='top-right', columns=3),
    ),

).transform_filter(
    alt.FieldOneOfPredicate(field='area', oneOf=['草津町', '渋川市', '中之条町'])
).properties(title='観光来訪者数: 草津町・渋川市・中之条町', height=height)
st.altair_chart(chart, use_container_width=True)