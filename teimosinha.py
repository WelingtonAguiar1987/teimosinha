import pandas as pd
import numpy as np
import streamlit as st

# LISTA DE DADOS DOS JOGOS POR DEZENAS:
lista_dezenas = {
    'Números': [15, 16, 17, 18, 19, 20],
    'Valor em R$': [3, 48, 408, 2448, 11628, 46512]
}

# LISTA DE DADOS DOS JOGOS POR TEIMOSINHA:
lista_teimosinha = {
    'Números': [1, 3, 6, 9, 12, 18, 24],
    'Valor em R$': [3, 9, 18, 27, 36, 54, 72]
}


# LISTA DE DADOS DOS JOGOS POR DEZENAS:
lista_probabilidade = {
    'Números': [15, 16, 17, 18, 19, 20],
    'Probabilidade': [3268760, 204298, 24035, 4006, 843, 211]
}

# GERANDO OS DATAFRAMES COM DADOS DOS JOGOS E VALORES:
df_dezenas = pd.DataFrame(lista_dezenas)
df_teimosinha = pd.DataFrame(lista_teimosinha)
df_probabilidade = pd.DataFrame(lista_probabilidade)

df1 = df_dezenas.set_index(['Números'])
df2 = df_teimosinha.set_index(['Números'])
df3 = df_probabilidade.set_index(['Números'])

# CONFIGURAÇÃO DE PÁGINA:
st.set_page_config(page_title='JOGOS DO PEZÃO',
                   page_icon='🎱 ', layout='wide')

st.title('JOGOS DO PEZÃO - LOTOFÁCIL 🎲')
st.sidebar.header('Controle dos Jogos: ', divider='rainbow')
st.sidebar.image('imagem_lotofacil.JPG')
total_numeros_aposta = st.sidebar.selectbox(
    'Selecione a Quantidade de Dezenas Desejada para este Jogo: ', list(lista_dezenas['Números']))


total_concurso_teimosinha = st.sidebar.selectbox(
    'Selecione a Quantidade de Concursos que Deseja Participar Neste Jogo: ', list(lista_teimosinha['Números']))

quantidade_jogos_realizar = st.sidebar.number_input(
    'Digite a Quantidade de Jogos que Deseja Realizar: ', value=1)

quantidade_jogador = st.sidebar.number_input(
    'Digite a Quantidade de Jogadores: ', value=1)


valor_premio = st.sidebar.number_input(
    'Digite o Valor Total do Prêmio: ', value=0)

# CONDICIONAL PARA O PREÇO DAS APOSTAS SIMPLES:
if total_numeros_aposta == 15:
    valor_aposta = 3

elif total_numeros_aposta == 16:
    valor_aposta = 48

elif total_numeros_aposta == 17:
    valor_aposta = 408

elif total_numeros_aposta == 18:
    valor_aposta = 2448

elif total_numeros_aposta == 19:
    valor_aposta = 11628

elif total_numeros_aposta == 20:
    valor_aposta = 46512


# CONDICIONAL PARA O PREÇO DAS APOSTAS POR TEIMOSINHAS:
if total_concurso_teimosinha == 1:
    valor_teimosinha = 3

elif total_concurso_teimosinha == 3:
    valor_teimosinha = 9

elif total_concurso_teimosinha == 6:
    valor_teimosinha = 18

elif total_concurso_teimosinha == 9:
    valor_teimosinha = 27

elif total_concurso_teimosinha == 12:
    valor_teimosinha = 36

elif total_concurso_teimosinha == 18:
    valor_teimosinha = 54

elif total_concurso_teimosinha == 24:
    valor_teimosinha = 72

# CONDICIONAL PRINTANDO TEXTOS TEIMOSINHA:
if total_concurso_teimosinha == 1:
    mostrar_texto = 'Aposta Simples'

else:
    mostrar_texto = 'Teimosinha'


# CONDICIONAL PARA PROBABILIDADE:
if total_numeros_aposta == 15:
    probabilidade = 3268760

elif total_numeros_aposta == 16:
    probabilidade = 204298

elif total_numeros_aposta == 17:
    probabilidade = 24035

elif total_numeros_aposta == 18:
    probabilidade = 4006

elif total_numeros_aposta == 19:
    probabilidade = 843

elif total_numeros_aposta == 20:
    probabilidade = 211

# VARIÁVEIS DE CONTROLE:
custo_aposta_lotofacil = valor_aposta * total_concurso_teimosinha
custo_teimosinha = custo_aposta_lotofacil * total_numeros_aposta

premio_por_jogador = valor_premio / quantidade_jogador
valor_arrecadado = custo_aposta_lotofacil * quantidade_jogos_realizar
valor_jogador = valor_arrecadado / quantidade_jogador

st.header('Dados das Apostas', divider='rainbow')
st.write(f'Valor da Aposta Simples Lotofácil:  :blue[ R$ {valor_aposta:.2f}]')
st.write(f'Custo da {mostrar_texto}: :blue[ R$ {custo_aposta_lotofacil:.2f}]')
st.write(f'Valor a Pagar por cada Jogador:  :red[ R$ {valor_jogador:.2f}]')
st.write(f'Valor Arrecadado:  :green[ R$ {valor_arrecadado:.2f}]')
st.write(f'Valor do Prêmio:  :green[ R$ {valor_premio:.2f}]')
st.write(f'Valor do Prêmio por Jogador:  :green[ R$ {premio_por_jogador:.2f}]')


st.header('Probabilidades', divider='rainbow')

probabilidade_jogos_simples = probabilidade
tentativas = total_concurso_teimosinha * quantidade_jogos_realizar
probabilidade_deste_jogo = probabilidade_jogos_simples / tentativas

st.write(f'Probabilidade de Jogos Simples Lotofácil: :orange[{
         probabilidade_jogos_simples}]')
st.write(f'Concorrerá por: :orange[{tentativas}] Tentativas.')
st.write(f'Probabilidade com essa Estratégia: :orange[ {
         probabilidade_deste_jogo:.0f}]')
st.header('', divider='rainbow')


# DATAFRAMES:
st.subheader('PREÇO POR QUANTIDADE DE DEZENAS: ')
st.dataframe(df1)

st.subheader('PREÇO POR TEIMOSINHA: ')
st.dataframe(df2)

st.subheader('PROBABILIDADES: ')
st.dataframe(df3)
