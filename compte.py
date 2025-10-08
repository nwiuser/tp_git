from transaction import Transaction

class Compte:
    def __init__(self, numero, proprietaire, solde=0,taux_interet=0.03):
        self.numero = numero
        self.proprietaire = proprietaire
        self.solde = solde
        self.transactions = []  # Liste des transactions
        self.taux_interet = taux_interet
        self.taux_interet = taux_interet

    def deposer(self, montant):
        self.solde += montant
        transaction = Transaction(len(self.transactions) + 1, montant, "dépôt", self)
        self.transactions.append(transaction)
        print(f"Dépôt de {montant} € effectué sur le compte {self.numero}")

    def retirer(self, montant):
        if montant <= 0:
            print("Le montant du retrait doit être supérieur à 0.")
            return

        if montant > self.solde:
            print(f"Solde insuffisant ! Retrait de {montant} € impossible. Solde actuel : {self.solde} €.")
            return

        self.solde -= montant
        transaction = Transaction(
            len(self.transactions) + 1,
            montant,
            "retrait",
            self
        )
        self.transactions.append(transaction)
        print(f"✅ Retrait de {montant} € effectué avec succès sur le compte {self.numero}.")
        print(f"Nouveau solde : {self.solde} €.")


    def afficher_solde(self):
        print(f"Solde du compte {self.numero}: {self.solde} €")

    # Étape 3 : afficher l’historique des transactions
    def afficher_historique(self):
        print(f"\nHistorique des transactions du compte {self.numero}:")
        if not self.transactions:
            print("Aucune transaction.")
        else:
            for t in self.transactions:
                print(t)

    def calculer_interets(self, duree_en_jours):
        """
        Calcule les intérêts simples pour une période donnée (en jours).
        """
        interets = self.solde * self.taux_interet * (duree_en_jours / 365)
        print(f"Intérêts pour {duree_en_jours} jours : {interets:.2f} €")
        return interets       

    def capitaliser_interets(self, duree_en_jours):
        interets = self.calculer_interets(duree_en_jours)
        self.solde += interets
        # On peut aussi créer une transaction spéciale pour l'intérêt
        transaction = Transaction(len(self.transactions) + 1, interets, "intérêt", self)
        self.transactions.append(transaction)
        print(f"✅ Intérêts de {interets:.2f} € ajoutés au compte {self.numero}. Nouveau solde : {self.solde:.2f} €")
     
