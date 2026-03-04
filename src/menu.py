from src.stats import statistiques

def run_menu(df):
    stats = statistiques()

    while True:
        print("\n=== Bibliothèque BOOKS TO SCRAPE ===")
        print("1 - Voir tous les livres")
        print("2 - Voir les livres les mieux notés")
        print("3 - Voir les livres les moins bien notés")
        print("4 - Voir les livres les moins chers")
        print("5 - Voir les livres les plus chers")
        print("6 - Afficher la moyenne des notes")
        print("7 - Afficher la note médiane")
        print("8 - Afficher la moyenne des prix")
        print("9 - Afficher le prix médian")
        print("10 - Graphique : répartition des notes")
        print("11 - Graphique : distribution des prix")
        print("12 - Exporter en CSV")
        print("13 - Quitter")

        try:
            choix = int(input("Votre choix : "))

        except ValueError:
            print("Veuillez entrer un nombre valide")
            continue

        match choix:

            case 1:
                print(df)

            case 2:
                print(stats['livres_mieux_notes'])
