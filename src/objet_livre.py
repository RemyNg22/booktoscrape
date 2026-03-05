class Livre:

    def __init__(self, nom, prix, rating, stock):
        self.nom = nom
        self.prix = prix
        self.rating = rating
        self.stock = stock
    
    def prix_ttc(self, taux=0.15):
        return self.prix * (1+taux)
    
    @staticmethod
    def note_converti(note_brute):
        mapping_note = {
        "one" : 1,
        "two" : 2,
        "three" : 3,
        "four" : 4,
        "five" : 5}
        return mapping_note[note_brute]
    
    @staticmethod
    def en_stock(stock):
        if stock == "in stock":
            return "Disponible"
        else:
            return "Indisponible"
