import streamlit as st

st.write("## Conversor de medidas")

medidas_velocidade_atual = st.selectbox("Selecione o tipo de medida de velocidade atual", ["km/h","m/s"])

medidas_velocidade_futura = st.selectbox("Selecione o tipo de medida de velocidade futura",["km/h","m/s"])

input_velocidade = st.number_input("Digite o valor da velocidade")

def converte_velocidade(velocidade_atual):
    return velocidade_atual *2

st.write(f"{converte_velocidade(input_velocidade)}")