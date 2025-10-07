from compte import Compte

class Client:
    """
    Classe représentant un client de la banque.
    """

    def __init__(self, id_client, nom, prenom):
        """
        Constructeur de la classe Client.
        :param id_client: Identifiant unique du client
        :param nom: Nom du client
        :param prenom: Prénom du client
        """
        self.id_client = id_client
        self.nom = nom
        self.prenom = prenom
        self.comptes = []  # liste d'objets Compte

    #Ajouter un compte
    def ajouter_compte(self, compte):
        """
        Ajoute un compte au client.
        """
        if isinstance(compte, Compte):
            self.comptes.append(compte)
            print(f"✅ Compte {compte.numero} ajouté pour {self.prenom} {self.nom}.")
        else:
            print("❌ L'objet ajouté n'est pas un compte valide.")

    #Supprimer un compte
    def supprimer_compte(self, numero_compte):
        """
        Supprime un compte du client selon son numéro.
        """
        for compte in self.comptes:
            if compte.numero == numero_compte:
                self.comptes.remove(compte)
                print(f"🗑️ Compte {numero_compte} supprimé avec succès.")
                return
        print("❌ Compte introuvable.")

    #Afficher les comptes du client
    def afficher_comptes(self):
        """
        Affiche tous les comptes du client.
        """
        if not self.comptes:
            print(f"ℹ️ {self.prenom} {self.nom} n’a aucun compte.")
        else:
            print(f"📋 Comptes de {self.prenom} {self.nom} :")
            for compte in self.comptes:
                print("   ", compte)

    #Représentation texte
    def __str__(self):
        return f"Client {self.id_client} : {self.prenom} {self.nom} ({len(self.comptes)} compte(s))"
