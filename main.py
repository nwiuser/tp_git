from banque import Banque

class Main:
    @staticmethod
    def menu():
        banque = Banque("MaBanque")

        while True:
            print("\n=== MENU BANQUE ===")
            print("1. Créer un compte")
            print("2. Dépôt")
            print("3. Retrait")
            print("4. Consulter le solde")
            print("5. Afficher l’historique des transactions")

            print("6. Effectuer un virement")
            print("7. Quitter")
            

            choix = input("Votre choix : ")

            if choix == "1":
                nom = input("Nom du client : ")
                numero = input("Numéro du compte : ")
                banque.creer_compte(numero, nom)

            elif choix == "2":
                numero = input("Numéro du compte : ")
                montant = float(input("Montant à déposer : "))
                banque.depot(numero, montant)

            elif choix == "3":
                numero = input("Numéro du compte : ")
                montant = float(input("Montant à retirer : "))
                banque.retrait(numero, montant)

            elif choix == "4":
                numero = input("Numéro du compte : ")
                banque.consulter_solde(numero)

            elif choix == "5":
                numero = input("Numéro du compte : ")
                banque.afficher_historique(numero)
            elif choix == "6":  
                source = input("Numéro du compte source : ")
                cible = input("Numéro du compte cible : ")
                montant = float(input("Montant à virer : "))
                banque.virement(source, cible, montant)
            
            elif choix == "7":
                print("Merci d’avoir utilisé MaBanque. À bientôt !")
                break

            else:
                print("Choix invalide, veuillez réessayer.")


if __name__ == "__main__":
    Main.menu()
