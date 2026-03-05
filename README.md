# Books Scraper & Analyzer

Projet Python de scraping et d’analyse de données à partir du site
https://books.toscrape.com

## Fonctionnalités
- Scraping multi-pages
- Nettoyage et structuration des données
- Analyse statistique (prix et notes)
- Visualisations avec matplotlib
- Export CSV

## Stack technique
- Python
- BeautifulSoup4
- pandas
- numpy
- matplotlib

## Architecture du projet
```text
BOOKTOSCRAPE
│
├─ data/                  # Pour exporter la bibliothèque en CSV
│   └─ __init__.py
│
├─ src/             # Fonctions utilisables
│   ├─ __init__.py
│   └─ export.py
│   └─ menu.py
│   └─ objet_livre.py
│   └─ scraper.py
│   └─ stats.py
│   └─ utils_df.py
│   └─ visualisation.py
│
├─ main.py         # script à lancer
├─ requirements.txt
└─ README.md
```

## Lancer le projet
```bash
pip install -r requirements.txt
python main.py