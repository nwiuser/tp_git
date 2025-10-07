from banque import Banque
from compte import Compte
from client import Client
from transaction import Transaction

def main():
    # Création de la banque
    banque = Banque("Banque Python")

    # Création d’un client et d’un compte
    client1 = Client("Benomar", "Ali")
    compte1 = Compte("001", 1000)

