import streamlit as st
from datetime import datetime
st.title("locadora de veiculos")
carro=st.sidebar.selectbox("selecione seu veiculo:",["tubarão.jpg","skiline.jpg","skiline.jpg","maclaren.jpg"])
valores_diarias = {"skiline.jpg":350.0, "r34carro.jpg":600.0, "maclaren.jpg":800.0}#dicionário

st.title(carro)
st.image(f"{carro}", width=500)

data_inicio = st.datetime_input("selecione o dia da retirada", datetime.now())
data_final = st.datetime_input("selecione o dia da devolução",data_inicio)

if st.button("calcular"): #se alguem clicar no butão
    dias = (data_final - data_inicio).days
    valor_total = valores_diarias[carro]* dias
    st.subheader(f"alugando {carro} por {dias}dias, o valor será {valor_total}")
    