import streamlit as st
from streamlit_extras.colored_header import colored_header
from teste.teste import mapa

colored_header(label=":orange[Indicadores de Segurança: em breve ⌛]", description="   ", color_name="orange-70",)

mapa('PR', 'pop', 'População', 'FisherJenks', 5, 'Oranges', ['Municípios','População'], 'AAA')
