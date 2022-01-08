from tkinter import*
from tkinter.font import BOLD


def crea_fiche(self):
    fiche = Tk()
    fiche.geometry('600x1000')
    fiche.title('test')
    fiche['bg'] = 'white'
    fiche.resizable(height=False, width=False)

    bgp = PhotoImage(file='f.png')
    img = Label(fiche, image=bgp)
    img.pack()

    nom = Label(fiche, text=f'{self.nom}', font=(
        "Gentium basic", 30, 'bold'), fg="white", bg='black')
    nom.place(x='25', y='25')

    classe = Label(fiche, text=f'{self.classe}', font=(
        "Gentium basic", 15, 'bold'), fg="white", bg='black')
    classe.place(x='400', y='10')

    ville = Label(fiche, text=f'{self.ville}', font=(
        "Gentium basic", 15, 'bold'), fg="white", bg='black')
    ville.place(x='400', y='60')

    race = Label(fiche, text=f'{self.race}', font=(
        "Gentium basic", 25, 'bold'), fg="white", bg='black')
    race.place(x='315', y='125')

    dieux = Label(fiche, text=f'{self.dieux}', font=(
        "Gentium basic", 25, 'bold'), fg="white", bg='black')
    dieux.place(x='475', y='125')

    metier = Label(fiche, text=f'{self.metier}', font=(
        "Gentium basic", 25, 'bold'), fg="white", bg='black')
    metier.place(x='305', y='225')

    PV = Label(fiche, text=f'{self.pv}', font=(
        "Gentium basic", 20, 'bold'), fg="white", bg='black')
    PV.place(x='315', y='305')

    E = Label(fiche, text=f'{self.e}', font=(
        "Gentium basic", 20, 'bold'), fg="white", bg='black')
    E.place(x='550', y='305')

    Force = Label(fiche, text=f'{self.F}', font=(
        "Gentium basic", 20, 'bold'), fg="white", bg='black')
    Force.place(x='315', y='355')

    Defense = Label(fiche, text=f'{self.D}', font=(
        "Gentium basic", 20, 'bold'), fg="white", bg='black')
    Defense.place(x='550', y='355')

    arme = Label(fiche, text=f'{self.arme} en {self.arme_mat}(+{self.arme_totale})',
                 font=("Gentium basic", 15, 'bold'), fg="white", bg='black')
    arme.place(x='315', y='415')

    armure = Label(fiche, text=' ', font=(
        "Gentium basic", 15, 'bold'), fg="white", bg='black')
    armure.place(x='315', y='450')

    bonus1 = Label(fiche, text=f'{self.bonus1}', font=(
        "Gentium basic", 10, 'bold'), fg="white", bg='black')
    bonus1.place(x='315', y='525')
    bonus2 = Label(fiche, text=f'{self.bonus2}', font=(
        "Gentium basic", 10, 'bold'), fg="white", bg='black')
    bonus2.place(x='315', y='590')
    bonus3 = Label(fiche, text=f'{self.bonus3}', font=(
        "Gentium basic", 10, 'bold'), fg="white", bg='black')
    bonus3.place(x='315', y='655')

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
    comp_r_f.place(x='315', y='740')
    df = Label(fiche, text="D4", font=(
        "Gentium basic", 20, 'bold'), fg="white", bg='black')
    df.place(x='470', y='730')
    d1 = Label(fiche, text="10", font=(
        "Gentium basic", 20, 'bold'), fg="white", bg='black')
    d1.place(x='545', y='730')

    comp_r_f = Label(fiche, text=f'{self.competencem}', font=(
        "Gentium basic", 10, 'bold'), fg="white", bg='black')
    comp_r_f.place(x='315', y='840')
    dm = Label(fiche, text="D6", font=(
        "Gentium basic", 20, 'bold'), fg="white", bg='black')
    dm.place(x='470', y='830')
    d2 = Label(fiche, text="13", font=(
        "Gentium basic", 20, 'bold'), fg="white", bg='black')
    d2.place(x='545', y='830')

    comp_r_p = Label(fiche, text=f'{self.competencep}', font=(
        "Gentium basic", 10, 'bold'), fg="white", bg='black')
    comp_r_p.place(x='315', y='940')
    dp = Label(fiche, text="D10", font=(
        "Gentium basic", 20, 'bold'), fg="white", bg='black')
    dp.place(x='470', y='930')
    d3 = Label(fiche, text="15", font=(
        "Gentium basic", 20, 'bold'), fg="white", bg='black')
    d3.place(x='545', y='930')

    liste_bonus_guerrier = Label(fiche, text=f'{self.liste_bonus_guerrier}', font=(
        "Gentium basic", 15, 'bold'), fg="white", bg='black')
    liste_bonus_guerrier.place(x='25', y='765')

    fiche.mainloop()
