import streamlit as st
from streamlit_extras.colored_header import colored_header
import folium
import leafmap
import leafmap.foliumap as leafmap
import geopandas as gpd
from deff.mapa__ import mapa
from deff.mapa import grafico
from deff.calculos import conta

op = st.radio("Selecione um indicador:",("A","B", "C", "D", "E", "F", "G"))
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

contexto = "./dados/csv/contexto.csv"
pop = "./dados/csv/pop_2021.csv"

if op == "A":
      a,b,c,d = st.columns(4)
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
elif op == "B":
      a,b,c,d = st.columns(4)
      with a:
            mapa('PR',contexto,'População','FisherJenks',5,'autumn_r', ['Município','População'],'População residente (hab)')
            st.text("autumn_r")
      with b:
            mapa('PR',contexto,'População','FisherJenks',5,'cividis_r', ['Município','População'],'População residente (hab)')
            st.text("cividis_r")
      with c:
            mapa('PR',contexto,'População','FisherJenks',5,'copper_r', ['Município','População'],'População residente (hab)')
            st.text("copper_r")
      with d:
            mapa('PR',contexto,'População','FisherJenks',5,'cubehelix_r', ['Município','População'],'População residente (hab)')
            st.text("cubehelix_r")
elif op == "C":
      a,b,c,d = st.columns(4)
      with a:
            mapa('PR',contexto,'População','FisherJenks',5,'gnuplot_r', ['Município','População'],'População residente (hab)')
            st.text("gnuplot_r")
      with b:
            mapa('PR',contexto,'População','FisherJenks',5,'inferno_r', ['Município','População'],'População residente (hab)')
            st.text("inferno_r")
      with c:
            mapa('PR',contexto,'População','FisherJenks',5,'magma_r', ['Município','População'],'População residente (hab)')
            st.text("magma_r")
      with d:
            mapa('PR',contexto,'População','FisherJenks',5,'plasma_r', ['Município','População'],'População residente (hab)')
            st.text("plasma_r")
elif op == "D":
      a,b,c = st.columns(3)
      with a:
            mapa('PR',contexto,'População','FisherJenks',5,'summer_r', ['Município','População'],'População residente (hab)')
            st.text("summer_r")
      with b:
            mapa('PR',contexto,'População','FisherJenks',5,'viridis_r', ['Município','População'],'População residente (hab)')
            st.text("viridis_r")
      with c:
            mapa('PR',contexto,'População','FisherJenks',5,'winter_r', ['Município','População'],'População residente (hab)')
            st.text("winter_r")
elif op == "E":
      a,b,c,d = st.columns(4)
      with a:
            mapa('PR',contexto,'População','FisherJenks',5,'BuGn', ['Município','População'],'População residente (hab)')
            st.text("BuGn")
      with b:
            mapa('PR',contexto,'População','FisherJenks',5,'GnPu', ['Município','População'],'População residente (hab)')
            st.text("GnPu")
      with c:
            mapa('PR',contexto,'População','FisherJenks',5,'OrRd', ['Município','População'],'População residente (hab)')
            st.text("OrRd")
      with d:
            mapa('PR',contexto,'População','FisherJenks',5,'PuBu', ['Município','População'],'População residente (hab)')
            st.text("PuBu")
elif op == "F":
      a,b,c,d = st.columns(4)
      with a:
            mapa('PR',contexto,'População','FisherJenks',5,'PuBuGn', ['Município','População'],'População residente (hab)')
            st.text("PuBuGn")
      with b:
            mapa('PR',contexto,'População','FisherJenks',5,'PuRd', ['Município','População'],'População residente (hab)')
            st.text("PuRd")
      with c:
            mapa('PR',contexto,'População','FisherJenks',5,'RdPu', ['Município','População'],'População residente (hab)')
            st.text("RdPu")
      with d:
            mapa('PR',contexto,'População','FisherJenks',5,'YlGn', ['Município','População'],'População residente (hab)')
            st.text("YlGn")
elif op == "G":
      a,b,c,d = st.columns(4)
      with a:
            mapa('PR',contexto,'População','FisherJenks',5,'YlGnBu', ['Município','População'],'População residente (hab)')
            st.text("YlGnBu")
      with b:
            mapa('PR',contexto,'População','FisherJenks',5,'YlOrBr', ['Município','População'],'População residente (hab)')
            st.text("YlOrBr")
      with c:
            mapa('PR',contexto,'População','FisherJenks',5,'YlOrRd', ['Município','População'],'População residente (hab)')
            st.text("YlOrRd")
      with d:
            mapa('PR',contexto,'População','FisherJenks',5,'Oranges', ['Município','População'],'População residente (hab)')
            st.text("Oranges")
