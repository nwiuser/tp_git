from datetime import datetime

class Transaction:
    def __init__(self, id, montant, type, compte_associe):
        self.id = id
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.montant = montant
        self.type = type  # "dépôt" ou "retrait"
        self.compte_associe = compte_associe

    def __str__(self):
        return f"[{self.date}] {self.type.capitalize()} de {self.montant} € sur le compte {self.compte_associe.numero}"
