# Le Jackpot par DECORTE Anthony du TPE

from tkinter import *
import random
fenetre=Tk()
fenetre.title("Jackpot")
fenetre.geometry("1200x800")
fenetre.config(background="darkred")
fenetre.resizable(width=True, height=True)

fond=Canvas(fenetre, width = 700, height = 900, bg = "white", highlightthickness = 5, highlightbackground = "black")

fond.pack()

# Fonction de clic gauche
def fenetreClique(event):
    
    debx = 35 # Position horizontale du rectangle
    deby = 200 # Position verticale du rectangle
    finx = debx + 200 # Largeur du rectangle
    finy = deby + 200 # Hauteur du rectangle
    
    # Tableau de cinq couleurs 
    tcouleur = ["darkred", "darkgreen", "orange", "pink", "darkblue"]

    # Tableau pour renvoyer le résultat
    tresultat = []

    # Nombre de rectangles souhaités
    nbrectangle = 3

    # Création des rectangles
    for i in range(nbrectangle):
        grand_rectangle = fond.create_rectangle(debx, deby, finx, finy, outline = "black", width = "5")
        debx2 = debx + 25
        deby2 = deby + 50
        finx2 = debx2 + 150
        finy2 = deby2 + 100
        couleur = random.choice(tcouleur)
        tresultat.append(couleur)
        petit_rectangle = fond.create_rectangle(debx2, deby2, finx2, finy2, outline = "black", width = "3", fill = couleur)
        debx = finx + 20
        finx = debx + 200

    # Message de victoire
    if(tresultat[0]!=tresultat[1] or tresultat[2]!=tresultat[1] or tresultat[2]!=tresultat[0]):
        fond.create_text(350, 550, text = "Gagné !", font = "Verdana 30 bold italic", fill = "white")
    elif(tresultat[0]==tresultat[1] and tresultat[2]==tresultat[1] and tresultat[2]==tresultat[0]):
        fond.create_text(350, 550, text = "Gagné !", font = "Verdana 30 bold italic", fill = "darkred")

# Bouton pour quitter
bouton_quitter = Button(fenetre, text = "Quitter", font = "Verdana 10", width = 15, bg = "grey", command = exit)
bouton_quitter.place(x= 25, y = 25)
fenetre.bind("<Button-1>", fenetreClique)

fenetre.mainloop()