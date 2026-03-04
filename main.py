from src.menu import run_menu
from src.scraper import ajout_livre

biblio = ajout_livre()
menu = run_menu(biblio)

print(menu)