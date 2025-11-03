from tkiteasy import *

g = ouvrirFenetre(800, 1000)
g.afficherImage(0,0, './fondbon.png', 800, 1000)

class Calc:
    def __init__(self):
        self.calc=[1,2,3,"A"],[4,5,6,"+"],[7,8,9,"-"],[0,"=","x","/"]

    def affichage(self):
        for i in range(4):
            for j in range(4):
                g.afficherImage(135 + 130*i,300 + 130*j, './casebon.png',120,115)
        g.afficherImage(125,50, './case2.png',530,230)
        g.actualiser()

        for i in range(4):
            for j in range(4):
                '''
                image = f"./{calc[i][j]}.png"
                g.afficherImage(171 + 130 * i, 334 + 130 * j, image, 50, 50)'''
                g.afficherTexte(self.calc[j][i],195 + 130 * i, 360 + 130 * j,"green",60)
        self.selection()
    def selection(self):
        l = []
        resul = g.afficherTexte("...",235,200 ,"green",60)
        boucle = True
        while boucle:
            clic = g.attendreClic()
            pos = (clic.x, clic.y)
            for i in range(4):
                for j in range(4):
                    if 150+i*130 < pos[0] < 240+i*130 and 307+j*130< pos[1] < 402+j*130:
                        l.append(self.calc[j][i])
                        g.supprimer(resul)
                        resul = g.afficherTexte(l,235 + (len(l)-1)*25 ,200 ,"green",60)

Calc = Calc()
Calc.affichage()