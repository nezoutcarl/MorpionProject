#!/usr/bin/python
# -*-coding:utf-8 -*

import socket

def connexion():
    global connexion_avec_client, infos_connexion, connexion_principale

    connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connexion_principale.bind((HOST, PORT))
    connexion_principale.listen(5)
    print('#Le serveur écoute à présent sur le port ',PORT,'.')
    connexion_avec_client, infos_connexion = connexion_principale.accept()
    dialogue()

def envoyer(message):
    message=message.encode()
    connexion_avec_client.send(message)

def recevoir():
    msg_recu = connexion_avec_client.recv(1024)
    msg_recu=msg_recu.decode()
    return msg_recu

def dialogue():
    while 1:
        msg_recu=recevoir()
        print(msg_recu)
        message = input("Entrez votre message: ")
        print(message)
        envoyer(message)

    print("Fermeture de la connexion")
    connexion_avec_client.close()
    connexion_principale.close()

HOST = ''
PORT = 0

def initialisation():
	# Création de la fenêtre principale (main window)
	print("## Mise en réseau - Serveur")
	HOST = '127.0.0.1'
	try:
		p = input("#Choix du port : (valeur entre 49152 et 65535\n")
		p = int(p)
		if (p < 49152) or (p > 65535):
			raise ValueError("Attention, domaine de port incorrect")
	except ValueError:
		print("Respecter l'ensemble de valeur svp")
	except TypeError:
		print("Type incompatible")
	except NameError:
		print("### ERREUR -> Saisie invalide, veuillez relancer une demande de serveur")
	else: #Si on arrive là tous les paramètres ont été saisie correctement
		PORT = p
		connexion()
		print("Serveur initialisé avec succès.")

initialisation()