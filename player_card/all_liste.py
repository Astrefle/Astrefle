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
    return ['Mineur', 'Cuisinier', 'Marchand', 'Herboriste', 'Chasseur', 'Historien']


def liste_arme():
    return {'1': 'Epee courte', '2': 'Epee batarde', '3': 'Sabre', '4': 'Hache d arme', '5': 'Hache de guerre', '6': 'Dague', '7': 'Glaive', '8': 'Lance', '9': 'Hallbarde', '10': 'Javelot', '11': 'Arc', '12': 'Sceptre', '13': 'Gant de combat'}


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
            '10': "Peur des animaux", '11': 'Maigre -2D', '12': 'Bruyant', '13': 'Myope', '14': 'Rigide ', '15': 'Idiot'}


def liste_bonus_guerrier():
    return {'Pyroguerrier': '+3F/3T', 'Amphibien': "+2F/dans l'eau +4F", 'Archer': 'C.C pour les attaques à distances/2T', 'Barbare': 'Imparable/3T', 'Electroguerrier': 'Inniative/Esquive 3T',
            'Coeurdeglace': "ne subit aucun effet d'état", 'Assassin': 'Invisible/3T', 'Chevalier': "Peut utiliser deux armes", 'Paladin': 'soigne (75%PV)', 'Necromancien': 'D6 squellete/3T'}


def liste_element():
    return{'Pyroguerrier': 'de Feu', "Amphibien": "d'Eau", 'Archer': 'du/de Vent', 'Barbare': 'de Terre', 'Electroguerrier': 'de Foudre', 'Coeurdeglace': 'de Glace', 'Assassin': 'de Poison', "Chevalier": "d'Acier", 'Paladin':
           'de la Lumiere', 'Necromancien': 'des Tenebres'}


def liste_competence_faible():
    return [f'Energie ', 'Colère ', 'Flèche ', 'Gloire aux', 'Protection', 'Soin ', 'Entrave']


def liste_competence_moyen():
    return ['Liens ', 'Tempete elementaire', 'Ravage', ' ', 'Trio ', 'Lame', 'Terre de ', 'Soutient ', 'Parade', 'Barriere ', 'Frappe', 'Bouclier ', 'Fendoir ', 'Supplice', 'Souffle ', 'Voyage']


def liste_competence_puissant():
    return [f'Pluie elementaire', 'Executions de', 'Vague ', 'Tourbillon elementaire', 'Vent de ', 'Creature de ', 'Montagne ', 'Onde ', 'Dévastation ', 'Prévenance ']


def liste_complement(self):
    return [self.classe, self.arme, self.dieux]


def liste_inventaire():
    return ['50 PO', 'Couverture', 'Outre', 'Gamelle', 'Torche']


def liste_metier_objet():
    return {'Mineur': 'Pioche,Livre des métaux', 'Cuisinier': '3 Pains,Livre de recette', 'Marchand': 'Parchemin des Marchands,Livre des Valeurs', 'Herboriste': '3 Fiole,Livre de la flore et de chimie',
            'Chasseur': 'Dague en Fer(3F),Livre de la faune', 'Historien': "3 Parchemin,Livre d'histoire"}


def liste_classe_objet():
    return {'Pyroguerrier': '3 Huile de feu', 'Amphibien': '2 Potion de vie', 'Archer': '3 Fleche explosife', 'Barbare': '3 Alcool fort', 'Electroguerrier': '3 Chaine de fer',
            'Coeurdeglace': '3 Plaque de glace', 'Assassin': '2 Piege empoisonne', 'Chevalier': 'Selle de chevale', 'Paladin': "Psaume d'Iros", 'Necromancien': '3 Os de loup'}
