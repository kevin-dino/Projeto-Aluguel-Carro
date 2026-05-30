import streamlit as st
from datetime import datetime
st.title("locadora de veiculos")
st.sidebar.image()
st.sidebar.image("skiline.jpg")
st.sidebar.image("r34carro.jpg")
st.sidebar.image("maclaren.jpg")
carro=st.sidebar.selectbox("selecione seu veiculo:",["tubarão.jpg","skiline.jpg","skiline.jpg","maclaren.jpg"])
valores_diarias = {skiline.jpg:350.0, "r34carro.jpg":600.0, "maclaren.jpg":800.0}#dicionário

st.title(carro)
st.image(f"{carro}.png", width=500)
valores_diarias = valores_diarias[carro]

data_inicio = st.datetime_input("selecione o dia da retirada", datetime.now())
data_final = st.datetime_input("selecione o dia da devolução",data_inicioio)

if st.buton("calcular"): #se alguem clicar no butão
    dias = (data_final - data_inicio).days
    valor_total = valor da diaria* days
    st.subheader(f"alugando {carro} por {dias}dias, o valor será {valor_total}")
    