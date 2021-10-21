
class Grille:
    def __init__(self):
        self.grille=[]
        for line in range(6):
            nvline=[]
            for colone in range(7):
                nvline.append([])    
            self.grille.append(nvline)
        
       
    def ajout_pion(self,colonne):
        self.grille[5][colonne-1]=1
        print(self.grille)


        