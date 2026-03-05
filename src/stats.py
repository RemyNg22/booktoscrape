import src.scraper as sc
from src.utils_df import reset_index_liste

df_bibliotheque = sc.ajout_livre()

def statistiques():
    return {
        'livres_mieux_notes' : reset_index_liste(df_bibliotheque.sort_values('Note', ascending=False).head(10)),
        'livres_moins_notes' : reset_index_liste(df_bibliotheque.sort_values('Note', ascending=True).head(10)),
        'livres_moins_chers' : reset_index_liste(df_bibliotheque.sort_values('Prix', ascending=True).head(10)),
        'livres_plus_chers' : reset_index_liste(df_bibliotheque.sort_values('Prix', ascending=False).head(10)),
        'livres_note_moyenne' : round(df_bibliotheque['Note'].mean(), 2),
        'livres_note_mediane' : round(df_bibliotheque['Note'].median(), 2),
        'livres_prix_moyen' : round(df_bibliotheque['Prix'].mean(), 2),
    }