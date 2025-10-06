# 🌧️ Análise de Risco de Inundação

Este repositório contém scripts em **Python** para classificar áreas de uma cidade de acordo com o risco de inundação, com base em variáveis como **altitude**, **distância até rios** e **histórico de alagamentos**.

## 📁 Estrutura

```
data/
└── dataset_enriquecido_com_risco_2.csv   # Dataset final com classificação
src/
├── classificar_risco_basico.py           # Script simples de classificação
└── classificar_risco_avancado.py         # Versão robusta com validação e logs
```

## ⚙️ Requisitos

- Python 3.9+
- pandas

Instalação:
```bash
pip install -r requirements.txt
```

## 🚀 Uso

### Script Básico
```bash
python src/classificar_risco_basico.py
```

### Script Avançado
```bash
python src/classificar_risco_avancado.py
```

Os scripts geram um novo arquivo CSV com a coluna `Risco_Alagamento` ou `classificacao`, conforme a versão usada.

## 📊 Fonte dos Dados
Os dados foram enriquecidos com variáveis ambientais e históricas e estão disponíveis em `data/dataset_enriquecido_com_risco_2.csv`.

## 🧠 Autor
Projeto desenvolvido por **Zyra (2025)**.
