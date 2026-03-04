import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from objet_livre import Livre
import pandas as pd

url = "https://books.toscrape.com/"

def get_soup(url):
    html = requests.get(url).text
    return BeautifulSoup(html, "html.parser")

def scrapping_cat():
    soup = get_soup(url)

    liste_categories = {}

    bloc_cat = soup.find("div", class_="side_categories")
    rech_cat = bloc_cat.find_all("a")

    for r in rech_cat:

        cat = r.get_text(strip=True)
        lien_cat = urljoin(url, r["href"])
        if cat != 'Books':
            liste_categories[cat] = lien_cat        


    return liste_categories

def ajout_livre():
    liste_cat = scrapping_cat()
    liste_livre = []

        
    for lien in liste_cat.values():
        url_cat = lien
        while True:
            
            scrapping = get_soup(url_cat)

            product = scrapping.find_all("article", class_="product_pod")

            for l in product:
                nom_livre = l.find("h3").find("a")["title"]
                prix_ht = l.find("p", class_="price_color").get_text(strip=True)[2:]
                notation = l.find("p", class_="star-rating")["class"][1].lower()
                note = Livre.note_converti(notation)
                in_stock = l.find("p", class_="instock availability").get_text(strip=True).lower()
                stock = Livre.en_stock(in_stock)
                
                try:
                    prix_ht = float(prix_ht)
                    livre = Livre(nom_livre, prix_ht, note, stock)

                    bon_prix = round(livre.prix_ttc(),2)

                    liste_livre.append({"Nom" : livre.nom, 
                                        "Prix" : bon_prix, 
                                        "Note" : livre.rating,
                                        "Stock" : livre.stock})
                except:
                    continue
                
            trouver_page_suivante = scrapping.find("li", class_="next")

            if trouver_page_suivante:
                nouvelle_page = trouver_page_suivante.find("a")["href"]
                url_cat = urljoin(lien, nouvelle_page)
            else:
                break
    
    return pd.DataFrame(liste_livre)

