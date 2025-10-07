class Compte:
    """
    Classe représentant un compte bancaire.
    """

    def __init__(self, numero, proprietaire, solde_initial=0.0):
        """
        Constructeur de la classe Compte.
        :param numero: Numéro du compte (str ou int)
        :param proprietaire: Nom du propriétaire (str)
        :param solde_initial: Solde de départ (float)
        """
        self.numero = numero
        self.proprietaire = proprietaire
        self.solde = solde_initial

    #Méthode pour déposer de l'argent
    def deposer(self, montant):
        """
        Dépose un montant sur le compte.
        """
        if montant > 0:
            self.solde += montant
            print(f"✅ Dépôt de {montant} DH effectué avec succès.")
        else:
            print("❌ Le montant doit être positif.")

    #Méthode pour retirer de l'argent
    def retirer(self, montant):
        """
        Retire un montant du compte si le solde est suffisant.
        """
        if montant <= 0:
            print("❌ Le montant doit être positif.")
        elif montant > self.solde:
            print("❌ Solde insuffisant.")
        else:
            self.solde -= montant
            print(f"✅ Retrait de {montant} DH effectué avec succès.")

    #Méthode pour consulter le solde
    def afficher_solde(self):
        """
        Affiche le solde actuel du compte.
        """
        print(f"💰 Solde du compte {self.numero} : {self.solde} DH")

    #Représentation sous forme de texte
    def __str__(self):
        return f"Compte n°{self.numero} - Propriétaire : {self.proprietaire} - Solde : {self.solde} DH"
