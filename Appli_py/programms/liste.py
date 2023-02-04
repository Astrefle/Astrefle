import random


def liste_m():
    liste_m = ['envahir un village', 'envahir un port', 'envahir une ville', 'envahir une principaute', 'envahir un pays', 'defendre un village', 'defendre un port', 'defendre une ville', 'defendre une principaute', 'defendre un pays',
               'faire chuter une capitale directement ou non']
    return liste_m[random.randint(0, 10)]


def liste_p():
    liste_p = ['fonder une aliance comerciale', 'fonder une aliance millitaire', 'trahiser une aliance comerciale', 'trahiser une aliance millitaire', 'stabiliser son commerce pendant trois tours',
               'donner des ressources', 'donner des troupes', 'donner du territoire', 'imposer une taxe de ressource', 'utiliser toute vos actions monarches', 'participer a trois entretiens diplomatique']
    return liste_p[random.randint(0, 10)]


def liste_r():
    liste_r = ['la couronne de caerex', 'la lame vorpalin', 'le parchemin des seigneurs', "le sable d'har", "l'orbe en zultanite", "l'arctanfaet", 'la hache de blot',
               'la botte de vidar', "l'eau du thyn", 'la pierre de thi', 'la statue de kaiti', 'la pomme de jouvence', 'la lance de wilhelm', 'le blason de harald']
    return (f'recuperer {liste_r[random.randint(0, 12)]}')


def slr():
    liste_slr = ['la couronne de caerex', 'la lame vorpalin', 'le parchemin des seigneurs', "le sable d'har", "l'orbe en zultanite", "l'artafaeat", 'la hache de blot',
                 'la botte de vidar', "l'eau du thyn", 'la pierre de thi', 'la statue de kaiti', 'la pomme de jouvence', 'la lance de wilhelm', 'le blason de harald']
    return liste_slr


def liste_all():
    liste_al = []
    for i in range(3):
        l_s = [liste_m(), liste_p(), liste_r()]
        liste_al.append(l_s[i])
    return liste_al


def liste_event():
    l = slr()
    al_a = 14
    l_e = []
    while al_a != 0:
        r = random.randint(0, len(l)-1)
        l_e.append(l[r])
        l.remove(l[r])
        al_a -= 1

    l_event = {1: ["bandit a combatre", "perdu dans les bois", f"decouverte de {l_e[0]}", "rencontre de bucheron"], 2: ["piege de chasseur", f"decouverte de {l_e[1]}", "rencontre de pecheurs", "perdu dans les bois"], 3: [f"decouverte de {l_e[2]}", "attaque de bandit", "chute de pierres", "rencontre de mineurs"], 4: ["perdus dans la jungle", "attaque de crocodiles", f"trouvaille de {l_e[3]}", "rencontre avec des nomades"], 5: ["tempete de sable", "serpent tricephale geant", "troupeau de chamaux", f"decouverte de {l_e[4]}"],
               6: [f'decouverte de {l_e[5]}', "ralentit par le terrain", "attaque de crocodiles", "pasage de marchand"], 7: ["chute de pieres", f"decouverte de {l_e[6]}", "attaque d'un troll geant", "aparition d'un brouillard epais"], 8: ["rencontre d'un dragon", f"decouverte de {l_e[7]}", "minerais gele", "rencontre de chasseurs de phoque"], 9: ["famille de sangliers", "groupe de bucherons", "perdus dans les bois", f"decouverte de {l_e[8]}"], 10: [f"decouverte de {l_e[9]}", "arbre a la seve riche", "antre de rama", "perdus dans les bois"],
               11: ["golem enterrer", "gisement de minerais", "bandits du nord", f"decouverte de {l_e[10]}"], 12: ["troupau de chevaux", "rencontre de marchands ambulants", "mercenaire a la recherche d emploi", f"coffre enterer avec {l_e[11]}"], 13: ["rencontre d'un serpent geant", "rencontre de pecheurs", f"coffre flotant avec {l_e[12]}", "courant fort"], 14: ["groupe de paysans", "ours enerve", f"{l_e[13]} deterrer", "perdus dans les bois"]}
    return l_event


def liste_unite():
    l_unite = {1: ["chevalier de l ieuse ,"], 2: ["soldat de sylv"], 3: ["bandit d alma"], 4: ["janissaire de razam"], 5: ["berserker de nors"], 6: ["enchanteur de mana"], 7: ["milice de harald"]}
    return l_unite


