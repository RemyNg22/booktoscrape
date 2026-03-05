from src.menu import run_menu
from src.scraper import ajout_livre
import time
import threading

def animation(stop_event):
    while not stop_event.is_set():
        for c in ".oO°":
            print(c, end="", flush=True)
            time.sleep(0.3)
            print("\b", end="", flush=True)

def main():
    """
    Point d'entrée du projet. Scrape les livres puis lance le menu 'menu.py'.
    Compatible avec un package GitHub complet.
    A lancer en faisant 'python main.py'
    """

    print("Scraping des livres en cours, cela peut prendre quelques minutes ", end="", flush=True)

    stop_event = threading.Event()
    thread = threading.Thread(target=animation, args=(stop_event,))
    thread.start()

    df = ajout_livre()

    stop_event.set()
    thread.join()

    print(f"\n{len(df)} livres récupérés !\n")

    run_menu(df)

if __name__ == "__main__":
    main()
