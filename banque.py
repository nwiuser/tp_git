from compte import Compte

class Banque:
    def __init__(self, nom):
        self.nom = nom
        self.comptes = {}

    def creer_compte(self, numero, proprietaire):
        if numero not in self.comptes:
            self.comptes[numero] = Compte(numero, proprietaire)
            print(f"✅ Compte {numero} créé pour {proprietaire}.")
        else:
            print("⚠️ Ce numéro de compte existe déjà.")

    def get_compte(self, numero):
        return self.comptes.get(numero)

    def depot(self, numero, montant):
        compte = self.get_compte(numero)
        if compte:
            compte.deposer(montant)
        else:
            print("Compte introuvable.")

    def retrait(self, numero, montant):
        compte = self.get_compte(numero)
        if compte:
            compte.retirer(montant)
        else:
            print("Compte introuvable.")

    def consulter_solde(self, numero):
        compte = self.get_compte(numero)
        if compte:
            compte.afficher_solde()
        else:
            print("Compte introuvable.")

    def afficher_historique(self, numero):
        compte = self.get_compte(numero)
        if compte:
            compte.afficher_historique()
        else:
            print("Compte introuvable.")
