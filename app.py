import streamlit as st

st.write("## Conversor de medidas")

medidas_velocidade_atual = st.selectbox("Selecione o tipo de medida de velocidade atual", ["km/h","m/s"])

medidas_velocidade_futura = st.selectbox("Selecione o tipo de medida de velocidade futura",["km/h","m/s"])

input_velocidade = st.number_input("Digite o valor da velocidade")

def converte_velocidade(velocidade_atual, velocidade_futura, input_velocidade):
    match velocidade_atual:
        case "km/h":
            match velocidade_futura:
                case "m/s":
                    return input_velocidade / 3.6
                case velocidade_atual:
                    return  input_velocidade
        case "m/s": 
            match velocidade_futura:
                case "k/h":
                    return input_velocidade * 3.6
                case velocidade_atual:
                    return input_velocidade
        case default:
            return "Selecione o tipo de medida para converter ou a ser convertida"


st.write(f"{converte_velocidade(medidas_velocidade_atual,medidas_velocidade_futura,input_velocidade)}")
