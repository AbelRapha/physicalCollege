import streamlit as st

st.write("## Conversor de medidas")

medidas_atual = st.selectbox("Selecione o tipo de medida de velocidade atual", ["km/h","m/s"])

medidas_futura = st.selectbox("Selecione o tipo de medida de velocidade futura",["km/h","m/s"])

input_medida = st.number_input("Digite o valor da velocidade")

def converte_medida(medida_atual, medida_futura, input_medida):
    match medida_atual:
        case "km/h":
            match medida_futura:
                case "m/s":
                    return input_medida / 3.6
                case medida_atual:
                    return  input_medida
        case "m/s": 
            match medida_futura:
                case "k/h":
                    return input_medida * 3.6
                case medida_atual:
                    return input_medida
        case default:
            return "Selecione o tipo de medida para converter ou a ser convertida"


st.write(f"{converte_medida(medidas_atual,medidas_futura,input_medida)}")

st.write("## Conversor de sistema de unidades")
 