import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime

def plotar_grafico_dbo(datas, valores, titulo="DBO (mg/L) Canal Aeroporto",
                       ylabel="DBO (mg/L)", classe2=5, classe3=10,
                       ylim_max=100, figsize=(8, 6)):
    """
    Cria um gráfico no estilo do Excel fornecido.

    Parâmetros:
    -----------
    datas : list ou array
        Lista de datas (podem ser strings no formato 'DD/MM/YYYY' ou objetos datetime)
    valores : list ou array
        Valores de DBO correspondentes às datas
    titulo : str
        Título do gráfico
    ylabel : str
        Label do eixo Y
    classe2 : float
        Valor da linha CONAMA CLASSE 2
    classe3 : float
        Valor da linha CONAMA CLASSE 3
    ylim_max : float
        Valor máximo do eixo Y
    figsize : tuple
        Tamanho da figura (largura, altura)
    """

    # Converter datas para datetime se forem strings
    if isinstance(datas[0], str):
        datas_dt = pd.to_datetime(datas, format='%d/%m/%Y')
    else:
        datas_dt = pd.to_datetime(datas)

    # Criar figura e eixos
    fig, ax = plt.subplots(figsize=figsize, facecolor='white')

    # Plotar os pontos de DBO com marcadores quadrados azuis
    ax.plot(datas_dt, valores, marker='s', color='#4472C4',
            linestyle='', markersize=6, label='DBO (mg/L)')

    # Linhas horizontais CONAMA
    ax.axhline(y=classe2, color='#FFC000', linewidth=2,
               label='CONAMA CLASSE 2', linestyle='-')
    ax.axhline(y=classe3, color='#C00000', linewidth=2,
               label='CONAMA CLASSE 3', linestyle='-')

    # Configurar grid
    ax.grid(True, which='major', axis='both', linestyle='-',
            linewidth=0.5, color='#D3D3D3', alpha=0.7)
    ax.set_axisbelow(True)

    # Configurar eixos
    ax.set_ylim(0, ylim_max)
    ax.set_xlim(min(datas_dt), max(datas_dt))

    # Labels e título
    ax.set_xlabel('')
    ax.set_ylabel(ylabel, fontsize=10)
    ax.set_title(titulo, fontsize=11, pad=10)

    # Formatar eixo X com datas
    import matplotlib.dates as mdates
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
    plt.xticks(rotation=90, fontsize=8)

    # Ajustar os ticks do eixo Y
    y_ticks = np.arange(0, ylim_max + 10, 10)
    ax.set_yticks(y_ticks)
    ax.tick_params(axis='y', labelsize=9)

    # Configurar borda do gráfico
    ax.spines['top'].set_visible(True)
    ax.spines['right'].set_visible(True)
    ax.spines['bottom'].set_visible(True)
    ax.spines['left'].set_visible(True)

    # Adicionar legenda
    ax.legend(loc='upper right', frameon=True, fontsize=8,
              fancybox=False, edgecolor='black')

    # Ajustar layout
    plt.tight_layout()

    return fig, ax


# EXEMPLO DE USO COM OS DADOS DO SEU GRÁFICO
if __name__ == "__main__":
    # Dados do gráfico fornecido (exemplo aproximado)
    datas_exemplo = [
        '01/01/2018', '03/05/2018', '01/11/2018',
        '01/04/2019', '01/09/2019',
        '01/04/2020', '01/07/2020',
        '01/12/2020', '01/05/2021', '01/08/2021',
        '01/10/2021', '01/03/2022', '01/08/2022'
    ]

    valores_exemplo = [
        40, 45, 30, 55, 40, 45, 40, 5, 10, 30, 80, 30, 15, 30, 50
    ][:len(datas_exemplo)]  # Ajustar ao número de datas

    # Criar o gráfico
    fig, ax = plotar_grafico_dbo(
        datas=datas_exemplo,
        valores=valores_exemplo,
        titulo="DBO (mg/L) Canal Aeroporto",
        ylabel="",
        classe2=5,
        classe3=10,
        ylim_max=90
    )

    # Salvar ou mostrar
    plt.savefig('grafico_dbo.png', dpi=300, bbox_inches='tight')
    print("Gráfico salvo como 'grafico_dbo.png'")

    # Para exibir na tela (descomente se quiser visualizar)
    # plt.show()


# EXEMPLO SIMPLES - Como usar com seus próprios dados:
"""
# Seus dados
minhas_datas = ['01/01/2023', '15/02/2023', '30/03/2023']
meus_valores = [25, 35, 15]

# Criar gráfico
fig, ax = plotar_grafico_dbo(minhas_datas, meus_valores)

# Salvar
plt.savefig('meu_grafico.png', dpi=300, bbox_inches='tight')
plt.show()
"""
