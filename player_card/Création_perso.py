import random
import all_liste
import fiche
from tkinter import*


class Crea_Perso:
    def __init__(self, nom):
        self.nom = nom

    def race(self):
        all_liste.liste_race()
        print("Choisissez votre race:")
        print(all_liste.liste_race())
        self.race = str(input())
        while self.race not in all_liste.liste_race():
            print("Le choix demander n'est pas dans la liste.Choisisez parmis la liste")
            self.race = str(input())
        return self.race

    def classe(self):
        all_liste.liste_classe()
        if self.race == 'Elfe':
            lclasse = ['Pyroguerrier', 'Amphibien', 'Archer', 'Necromancien']
            print("Choisissez votre classe:")
            print(lclasse)
            self.classe = str(input())
            while self.classe not in lclasse:
                print(
                    "Le choix demander n'est pas dans la liste.Choisisez parmis la liste")
                self.classe = str(input())
        if self.race == 'Humain':
            lclasse = ['Pyroguerrier', 'Coeurdeglace',
                       'Assassin', 'Paladin', 'Necromancien']
            print("Choisissez votre classe:")
            print(lclasse)
            self.classe = str(input())
            while self.classe not in lclasse:
                print(
                    "Le choix demander n'est pas dans la liste.Choisisez parmis la liste")
                self.classe = str(input())
        if self.race == 'Nain':
            lclasse = ['Electroguerrier', 'Chevalier', 'Necromancien']
            print("Choisissez votre classe:")
            print(lclasse)
            self.classe = str(input())
            while self.classe not in lclasse:
                print(
                    "Le choix demander n'est pas dans la liste.Choisisez parmis la liste")
                self.classe = str(input())
        if self.race == 'Gobelin':
            lclasse = ['Barbare', 'Assassin', 'Necromancien']
            print("Choisissez votre classe:")
            print(lclasse)
            self.classe = str(input())
            while self.classe not in lclasse:
                print(
                    "Le choix demander n'est pas dans la liste.Choisisez parmis la liste")
                self.classe = str(input())

        print(f'Vous avez choisis {self.classe}')
        return self.classe

    def ville(self):
        lville_use = []
        if self.race == 'Elfe':
            print(f'Choisissez une ville Elfique:')
        else:
            print(f'Choisissez une ville {self.race}e:')

        if self.race == 'Elfe':
            if self.classe == 'Archer':
                for i in range(3):
                    lville_use.append(all_liste.liste_villeE()[i+3])

                print(lville_use)
                self.ville = str(input())
                while self.ville not in lville_use:
                    print(
                        "Le choix demander n'est pas dans la liste.Choisisez parmis la liste")
                    self.ville = str(input())

            elif self.classe == 'Amphibien':
                for i in range(3):
                    lville_use.append(all_liste.liste_villeE()[i])

                print(lville_use)
                self.ville = str(input())
                while self.ville not in lville_use:
                    print(
                        "Le choix demander n'est pas dans la liste.Choisisez parmis la liste")
                    self.ville = str(input())

            elif self.classe == 'Pyroguerrier':
                for i in range(3):
                    lville_use.append(all_liste.liste_villeE()[i+6])
                print(lville_use)
                self.ville = str(input())
                while self.ville not in lville_use:
                    print(
                        "Le choix demander n'est pas dans la liste.Choisisez parmis la liste")
                    self.ville = str(input())
            else:
                print(all_liste.liste_villeE())
                self.ville = str(input())
                while self.ville not in all_liste.liste_villeE():
                    print(
                        "Le choix demander n'est pas dans la liste.Choisisez parmis la liste")
                    self.ville = str(input())

        elif self.race == 'Humain':
            if self.classe == 'Paladin':
                for i in range(5):
                    lville_use.append(all_liste.liste_villeH()[i])

                print(lville_use)
                self.ville = str(input())
                while self.ville not in lville_use:
                    print(
                        "Le choix demander n'est pas dans la liste.Choisisez parmis la liste")
                    self.ville = str(input())

            elif self.classe == 'Pyroguerrier':
                for i in range(6):
                    lville_use.append(all_liste.liste_villeH()[i+5])

                print(lville_use)
                self.ville = str(input())
                while self.ville not in lville_use:
                    print(
                        "Le choix demander n'est pas dans la liste.Choisisez parmis la liste")
                    self.ville = str(input())

            elif self.classe == 'Assassin':
                for i in range(2):
                    lville_use.append(all_liste.liste_villeH()[i+11])
                print(lville_use)
                self.ville = str(input())
                while self.ville not in lville_use:
                    print(
                        "Le choix demander n'est pas dans la liste.Choisisez parmis la liste")
                    self.ville = str(input())
            elif self.classe == 'Coeurdeglace':
                for i in range(3):
                    lville_use.append(all_liste.liste_villeH()[i+13])
                print(lville_use)
                self.ville = str(input())
                while self.ville not in lville_use:
                    print(
                        "Le choix demander n'est pas dans la liste.Choisisez parmis la liste")
                    self.ville = str(input())
            else:
                print(all_liste.liste_villeH())
                self.ville = str(input())
                while self.ville not in all_liste.liste_villeH():
                    print(
                        "Le choix demander n'est pas dans la liste.Choisisez parmis la liste")
                    self.ville = str(input())

        elif self.race == 'Nain':
            if self.classe == 'Chevalier':
                for i in range(6):
                    lville_use.append(all_liste.liste_villeN()[i])
                print(lville_use)
                self.ville = str(input())
                while self.ville not in lville_use:
                    print(
                        "Le choix demander n'est pas dans la liste.Choisisez parmis la liste")
                    self.ville = str(input())
            elif self.classe == 'Electroguerrier':
                for i in range(2):
                    lville_use.append(all_liste.liste_villeN()[i+6])
                print(lville_use)
                self.ville = str(input())
                while self.ville not in lville_use:
                    print(
                        "Le choix demander n'est pas dans la liste.Choisisez parmis la liste")
                    self.ville = str(input())
            else:
                print(all_liste.liste_villeN())
                self.ville = str(input())
                while self.ville not in all_liste.liste_villeN:
                    print(
                        "Le choix demander n'est pas dans la liste.Choisisez parmis la liste")
                    self.ville = str(input())

        elif self.race == 'Gobelin':
            if self.classe == 'Assassin':
                for i in range(3):
                    lville_use.append(all_liste.liste_villeG()[i])
                print(lville_use)
                self.ville = str(input())
                while self.ville not in lville_use:
                    print(
                        "Le choix demander n'est pas dans la liste.Choisisez parmis la liste")
                    self.ville = str(input())
            else:
                print(all_liste.liste_villeG())
                self.ville = str(input())
                while self.ville not in all_liste.liste_villeG():
                    print(
                        "Le choix demander n'est pas dans la liste.Choisisez parmis la liste")
                    self.ville = str(input())

        print(f'Vous avez choisis un(e){self.race} de {self.ville}')
        return self.ville

    def dieux(self):
        self.dieux = all_liste.liste_dieux()[self.classe]
        print(f'Vous êtes un guerrier vénérant {self.dieux}')

    def metier(self):
        print(all_liste.liste_metier())
        print("Choisissez votre metier:")
        self.metier = str(input())

        while self.metier not in all_liste.liste_metier():
            print("Le choix demander n'est pas dans la liste.Choisisez parmis la liste")
            self.metier = str(input())

        print(f'Vous avez choisis {self.metier}')
        return self.metier

    def PV(self):
        self.pv = random.randrange(10, 20, 1)
        print(f'{self.nom} à {self.pv} PV')
        return self.pv

    def E(self):
        self.e = random.randint(1, 4)
        print(f'{self.nom} à {self.e} E')
        return self.e

    def Force(self):
        self.F = random.randrange(1, 10, 1)
        print(f'{self.nom} à {self.F} de Force')
        return self.F

    def Defense(self):
        self.D = 0
        print(f'{self.nom} à {self.D} de Défense')
        return self.D

    def Arme(self):
        larme_use = []
        if self.race == 'Humain':
            larme_use.append(all_liste.liste_arme()['1'])
            larme_use.append(all_liste.liste_arme()['12'])
            if self.classe == 'Paladin':
                larme_use.append(all_liste.liste_arme()['9'])
            if self.classe == 'Pyroguerrier':
                larme_use.append(all_liste.liste_arme()['7'])
            if self.classe == 'Assassin':
                larme_use.append(all_liste.liste_arme()['6'])
            if self.classe == 'Coeurdeglace':
                larme_use.append(all_liste.liste_arme()['8'])
            print('Quel arme voulez-vous choisire ?:')
            print(larme_use)
            self.arme = str(input())
            if self.arme not in larme_use:
                print(
                    "Le choix demander n'est pas dans la liste.Choisisez parmis la liste")
                self.arme = str(input())

        elif self.race == 'Elfe':
            larme_use.append(all_liste.liste_arme()['1'])
            larme_use.append(all_liste.liste_arme()['12'])
            if self.classe == 'Archer':
                self.arme = all_liste.liste_arme()['11']
                print("En tant que Archer, vous ne pouvez utilisez que l'arc")
                return self.arme
            if self.classe == 'Pyroguerrier':
                larme_use.append(all_liste.liste_arme()['13'])
            if self.classe == 'Amphibien':
                self.arme = all_liste.liste_arme()['13']
            print('Quel arme voulez-vous choisire ?:')
            print(larme_use)
            self.arme = str(input())
            if self.arme not in larme_use:
                print(
                    "Le choix demander n'est pas dans la liste.Choisisez parmis la liste")
                self.arme = str(input())

        elif self.race == 'Nain':
            larme_use.append(all_liste.liste_arme()['1'])
            larme_use.append(all_liste.liste_arme()['12'])
            if self.classe == 'Electroguerrier':
                larme_use.append(all_liste.liste_arme()['3'])
                larme_use.append(all_liste.liste_arme()['13'])
            if self.classe == 'Chevalier':
                larme_use.append(all_liste.liste_arme()['2'])
                larme_use.append(all_liste.liste_arme()['6'])
            print('Quel arme voulez-vous choisire ?:')
            print(larme_use)
            self.arme = str(input())
            if self.arme not in larme_use:
                print(
                    "Le choix demander n'est pas dans la liste.Choisisez parmis la liste")
                self.arme = str(input())

        elif self.race == 'Gobelin':
            larme_use.append(all_liste.liste_arme()['1'])
            larme_use.append(all_liste.liste_arme()['12'])
            if self.classe == 'Barbare':
                larme_use.append(all_liste.liste_arme()['4'])
                larme_use.append(all_liste.liste_arme()['5'])
                larme_use.append(all_liste.liste_arme()['13'])
            if self.classe == 'Assassin':
                larme_use.append(all_liste.liste_arme()['10'])
                larme_use.append(all_liste.liste_arme()['6'])
            print('Quel arme voulez-vous choisire ?:')
            print(larme_use)
            self.arme = str(input())
            if self.arme not in larme_use:
                print(
                    "Le choix demander n'est pas dans la liste.Choisisez parmis la liste")
                self.arme = str(input())
        return self.arme

    def arme_force(self):
        if self.arme == 'Epee batarde' or self.arme == 'Hache de guerre' or self.arme == 'Hallbarde':
            self.arme_force = random.randrange(1, 4, 1)
        elif self.arme == 'Sceptre':
            self.arme_force = 0
        else:
            self.arme_force = random.randrange(1, 6, 1)

        return self.arme_force

    def arme_mat(self):
        self.arme_mat = all_liste.liste_mat()[self.classe]
        return self.arme_mat

    def arme_mat_dmg(self):
        if self.arme_mat == 'Diamant' or 'Acier':
            self.arme_mat_dmg = random.randrange(1, 20, 1)
        elif self.arme_mat == 'Fer' or 'Onyx':
            self.arme_mat_dmg = random.randrange(1, 12, 1)
        else:
            self.arme_mat_dmg = random.randrange(1, 10, 1)

        return self.arme_mat_dmg

    def arme_totale(self):
        arme_t = []
        arme_t.append(self.arme_mat_dmg)
        arme_t.append(self.arme_force)
        if arme_t[0] < arme_t[1]:
            self.arme_totale = 10
        else:
            self.arme_totale = arme_t[0]-arme_t[1]

        print(
            f'Votre {self.arme} de {self.arme_mat} à une puissance de {self.arme_totale} de Force')
        return self.arme_totale

    def bonus(self):
        all_liste.liste_bonus()
        print('Voici vos 3 Bonus:')
        r = random.randint(1, 15)
        self.bonus1 = all_liste.liste_bonus()[f'{r}']
        print(f'-{self.bonus1}')
        r = random.randint(1, 15)
        self.bonus2 = all_liste.liste_bonus()[f'{r}']
        print(f'-{self.bonus2}')
        r = random.randint(1, 15)
        self.bonus3 = all_liste.liste_bonus()[f'{r}']
        print(f'-{self.bonus3}')
        return self.bonus

    def malus(self):
        all_liste.liste_malus()
        print('Voici vos 3 Malus:')
        r = random.randint(1, 15)
        self.malus1 = all_liste.liste_malus()[f'{r}']
        print(f'-{self.malus1}')
        r = random.randint(1, 15)
        self.malus2 = all_liste.liste_malus()[f'{r}']
        print(f'-{self.malus2}')
        r = random.randint(1, 15)
        self.malus3 = all_liste.liste_malus()[f'{r}']
        print(f'-{self.malus3}')
        return self.malus

    def liste_bonus_guerrier(self):
        all_liste.liste_bonus_guerrier()
        self.liste_bonus_guerrier = all_liste.liste_bonus_guerrier()[
            self.classe]
        print(
            f'Votre compétence unique de {self.classe} est {self.liste_bonus_guerrier}')
        return self.liste_bonus_guerrier

    def competencef(self):
        all_liste.liste_element()
        all_liste.liste_competence_faible()
        all_liste.liste_complement(self)

        comp_r_f = random.randint(0, 6)
        print('Voici votre 3 compétences:')

        if comp_r_f == 3:
            print(
                f'-{all_liste.liste_competence_faible()[comp_r_f]} {all_liste.liste_complement(self)[0]} ')
        else:
            print(
                f'-{all_liste.liste_competence_faible()[comp_r_f]} {all_liste.liste_element()[self.classe]}')
        self.competencef = f'-{all_liste.liste_competence_faible()[comp_r_f]} {all_liste.liste_element()[self.classe]}'
        return self.competencef

    def competencem(self):
        all_liste.liste_competence_moyen()
        all_liste.liste_element()
        all_liste.liste_complement(self)
        comp_r_m = random.randint(0, 15)

        if comp_r_m == 3:
            print(
                f'-{all_liste.liste_complement(self)[1]} {all_liste.liste_element()[self.classe]} ')
        elif comp_r_m == 7:
            print(
                f'-{all_liste.liste_competence_moyen()[comp_r_m]} {all_liste.liste_complement(self)[2]} ')

        else:
            print(
                f'-{all_liste.liste_competence_moyen()[comp_r_m]} {all_liste.liste_element()[self.classe]}')
        self.competencem = f'-{all_liste.liste_competence_moyen()[comp_r_m]} {all_liste.liste_element()[self.classe]}'
        return self.competencem

    def competencep(self):
        all_liste.liste_competence_puissant()
        all_liste.liste_element()
        all_liste.liste_complement(self)
        comp_r_p = random.randint(0, 9)
        if comp_r_p == 1 or comp_r_p == 5 or comp_r_p == 4 or comp_r_p == 9:
            print(
                f'-{all_liste.liste_competence_puissant()[comp_r_p]} {all_liste.liste_complement(self)[2]} ')
        else:
            print(
                f'-{all_liste.liste_competence_puissant()[comp_r_p]} {all_liste.liste_element()[self.classe]}')
        self.competencep = f'-{all_liste.liste_competence_puissant()[comp_r_p]} {all_liste.liste_element()[self.classe]}'
        return self.competencep

    def inventaire(self):
        all_liste.liste_inventaire()
        all_liste.liste_metier_objet()
        all_liste.liste_classe_objet()
        self.inventaire = all_liste.liste_inventaire()
        self.inventaire.append(self.arme)
        self.inventaire.append(all_liste.liste_metier_objet()[self.metier])
        self.inventaire.append(all_liste.liste_classe_objet()[self.classe])
        print('Voici votre inventaire:')
        print(self.inventaire)
        return self.inventaire

    def affichage(self):
        fiche.crea_fiche(self)
        return self.affichage


def perso():
    print('Choisisez votre prénom:')
    nom = Crea_Perso(str(input()))
    nom.race()
    nom.classe()
    nom.ville()
    nom.dieux()
    nom.metier()
    nom.PV()
    nom.E()
    nom.Force()
    nom.Defense()
    nom.Arme()
    nom.arme_force()
    nom.arme_mat()
    nom.arme_mat_dmg()
    nom.arme_totale()
    nom.bonus()
    nom.malus()
    nom.liste_bonus_guerrier()
    nom.competencef()
    nom.competencem()
    nom.competencep()
    nom.inventaire()
    nom.affichage()


perso()
