def liste_race():
    return ['Elfe', 'Humain', 'Nain', 'Gobelin']


def liste_classe():
    return ['Pyroguerrier', 'Amphibien', 'Archer', 'Barbare', 'Electroguerrier', 'Coeurdeglace', 'Assassin', 'Chevalier', 'Paladin', 'Necromancien']


def liste_villeE():

    return ['Comas', 'Flas', 'Crinesas', 'Arcos', 'Mistras', 'Horenas', 'Seris', 'Maris', 'Namis']


def liste_villeH():
    return ['Sanos', 'Vlorus', 'Hisotus', 'Port-Finoph', 'Iros', 'Pores', 'Gues', 'Nyares', 'Sones', 'Mones', 'Sures', 'Gres', 'Teres', 'Prisis', 'Conis', 'Netis']


def liste_villeN():
    return ['Morus', 'Tius', 'Dinerus', 'Ameteus', 'Lousseus', 'Roceus', 'Mires', 'Wires']


def liste_villeG():
    return ['Lavas', 'Gargas', 'Minetas', 'Solarus', 'Dorus', 'Crisus', 'Montrus', 'Magnus', 'Metus']


def liste_dieux():
    return {'Pyroguerrier': 'Fires', 'Amphibien': 'Oris', 'Archer': 'Varus', 'Barbare': 'Teros', 'Electroguerrier': 'Stores', 'Coeurdeglace': 'Gis', 'Assassin': 'Corcus', 'Chevalier': 'Dures', 'Paladin': 'Iros', 'Necromancien': 'Nemesis'}


def liste_metier():
    return ['Mineur', 'Forgeron', 'Cuisinier', 'Artisan', 'Marchand', 'Herboriste', 'Chasseur', 'Historien']


def liste_arme():
    return {'1': 'Epee courte', '2': 'Epee batarde', '3': 'Sabre', '4': 'Hache', '5': 'Labrys', '6': 'Dague', '7': 'Glaive', '8': 'Lance', '9': 'Hallbarde', '10': 'Javelot', '11': 'Arc', '12': 'Sceptre', '13': 'Gant'}


def liste_mat():
    return{'Pyroguerrier': 'Rubis', 'Amphibien': 'Aiguemarine', 'Archer': 'Jade', 'Barbare': 'Emmeraude', 'Electroguerrier': 'Or', 'Coeurdeglace': 'Lapislazuli', 'Assassin': 'Amethyste', 'Chevalier': 'Acier', 'Paladin': 'Fer', 'Necromancien': 'Onyx'
           }


def liste_bonus():
    return {'1': " Maitre d'arme", '2': 'Rage', '3': 'Corps a corps ', '4': 'Precision ', '5': 'Vitalite',
            '6': 'Agilite', '7': 'Vitesse ', '8': 'Sang-froid ', '9': 'Resistance au froid',
            '10': 'Resistance a la chaleur', '11': 'Defense', '12': 'Discretion', '13': 'Vision', '14': 'Esquive ', '15': 'Stratège'}


def liste_malus():
    return {'1': " Novice d'arme ", '2': 'Peur', '3': 'Lache', '4': 'Taupe', '5': 'Faible ',
            '6': 'Engourdie', '7': 'Lent', '8': 'Colère(+)', '9': 'Peur du noir',
            '10': "Peur des animaux", '11': 'Maigre', '12': 'Bruyant', '13': 'Myope', '14': 'Rigide ', '15': 'Idiot'}


def liste_bonus_guerrier():
    return {'Pyroguerrier': 'Attaque de Fires:+3F/3T', 'Amphibien': "Force aquatique:+2F/dans l'eau +4F", 'Archer': "Oeil d'hirondelle:C.C/2T", 'Barbare': 'Force Terosiene:Imparable/3T', 'Electroguerrier': 'Foudre rapide:Inniative/Esquive 3T',
            'Coeurdeglace': "Esprit de Gis:pas d'effet d'état", 'Assassin': 'Aile de Corcus:Invisible/3T', 'Chevalier': "Double lame:Peut utiliser deux armes", 'Paladin': 'Onde de vie:soigne (75%PV)', 'Necromancien': 'Diane des déchus:D6 squellete/3T'}


def liste_element():
    return{'Pyroguerrier': 'de Feu', "Amphibien": "d'Eau", 'Archer': 'du Vent', 'Barbare': 'de Terre', 'Electroguerrier': 'de Foudre', 'Coeurdeglace': 'de Glace', 'Assassin': 'de Poison', "Chevalier": "d'Acier", 'Paladin':
           'de la Lumiere', 'Necromancien': 'des Tenebres'}


def liste_competence_faible():
    return [f'Energie ', 'Colère ', 'Flèche ', 'Gloire aux', 'Protection', 'Soin ', 'Entrave']


def liste_competence_moyen():
    return ['Liens ', 'Tempete ', 'Ravage', ' ', 'Trio ', 'Lame', 'Terre de ', 'Soutient ', 'Parade', 'Barriere ', 'Frappe', 'Bouclier ', 'Fendoir ', 'Supplice', 'Souffle ', 'Voyage']


def liste_competence_puissant():
    return [f'Pluie', 'Executions de', 'Vague ', 'Tourbillon ', 'Vent de ', 'Creature de ', 'Montagne ', 'Onde ', 'Dévastation ', 'Prévenance ']


def liste_complement(self):
    return [self.classe, self.arme, self.dieux]

def liste_PA():
    return 50 

def liste_inventaire():
    return ['Couverture', 'Outre', 'Gamelle', 'Torche']


def liste_metier_livre():
    return {'Mineur': 'Livre des métaux', 'Forgeron': 'Livre de métallurgie', 'Cuisinier': 'Livre de recette', 'Artisan': "Livre d'artisanat", 'Marchand': 'Livre des Valeurs', 'Herboriste': 'Livre de la flore',
            'Chasseur': 'Livre de la faune', 'Historien': "Livre d'histoire"}


def liste_metier_objet():
    return {'Mineur': 'Pioche', 'Forgeron': 'Fer', 'Cuisinier': 'Pains', 'Artisan': "Corde", 'Marchand': 'Parchemin des Marchands', 'Herboriste': 'Fiole', 'Chasseur': 'Dague en Fer(3F)', 'Historien': "Parchemin"}


def liste_classe_objet():
    return {'Pyroguerrier': 'Huile de feu', 'Amphibien': 'Potion de vie', 'Archer': 'Fleche explosife', 'Barbare': 'Alcool fort', 'Electroguerrier': 'Chaine de fer',
            'Coeurdeglace': 'Plaque de glace', 'Assassin': 'Piege empoisonne', 'Chevalier': 'Selle de chevale', 'Paladin': "Psaume d'Iros", 'Necromancien': 'Os de loup'}

"""l=162
    for i in range(0,8):
        inventaire = Label(fiche, text=f'-{self.inventaire[i]}', font=(
            "Gentium basic", 14, 'bold'), fg="white", bg='black')
        inventaire.place(x='10',y=l)
        l+=37"""