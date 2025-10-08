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
    
    def virement(self, numero_source, numero_cible, montant):
        compte_source = self.get_compte(numero_source)
        compte_cible = self.get_compte(numero_cible)
        if compte_source and compte_cible:
            if compte_source.solde >= montant:
                compte_source.retirer(montant)
                compte_cible.deposer(montant)
                print(f"✅ Virement de {montant}€ de {numero_source} vers {numero_cible} effectué.")
            else:
                print("⚠ Solde insuffisant pour le virement.")
        else:
            print("⚠ Un ou les deux comptes introuvables.")
            
