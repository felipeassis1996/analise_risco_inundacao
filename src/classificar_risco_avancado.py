import pandas as pd
import sys

nome_do_arquivo = 'dataset_enriquecido.csv'

try:
    try:
        df = pd.read_csv(nome_do_arquivo, sep=';')
    except Exception:
        df = pd.read_csv(nome_do_arquivo, sep=',')
except FileNotFoundError:
    print(f"Arquivo não encontrado: '{nome_do_arquivo}'")
    sys.exit()
except Exception as e:
    print(f"Erro ao ler o arquivo: {e}")
    sys.exit()

df.columns = df.columns.str.lower().str.replace(' ', '_').str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
colunas_necessarias = ['dist_rio_m', 'altitude_m', 'uos', 'tipo_ponto']
colunas_faltando = [c for c in colunas_necessarias if c not in df.columns]

if colunas_faltando:
    print(f"Colunas faltando: {colunas_faltando}")
    sys.exit()

df['dist_rio_m'] = pd.to_numeric(df['dist_rio_m'], errors='coerce')
df['altitude_m'] = pd.to_numeric(df['altitude_m'], errors='coerce')
df.fillna({'dist_rio_m': 0, 'altitude_m': 0}, inplace=True)

def classificar_ponto(row):
    score = 0
    if row['dist_rio_m'] < 500:
        score += 3
    elif row['dist_rio_m'] < 1000:
        score += 2
    else:
        score += 1

    if row['altitude_m'] < 10:
        score += 3
    elif row['altitude_m'] < 25:
        score += 2
    else:
        score += 1

    if str(row['uos']).lower() == 'urbano':
        score += 2
    else:
        score += 1

    if str(row['tipo_ponto']).lower() == 'histórico':
        score += 3

    if score >= 9:
        return 'Alto'
    elif score >= 6:
        return 'Médio'
    else:
        return 'Baixo'

df['classificacao'] = df.apply(classificar_ponto, axis=1)
df.to_csv('dataset_enriquecido_com_risco_2.csv', index=False, sep=';', encoding='utf-8-sig')
print("Arquivo 'dataset_enriquecido_com_risco_2.csv' gerado com sucesso!")