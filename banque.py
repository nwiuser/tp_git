from client import Client
from compte import Compte

class Banque:
    """
    Classe représentant une banque, qui gère des clients et des comptes.
    """

    def __init__(self, nom):
        """
        Constructeur de la classe Banque.
        :param nom: Nom de la banque
        """
        self.nom = nom
        self.clients = []  # Liste des objets Client
        self.comptes = []  # Liste des objets Compte

    #Ajouter un client
    def ajouter_client(self, client):
        """
        Ajoute un client à la banque.
        """
        if isinstance(client, Client):
            self.clients.append(client)
            print(f"✅ Nouveau client ajouté : {client.prenom} {client.nom}")
        else:
            print("❌ L'objet fourni n'est pas un client valide.")

    #Ajouter un compte
    def ajouter_compte(self, compte, id_client):
        """
        Ajoute un compte à la banque et au client correspondant.
        """
        if isinstance(compte, Compte):
            self.comptes.append(compte)

            # associer au client s’il existe
            client = self.trouver_client(id_client)
            if client:
                client.ajouter_compte(compte)
            print(f"Compte {compte.numero} ajouté à la banque avec succées.")
        else:
            print("L'objet fourni n'est pas un compte valide.")

    #Trouver un client par ID
    def trouver_client(self, id_client):
        """
        Recherche un client par identifiant.
        """
        for client in self.clients:
            if client.id_client == id_client:
                return client
        return None

    # 🔹 Trouver un compte par numéro
    def trouver_compte(self, numero):
        """
        Recherche un compte par numéro.
        """
        for compte in self.comptes:
            if compte.numero == numero:
                return compte
        return None

    # 🔹 Effectuer un dépôt
    def deposer(self, numero_compte, montant):
        compte = self.trouver_compte(numero_compte)
        if compte:
            compte.deposer(montant)
        else:
            print("Compte introuvable.")

    #Effectuer un retrait
    def retirer(self, numero_compte, montant):
        compte = self.trouver_compte(numero_compte)
        if compte:
            compte.retirer(montant)
        else:
            print("Compte introuvable.")

    #Afficher les comptes de la banque
    def afficher_comptes(self):
        """
        Affiche tous les comptes enregistrés dans la banque.
        """
        print(f"🏦 Comptes enregistrés dans {self.nom} :")
        for compte in self.comptes:
            print("   ", compte)

    #Afficher les clients
    def afficher_clients(self):
        """
        Affiche tous les clients enregistrés dans la banque.
        """
        print(f"Clients de {self.nom} :")
        for client in self.clients:
            print("   ", client)

    def __str__(self):
        return f"Banque {self.nom} : {len(self.clients)} client(s), {len(self.comptes)} compte(s)"
