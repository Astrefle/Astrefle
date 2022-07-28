from cgitb import text
from tkinter import*
from tkinter.font import BOLD

def crea_fiche(self):
    fiche = Tk()
    fiche.geometry('600x1000')
    fiche.title(f'Fiche de {self.nom}')
    fiche['bg'] = 'black'
    fiche.resizable(height=False, width=False)

    nom = Label(fiche, text=f'{self.nom}', font=(
        "Gentium basic", 30, 'bold'), fg="white", bg='black')
    nom.place(x='25', y='25')

    classe = Label(fiche, text=f'{self.classe}', font=(
        "Gentium basic", 18, 'bold'), fg="white", bg='black')
    classe.place(x='400', y='10')

    ville = Label(fiche, text=f'{self.ville}', font=(
        "Gentium basic", 18, 'bold'), fg="white", bg='black')
    ville.place(x='400', y='60')

    race = Label(fiche, text=f'{self.race}', font=(
        "Gentium basic", 23, 'bold'), fg="white", bg='black')
    race.place(x='315', y='125')

    dieux = Label(fiche, text=f'{self.dieux}', font=(
        "Gentium basic", 23, 'bold'), fg="white", bg='black')
    dieux.place(x='470', y='125')

    metier = Label(fiche, text=f'{self.metier}', font=(
        "Gentium basic", 20, 'bold'), fg="white", bg='black')
    metier.place(x='310', y='225')

    animal=Label(fiche,text=' ', font=(
        "Gentium basic", 20, 'bold'), fg="white", bg='black')
    animal.place(x='470', y='225')

    PV = Label(fiche, text=self.pv, font=(
        "Gentium basic", 20, 'bold'), fg="white", bg='black')
    PV.place(x='315', y='305')

    E = Label(fiche, text=self.e, font=(
        "Gentium basic", 20, 'bold'), fg="white", bg='black')
    E.place(x='500', y='305')

    Force = Label(fiche, text=self.F, font=(
        "Gentium basic", 20, 'bold'), fg="white", bg='black')
    Force.place(x='315', y='355')

    Defense = Label(fiche, text=self.D, font=(
        "Gentium basic", 20, 'bold'), fg="white", bg='black')
    Defense.place(x='500', y='355')

    arme = Label(fiche, text=f'{self.arme} en {self.arme_mat}(+{self.arme_totale})',
                 font=("Gentium basic", 15, 'bold'), fg="white", bg='black')
    arme.place(x='315', y='415')

    armure = Label(fiche, text=' ', font=(
        "Gentium basic", 15, 'bold'), fg="white", bg='black')
    armure.place(x='315', y='450')

    bonus1 = Label(fiche, text=f'{self.bonus1}', font=(
        "Gentium basic", 10, 'bold'), fg="white", bg='black')
    bonus1.place(x='310', y='525')
    bonus2 = Label(fiche, text=f'{self.bonus2}', font=(
        "Gentium basic", 10, 'bold'), fg="white", bg='black')
    bonus2.place(x='310', y='590')
    bonus3 = Label(fiche, text=f'{self.bonus3}', font=(
        "Gentium basic", 10, 'bold'), fg="white", bg='black')
    bonus3.place(x='310', y='655')

    malus1 = Label(fiche, text=f'{self.malus1}', font=(
        "Gentium basic", 10, 'bold'), fg="white", bg='black')
    malus1.place(x='460', y='525')
    malus2 = Label(fiche, text=f'{self.malus2}', font=(
        "Gentium basic", 10, 'bold'), fg="white", bg='black')
    malus2.place(x='460', y='590')
    malus3 = Label(fiche, text=f'{self.malus3}', font=(
        "Gentium basic", 10, 'bold'), fg="white", bg='black')
    malus3.place(x='460', y='655')

    comp_r_f = Label(fiche, text=f'{self.competencef}', font=(
        "Gentium basic", 10, 'bold'), fg="white", bg='black')
    comp_r_f.place(x='308', y='740')
    df = Label(fiche, text="D4", font=(
        "Gentium basic", 20, 'bold'), fg="white", bg='black')
    df.place(x='467', y='730')
    d1 = Label(fiche, text="10", font=(
        "Gentium basic", 20, 'bold'), fg="white", bg='black')
    d1.place(x='542', y='730')

    comp_r_m = Label(fiche, text=f'{self.competencem}', font=(
        "Gentium basic", 10, 'bold'), fg="white", bg='black')
    comp_r_m.place(x='308', y='840')
    dm = Label(fiche, text="D6", font=(
        "Gentium basic", 20, 'bold'), fg="white", bg='black')
    dm.place(x='467', y='830')
    d2 = Label(fiche, text="13", font=(
        "Gentium basic", 20, 'bold'), fg="white", bg='black')
    d2.place(x='542', y='830')

    comp_r_p = Label(fiche, text=f'{self.competencep}', font=(
        "Gentium basic", 10, 'bold'), fg="white", bg='black')
    comp_r_p.place(x='308', y='940')
    dp = Label(fiche, text="D10", font=(
        "Gentium basic", 20, 'bold'), fg="white", bg='black')
    dp.place(x='467', y='930')
    d3 = Label(fiche, text="15", font=(
        "Gentium basic", 20, 'bold'), fg="white", bg='black')
    d3.place(x='542', y='930')

    liste_bonus_guerrier = Label(fiche, text=f'{self.liste_bonus_guerrier}', font=(
        "Gentium basic", 14, 'bold'), fg="white", bg='black')
    liste_bonus_guerrier.place(x='10', y='765')

    rl = 875
    rule = Label(fiche, text='à faire', font=(
        "Gentium basic", 14, 'bold'), fg="white", bg='black')
    rule.place(x="10", y=rl)

    PA = Label(fiche, text=self.PA, font=(
        "Gentium basic", 14, 'bold'), fg="white", bg='black')
    PA.place(x='10', y=125)

    l = 162
    l_in=[]
    nb_b=[]
    for i in range(0, 8):
        inventaire = Label(fiche, text=f'-{self.inventaire[i]}', font=(
            "Gentium basic", 14, 'bold'), fg="white", bg='black')
        inventaire.place(x='10', y=l)
        l_in.append(inventaire)
        button_del_item= Button(fiche, text='X', bg='black', fg="white",command=lambda i=i:suppr_item(i))
        button_del_item.place(x='280', y=l)
        nb_b.append(button_del_item)
        l += 37
    def ad_PA():
        PA['text'] += 1

    def supp_PA():
        PA['text'] -= 1

    def ad_PV():
        PV['text'] += 1

    def supp_PV():
        PV['text'] -= 1

    def ad_E():
        E['text'] += 1

    def supp_E():
        E['text'] -= 1

    def ad_F():
        Force['text'] += 1

    def supp_F():
        Force['text'] -= 1

    def ad_D():
        Defense['text'] += 1

    def supp_D():
        Defense['text'] -= 1

    def ad_armure():
        armure['text'] = ajout_A.get()

    def suppr_armure():
        armure['text'] = ' '

    def ad_arme():
        arme['text'] = ajout_A.get()

    def suppr_arme():
        arme['text'] = ' '

    def ad_an():
        animal['text']=ajout_an.get()
    
    def suppr_an():
        animal['text']=' '

    def ad_item1():
        if len(l_in)<= 15:
            inventaire= Label(fiche, text=f'-{ajout_i.get()}', font=(
                "Gentium basic", 14, 'bold'), fg="white", bg='black')
            inventaire.place(x='10', y=37*(len(l_in))+162)
            l_in.append(inventaire)
            button_del_item= Button(fiche, text='X', bg='black', fg="white",command=lambda :suppr_item(i))
            button_del_item.place(x='280', y=37*(len(l_in))+125)
            nb_b.append(button_del_item)
    
    def suppr_item(i):
        l_in[i]['text']=' '
        del l_in[i]

    
    ajout_A = StringVar()
    enter_armure = Entry(fiche, textvariable=ajout_A)
    enter_armure.place(x='450', y='500')
    button_ad_armure = Button(
        fiche, text='+', bg='black', fg="white", command=ad_armure)
    button_ad_armure.place(x='553', y='450')
    button_del_arme = Button(fiche, text='X', bg='black',
                             fg="white", command=suppr_armure)
    button_del_arme.place(x='573', y='450')

    button_ad_arme = Button(fiche, text='+', bg='black',
                            fg="white", command=ad_arme)
    button_ad_arme.place(x='553', y='415')
    button_del_arme = Button(fiche, text='X', bg='black',
                             fg="white", command=suppr_arme)
    button_del_arme.place(x='573', y='415')

    button_up_PA = Button(fiche, text='▲', bg='black',
                          fg="white", command=ad_PA)
    button_up_PA.place(x='250', y='125')
    button_down_PA = Button(fiche, text='▼', bg='black',
                            fg="white", command=supp_PA)
    button_down_PA.place(x='270', y='125')

    button_up_PV = Button(fiche, text='▲', bg='black',
                          fg="white", command=ad_PV)
    button_up_PV.place(x='373', y='305')
    button_down_PV = Button(fiche, text='▼', bg='black',
                            fg="white", command=supp_PV)
    button_down_PV.place(x='393', y='305')

    button_up_E = Button(fiche, text='▲', bg='black',
                         fg="white", command=ad_E)
    button_up_E.place(x='553', y='305')
    button_down_E = Button(fiche, text='▼', bg='black',
                           fg="white", command=supp_E)
    button_down_E.place(x='573', y='305')

    button_up_F = Button(fiche, text='▲', bg='black', fg="white", command=ad_F)
    button_up_F.place(x='373', y='360')
    button_down_F = Button(fiche, text='▼', bg='black',
                           fg="white", command=supp_F)
    button_down_F.place(x='393', y='360')

    button_up_D = Button(fiche, text='▲', bg='black', fg="white", command=ad_D)
    button_up_D.place(x='553', y='360')
    button_down_D = Button(fiche, text='▼', bg='black',
                           fg="white", command=supp_D)
    button_down_D.place(x='573', y='360')

    ajout_i=StringVar()
    enter_item=Entry(fiche,textvariable=ajout_i)
    enter_item.place(x='170',y='700')
    button_ad_item = Button(fiche, text='+', bg='black', fg="white",command=ad_item1)
    button_ad_item.place(x='300', y='697')


    ajout_an=StringVar()
    enter_an=Entry(fiche,textvariable=ajout_an)
    enter_an.place(x='500',y='270')
    button_ad_an = Button(fiche, text='+', bg='black', fg="white",command=ad_an)
    button_ad_an.place(x='460', y='270')
    button_del_an = Button(fiche, text='X', bg='black', fg="white",command=suppr_an)
    button_del_an.place(x='480', y='270')

    fiche.mainloop()
# Penser a faire le systême de modification des mandats,finaliser le systeme de suppr 
# Revoir le style graphique de la fiche
