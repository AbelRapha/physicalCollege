import streamlit as st

st.write("## Conversor de medidas")

medidas_atual = st.selectbox("Selecione o tipo de medida atual", ["km/h","m/s","km", "m","dm","cm","mm","W","HP","pol","mmHg", "kgf/cm²","kg/m³","g/cm³","Btu/h", "litros","km³", "m³","dm³","cm³","mm³","km²", "m²","dm²","cm²","mm²"])

medidas_futura = st.selectbox("Selecione o tipo de medida futura",["km/h","m/s","km","m","dm","cm","mm","W","HP","pol","mmHg", "kgf/cm²","kg/m³","g/cm³","Btu/h", "litros","hm³","km³", "dam³" "m³","dm³","cm³","mm³","km²", "m²","dm²","cm²","mm²"])


input_medida = st.number_input("Digite o valor da medida")

def converte_medida(medida_atual, medida_futura, input_medida):
    match medida_atual:
        # Velocidade
        case "km/h":
            match medida_futura:
                case "m/s":
                    return input_medida / 3.6
                case "km/h":
                    return  input_medida
                case default:
                    return "Selecione tipos de medidas compatíveis para conversão"
        case "m/s": 
            match medida_futura:
                case "k/h":
                    return input_medida * 3.6
                case "m/s":
                    return input_medida
                case default:
                    return "Selecione tipos de medidas compatíveis para conversão"
        # Distância
        case "km":
            match medida_futura:
                case "m":
                    return input_medida * 1000
                case "dm":
                    return input_medida * 10000
                case "cm":
                    return input_medida * 100000
                case "mm":
                    return input_medida * 1000000
                case "km":
                    return input_medida
                case default:
                    return "Selecione tipos de medidas compatíveis para conversão"    

        case "m":
            match medida_futura:
                case "km":
                    return input_medida / 1000
                case "dm":
                    return input_medida * 10
                case "cm":
                    return input_medida * 100
                case "mm":
                    return input_medida * 1000
                case "m":
                    return input_medida
                case default:
                    return "Selecione tipos de medidas compatíveis para conversão"
        case "dm":
            match medida_futura:
                case "km":
                    return input_medida / 10000
                case "m":
                    return input_medida / 10
                case "dm":
                    return input_medida
                case "mm":
                    return input_medida * 100
                case "cm":
                    return input_medida * 10
                case default:
                    return "Selecione tipos de medidas compatíveis para conversão"
        case "cm":
            match medida_futura:
                case "km":
                    return input_medida / 100000
                case "m":
                    return input_medida / 100
                case "dm":
                    return input_medida / 10
                case "mm":
                    return input_medida * 10
                case "cm":
                    return input_medida
                case default:
                    return "Selecione tipos de medidas compatíveis para conversão"
        case "mm":
            match medida_futura:
                case "m":
                    return input_medida / 1000
                case "dm":
                    return input_medida / 100
                case "cm":
                    return input_medida / 10
                case "km":
                    return input_medida / 1000000
                case "mm":
                    return input_medida
                case default:
                    return "Selecione tipos de medidas compatíveis para conversão"
        # Área
        # Volume
        # Energia
        # Hidrodinâmica
       


st.write(f"{converte_medida(medidas_atual,medidas_futura,input_medida)}")

st.write("## Conversor de sistema de unidades")
 