def liste_ud():
    l_ud = {1: ["vos jets d attaque ont un bonus de 1 ,"], 2: ["Vous pouvez avoir une unite en plus de votre limite,"], 3: ["Vos jets d'attaque ont un bonus de 1 et ceux de , defenses de 2,"], 4: ["Apres une bataille reussite lancer un de si il est , superieur a 5 vous gagner une unite,"], 5: [
        "lancer un de pour chaque mort durant une bataille si , le jet est 6 il revit,"], 6: ["au choix sois vous avez 1 bonus de deplacement ou une , unite ennemi a vous pour un jet égal à 6,"], 7: ["Vos adversaires ont un malus de 1 durant les batailles,"]}
    return l_ud


def liste_ad():
    liste_ad = {1: ["tout vos village apporte 1 unite par recolte disponible", "vous gagnez 1 recolte par village sans ressources", "vous pouvez offrir 1 recolte gratuitement", "vous pouvez deplacer 1 unite vers une autre", "chaque unite gagne 3 de deplacement", "si vous etes en plein combat vous pouvez deplacer une , unite vers la bataille", "votre prochain cout commerciale est diviser par 2",
                                    "vous pouvez faire payez le prochain cout monetaire d un , adversaire par 2", "votre port peut garder 2 ressource"], 
                                    2: ["vous pouvez detruire un village voisin", "vous pouvez faire perdre 1 recolte a un village voisin", "faite perdre une unite a un adversaire", "si vous etes en plein evenement combat rempemporter le , combat et relancer l evenement", "vous pouvez gagnez sois une unite ou une ressource", "vos jets ont un bonus de 1 pendant une bataille", 
                                    "vous pouvez offrir sois une ressource ou une unite , gratuitement", "si vous ne participez pas a une enchere choisissez qui , l'emportera", "votre port est inaccessible aux attaques et au actes , commerciales pendant 3 tours"], 
                                    3: ["vous pouvez detruire un village voisin les recoltes et , la proprieter est detruite","vous pouvez empecher le deroulement d une action , commerciale","faite perdre une unite a un adversaire","vous pouvez debarquez dans un lieu meme si il n y a pas , de port","vos villages peuvent avoir 2 ressource au lieu d une","vous gagnez une unite gratuitement",
                                    "si une unite ennemi ce trouve sur votre territoire , elle est eliminer","votre port gagne un bonus de 2 en defense"], 
                                    4: ["vos unite gagne 2 de deplacement si vous en posseder , minimum 4 pendant 1 tour","si vous etes sur un village abandonne il est desormais , en votre possession","vous pouvez deplacer une unite ou vous le voulez dans , votre territoire","votre port est inaccessible aux attaques et au actes , commerciales pendant 3 tours",
                                    "si vous etes a l origine d un acte commerciale vous , gagnez 1 de ressource de votyre choix","lors d un acte commerciale le cout a payez est divise , par 2","si vous posseder une relique vous gagnez un bonus de 1 , durant une bataille","vos defenses ont un bonus de 1","si vous agissez dans votre territoire vos jets ont un , bonus de 2"], 
                                    5: ["vos unites se deplacent plus vite en mer","vous pouvez detruire un port","vous avez un bonus de 2 dans les batailes maritime","vos unite gagne un bonuse de 2 deplacement pendant 1 , tour","si vous vous trouvez dans un village adverse sans defense , detruiser le","durant une bataille si vous avez moins d unite que votre , adversaire vos jets gagne un bonus de 1",
                                    "vous pouvez produire une recolte pour chaque village , sans ressources","vous pouvez donner une ressource gratuitement","votre prochain cout d acte commerciale est divise par 2"], 
                                    6: ["vous pouvez participer a un entretien diplomatique sans , y etre invite","vous pouvez annuler un entretien diplomatique","vous pouvez annuler un acte commerciale","vous pouvez deplacer une unite ou vous le voulez","vous pouvez recuperer une unite ennemie","durant un combat eleminer 2 unites ennemies","si vous avez une relique vous ne pouvez pas etre , attaquer pendant une seule bataille",
                                    "si vous avez une relique vous avez un bonus de 2 durant , une bataille","si vous avez une relique vous pouvez recuperer 3 unites , perdues"], 
                                    7: ["chaque unite gagne 3 de deplacement","vous gagnez 2 de deplacement en mer","pour chaque village dans votre territoire vous gagnez , 1 de deplacement pendant 1 tour","vous pouvez empecher un port ennemie d etre actif , pendant 1 tour","si vous participez a un acte commerciale vous le , remporte","vous gagnez 1 ressource par unite","vos ennemies ont un malus de 1 pendant 1 tour","si vous vous trouvez dans un village lancez un de si il , est egale a 6 il vous appartiens",
                                    "si une unite ce fait attaquer et que vous avez une , autre unite dans le meme pays vous pouvez la deplacer "]}
    return liste_ad