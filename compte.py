from transaction import Transaction

class Compte:
    def __init__(self, numero, proprietaire, solde=0):
        self.numero = numero
        self.proprietaire = proprietaire
        self.solde = solde
        self.transactions = []  # Liste des transactions

    def deposer(self, montant):
        self.solde += montant
        transaction = Transaction(len(self.transactions) + 1, montant, "dépôt", self)
        self.transactions.append(transaction)
        print(f"Dépôt de {montant} € effectué sur le compte {self.numero}")


# modifié par zakaria sur branch devB
    def retirer(self, montant):
    # Vérification de la validité du montant
        if montant <= 0:
            print("❌ Le montant doit être supérieur à 0.")
            return False

        # Vérification du solde disponible
        if montant > self.solde:
            print("❌ Solde insuffisant !")
            return False

        # Exécution du retrait
        self.solde -= montant
        transaction = Transaction(
            len(self.transactions) + 1,
            montant,
            "retrait",
            self
        )
        self.transactions.append(transaction)

        print(f"✅ Retrait de {montant:.2f} € effectué sur le compte {self.numero}. Nouveau solde : {self.solde:.2f} €.")
        return True


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
