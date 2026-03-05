import matplotlib.pyplot as plt
import pandas as pd

def repartition_note(df: pd.DataFrame):
    data = df.groupby("Note").size()

    fig, ax = plt.subplots()
    ax.pie(
        data.values,
        labels=data.index,
        autopct="%.1f%%"
    )
    ax.set_title("Répartition des notes")
    return fig


def distribution_prix(df : pd.DataFrame):
    fig, ax = plt.subplots()
    ax.hist(df["Prix"])
    ax.set_title("Distribution des prix")
    ax.set_xlabel("Prix (€)")
    ax.set_ylabel("Nombre de livres")
    return fig