# tp_git

## Description  
Ce projet est un TP (travail pratique) de gestion de comptes bancaires. Il permet de simuler des opérations bancaires de base comme créer un client, créer des comptes, faire des transactions, etc.

## Structure du projet  
Voici les fichiers principaux et leur rôle :

| Fichier | Rôle |
|---|---|
| `main.py` | Point d’entrée — orchestration de l’exécution |
| `client.py` | Définition de la classe **Client** |
| `compte.py` | Définition de la classe **Compte** |
| `transaction.py` | Classe pour représenter les transactions (dépôt, retrait, etc.) |
| `banque.py` | Classe **Banque** qui gère tous les comptes, clients et opérations |
| `README.md` | Ce fichier de documentation |
| `__pycache__/` | Dossier généré automatiquement contenant les fichiers compilés |

## Prérequis  
- Python 3.x  
- (Optionnel) un environnement virtuel pour isoler les dépendances  

## Installation & exécution  
1. Clone le dépôt :  
   ```bash
   git clone https://github.com/nwiuser/tp_git.git
   cd tp_git
