import src.scraper as sc

df_bibliotheque = sc.ajout_livre()

def statistiques():
    return {
        'livres_mieux_notes' : df_bibliotheque.sort_values('Note', ascending=False).head(),

    }