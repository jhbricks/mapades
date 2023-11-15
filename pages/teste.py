import streamlit as st
from streamlit_extras.colored_header import colored_header
import folium
import leafmap
import leafmap.foliumap as leafmap
import geopandas as gpd
from deff.mapa import mapa
from deff.mapa import grafico
from deff.calculos import conta

op = st.radio("Selecione um indicador:",("A","B", "C", "D", "E", "F", "G"))
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

contexto = "./dados/csv/contexto.csv"
pop = "./dados/csv/pop_2021.csv"

if op == "A":
      a,b,c,d,e,f = st.columns()
      with a:
            mapa('PR',contexto,'População','FisherJenks',5,'Wistia', ['Município','População'],'População residente (hab)')
            st.text("Wistia")
      with b:
            mapa('PR',contexto,'População','FisherJenks',5,'YlGnBu', ['Município','População'],'População residente (hab)')
            st.text("YlGnBu")
      with c:
            mapa('PR',contexto,'População','FisherJenks',5,'YlGn', ['Município','População'],'População residente (hab)')
            st.text("YlGn")
      with d:
            mapa('PR',contexto,'População','FisherJenks',5,'YlOrRd', ['Município','População'],'População residente (hab)')
            st.text("YlOrRd")
      with e:
            mapa('PR',contexto,'População','FisherJenks',5,'autumn_r', ['Município','População'],'População residente (hab)')
            st.text("autumn_r")
      with f:
            mapa('PR',contexto,'População','FisherJenks',5,'cividis_r', ['Município','População'],'População residente (hab)')
            st.text("cividis_r")