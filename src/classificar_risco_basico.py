import pandas as pd

arquivo_entrada = 'dataset_enriquecido.csv'
arquivo_saida = 'dataset_enriquecido_com_risco.csv'

try:
    df = pd.read_csv(arquivo_entrada, sep=';', decimal=',', engine='python')
except FileNotFoundError:
    print(f"Erro: arquivo não encontrado em {arquivo_entrada}")
    exit()
except Exception as e:
    print(f"Erro ao ler o CSV: {e}")
    exit()

df.columns = df.columns.str.strip()

for col in ['Dist_RIO_m', 'Altitude_m', 'Status_Inundacao']:
    if col in df.columns:
        df[col] = (
            df[col]
            .astype(str)
            .str.replace('.', '', regex=False)
            .str.replace(',', '.', regex=False)
            .astype(float)
        )
    else:
        print(f"Atenção: coluna '{col}' não encontrada no CSV.")

def classificar_risco(row):
    risco = 0

    if row.get('Status_Inundacao', 0) == 1:
        risco += 3

    altitude = row.get('Altitude_m', 0)
    if altitude < 10:
        risco += 3
    elif 10 <= altitude <= 20:
        risco += 2
    else:
        risco += 1

    dist_rio = row.get('Dist_RIO_m', 10000)
    if dist_rio < 500:
        risco += 3
    elif 500 <= dist_rio <= 1000:
        risco += 2
    else:
        risco += 1

    local_lower = str(row.get('Local', '')).lower()
    if any(x in local_lower for x in ['baixo', 'centro', 'rio']):
        risco += 1
    if any(x in local_lower for x in ['alto', 'colina', 'mor']):
        risco -= 1

    if risco >= 7:
        return 'Alto'
    elif 4 <= risco < 7:
        return 'Médio'
    else:
        return 'Baixo'

df['Risco_Alagamento'] = df.apply(classificar_risco, axis=1)
df.to_csv(arquivo_saida, sep=';', index=False, decimal=',', encoding='utf-8-sig')
print(f"Arquivo '{arquivo_saida}' gerado com sucesso!")