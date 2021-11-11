def liste_race():
    return ['Elfe','Humain','Nain','Gobelin']

def liste_classe():
    return ['Pyroguerrier','Amphibien','Archer','Barbare','Electroguerrier','Coeurdeglace','Assassin','Chevalier','Paladin','Necromancien']

def liste_villeE():

    return ['Comas','Flas','Crinesas','Arcos','Mistras','Horenas','Seris','Maris','Namis']

def liste_villeH():
    return ['Sanos','Vlorus','Hisotus','Port-Finoph','Iros','Pores','Gues','Nyares','Sones','Mones','Sures','Gres','Teres','Prisis','Conis','Netis']
def liste_villeN():
    return ['Morus','Tius','Dinerus','Ameteus','Lousseus','Roceus','Mires','Wires']

def liste_villeG():
    return ['Lavas','Gargas','Minetas','Solarus','Dorus','Crisus','Montrus','Magnus','Metus']

def liste_dieux():
    return {'Pyroguerrier':'Fires','Amphibien':'Oris','Archer':'Varus','Barbare':'Teros','Electroguerrier':'Stores','Coeurdeglace':'Gis','Assassin':'Corcus','Chevalier':'Dures','Paladin':'Iros','Necromancien':'Nemesis'}

def liste_metier():
    return ['Mineur','Cuisinier','Marchand','Herboriste','Chasseur','Historien']

def liste_arme():
    return {'1':'Epee courte','2':'Epee batarde','3':'Sabre','4':'Hache d arme','5':'Hache de guerre','6':'Dague','7':'Glaive','8':'Lance','9':'Hallbarde','10':'Javelot','11':'Arc','12':'Sceptre','13':'Gant de combat'}


def liste_mat():
    return{'Pyroguerrier':'Rubis','Amphibien':'Aiguemarine','Archer':'Jade','Barbare':'Emmeraude','Electroguerrier':'Or','Coeurdeglace':'Lapislazuli','Assassin':'Amethyste','Chevalier':'Acier','Paladin':'Fer','Necromancien':'Onyx'
    }

def liste_bonus():
    return {'1':" Maitre d'arme +10F pour le maniement de votre arme principale",'2':'Rage +10F quand le  joueur est blesse','3':'Corps a corps +10F au corps à corps','4':'Precision +1 de préscision','5':'Vitalite +20pv',
    '6':'Agilite +1 en agilite','7':'Vitesse +1 de vitesse','8':'Sang-froid permet de ne pas avoir Colère ou Panique','9':'Resistance au froid pas de malus dans les zones froides',
    '10':'Resistance a la chaleur pas de malus dans les zones  chaudes','11':'Defense +20D','12':'Discretion +1 en discretion','13':'Vision +1 en vision','14':'Esquive +1 en esquive','15':'Stratège +1 en stratégie'}

def liste_malus():
    return {'1':" Novice d'arme -10F pour le maniement d'une nouvelle arme ",'2':'Peur -10F quand le  joueur est blesse','3':'Lache -10F au corps à corps','4':'Taupe -1 de préscision','5':'Faible -20pv',
    '6':'Engourdie -1 en agilite','7':'Lent +1 de vitesse','8':'Colère(+) +20F(40F)/-20D(-40D)/1sur3(2sur3)de toucher un allié','9':'Peur du noir -2 au jet de dés dans le noir',
    '10':"Peur des animaux -2 au jet de dés contre les animaux/pas d'intéractions",'11':'Maigre -20D','12':'Bruyant -1 en discretion','13':'Myope -1 en vision','14':'Rigide -1 en esquive','15':'Idiot -1 en stratégie'}

def liste_bonus_guerrier():
    return {'Pyroguerrier':'+30F/3T','Amphibien':"20F/dans l'eau +40",'Archer':'coup critique pour les attaques a distance 2T','Barbare':'imparable au corps à corps 3T','Electroguerrier':'Inniative/Esquive 3T',
    'Coeurdeglace':"ne subit aucun effet d'état",'Assassin':'Invisible 3T','Chevalier':"peut utiliser deux armes",'Paladin':'ressucite ou soigne les alliés 75','Necromancien':'invoque d6 squellete 3T'}

def liste_element():
    return{'Pyroguerrier':'de Feu',"Amphibien":"d'Eau",'Archer':'du Vent','Barbare':'de Terre','Electroguerrier':'de Foudre','Coeurdeglace':'de Glace','Assassin':'de Poison',"Chevalier":"d'Acier",'Paladin':
    'de la Lumiere','Necromancien':'des Tenebres'}

def liste_competence_faible():
    return [f'Energie elementaire','Element enrage','Flèche ','Gloire du','Element protecteur','Element psychique','soin ','Element tournoyant']

def liste_competence_moyen():
    return ['Liens elementaire','Tempete elementaire','Element meutrier',' elementaire','Trio elementaire','Element de vie','Element tueur','Lame elementaire','Terre de','Element solide','Parade'
    ,'Barriere elementaire','Pique elementaire','Bouclier elementaire','Element coupant','Element mortelle','Souffle elementaire']

def liste_competence_puissant():
    return [f'Pluie elementaire','Executions de','Vague elementaire','Tourbillon elementaire','Vent elementaire','Creature de ','Montagne elementaire','Chaine elementaire','Onde elementaire'
    ,'Ouragan elementaire']

def liste_complement(self):
    return [self.classe,self.arme,self.dieux]

def liste_inventaire():
    return ['50 PO','Couverture','Outre','Gamelle','Torche']

def liste_metier_objet():
    return {'Mineur':'Pioche,Livre des métaux','Cuisinier':'3 Pains,Livre de recette','Marchand':'Parchemin des Marchands,Livre des Valeurs','Herboriste':'3 Fiole,Livre de la flore et de chimie',
    'Chasseur':'Dague en Fer(30F),Livre de la faune','Historien':"3 Parchemin,Livre d'histoire"}

def liste_classe_objet():
    return {'Pyroguerrier':'3 Huile de feu','Amphibien':'2 Potion de vie','Archer':'3 Fleche explosife','Barbare':'3 Alcool fort','Electroguerrier':'3 Chaine de fer',
    'Coeurdeglace':'3 Plaque de glace','Assassin':'2 Piege empoisonne','Chevalier':'Selle de chevale','Paladin':"Psaume d'Iros",'Necromancien':'3 Os de loup'}
