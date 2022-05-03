#EXO
###

import re
from traceback import print_tb


f=[5,3,8]
def moyenne(liste):
    if liste==[]:
        return 'erreur'
    else:
        m=0
        for elt in liste:
            m+=elt
        m=m/len(liste)
        return m

"print(moyenne(f))"
###

def max_dico(dic):
    m = 0
    nom_m = ""
    for nom,v in dic.items():
        if v > m:
            m = v
            nom_m = nom
    return (nom_m,m)

"""print(max_dico({'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50}))"""
###

def recherche(elt,tab):
    if not elt in tab:
        return -1
    rec=0
    for i in range(len(tab)):
        if elt==tab[i]:
            rec=i
    return rec

'print( recherche(1,[8,1,10,1,7,1,8]))'
###

def maxi(tab):
    val=0
    id=0
    for i in range(len(tab)):
        if val< tab[i]:
            val=tab[i]
            id=i

    return val,id

'print (maxi([1,5,6,9,1,2,3,7,9,8]))'
###

def rechercheMinMax(tableau):
    dic={"min":'None',"max":'None'}
    m=tableau[0]
    M=tableau[0]
    for i in tableau:
        if M<i:
            M=i
            dic['max']=M
        elif m>i:
            m=i
            dic['min']=m
    return dic

'tableau = [0, 1, 4, 2, -2, 9, 3, 1, 7, 1]'
'resultat = rechercheMinMax(tableau)'
'print(resultat)'
###

def moyenne(tab):
    m=0
    for i in tab:
        m+=i
    m/=len(tab)
    return m

'print(moyenne([1.0, 2.0, 4.0]))'
###

def indice_du_min(tab):
    if len(tab)==1:
        return 0
    else:
        m=tab[0]
        id=0
        for i in range(len(tab)):
            if m>tab[i]:
                m=tab[i]
                id=i
        return id

'print(indice_du_min([5, 3, 2, 2, 4]))'
###

def mini(r,d):
    m=r[0]
    id=0
    for i in range(len(r)):
        if m>r[i]:
            m=r[i]
            id=i
    return m,d[id]

't_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]'
'annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]'
'print(mini(t_moy, annees))'
###

def nb_repetitions(elt,tab):
    nb=0
    for i in tab:
        if i==elt:
            nb+=1
    return nb

'print(nb_repetitions(5,[2,5,3,5,6,9,5]))'
###

def recherche_paire(tab):
    t=[]
    for i in range(len(tab)):
        if i<len(tab)-1:
            if tab[i]==tab[i+1]-1:
                a=tab[i]
                b=tab[i+1]
                c=a,b
                t.append(c)
    return t

"""print(recherche_paire([5, 1, 2, 3, 8, -5, -4, 7]))"""
###

def calcul(k):
    t=[]
    while k>1:
        if k%2==0:
            k//=2
            t.append(k)
        elif k%2!=0:
            k=(k*3)+1
            t.append(k)
    return t

'print(calcul(7))'
###

"""def multiplication(n1,n2):
    rez=0
    if n1>0 and n2>0:
        for i in range(n1):
            rez+=n2
    elif n1<0 and n2<0:
        for i in range()

    return rez

print(multiplication(-4,-8))
"""
###

def moy_ass(tab):
    t=0
    for i in tab:
        t+=i
    if len(tab)%2==0:
        t/=len(tab)
    else:
        t//=len(tab)
    return (t)


###

def convertir(T):
    r_bin=0
    v=(len(T))
    id_bin=2**v

    for i in range(len(T)):
    ###print(i,r_bin,v,id_bin)
        v-=1
        id_bin=2**v
        if T[i]==1:
            r_bin+=id_bin
    return r_bin

"""print(convertir([1, 0, 0, 0, 0, 0, 1, 0]))"""
###

def rendu(somme_a_rendre):
    banque=[5,2,1]
    tab=[0,0,0]
    i=0
    j=0
    while somme_a_rendre>0:
        while j+banque[i]<=somme_a_rendre:
            tab[i]+=1
            j+=banque[i]
        somme_a_rendre-=j
        ###print(j,somme_a_rendre)
        j=0
        i+=1
    return tab

"""print(rendu(64))"""
###

def recherche_l(cara,mot):
    nb=0
    for i in mot:
        if i==cara:
            nb+=1
    return nb

"""print(recherche_l('i',"mississippi"))"""
###

def moyenne_note(liste):
    moy=0
    div=0
    for i in range(len(liste)):
        moy=moy+(liste[i][1]*liste[i][0])
        ###print(moy)
    for i in range(len(liste)):
        div+=liste[i][1]
        ###print (div)
    moy/=div
    return moy

"""print(moyenne_note([(15,2),(9,1),(12,3)]))"""
###

def delta(tab):
    t=[]
    t.append(tab[0])
    n_nb=0
    for i in range(0,len(tab)-1):
        n_nb=tab[i+1]-tab[i]
        t.append(n_nb)
    return t

"""print(delta([1000, 800, 802, 1000, 1003]))"""
###

def conv_bin(n):
    b=[]
    while n!=0:
        b.append(n%2)
        n//=2
    b.reverse()
    return b,len(b)

"""print(conv_bin(255))"""
###

def occurence_lettres (phrase):
    dic = {}
    for i in phrase:
        if i in dic:
            dic[i] = dic[i] + 1
        else :
            dic[i] = 1
    return dic

"""print(occurence_lettres('Ngolo Kante'))"""
###

def correspond(mot,mat):
    i = 0
    n = len(mot)
    m = len(mat)
    if n != m :
        return False
    for i in range(n):
        if mat[i] != '*':
            if mot[i] != mat[i]:
                return False
    return True

"""print(correspond('INFORMATIQUE', 'INFO*MA*IQUE'))"""
###

def nombre_de_mots(phrase):
    esp=0
    for i in phrase:
        if i==' ':
            esp+=1
    return esp

"""print(nombre_de_mots('Gilbouze macarbi acra cor ed filbuzine ?'))"""
###

def xor(l_b1,l_b2):
    assert len(l_b1)==len(l_b2)
    l_br=[]
    for i in range(len(l_b1)):
        if l_b1[i]==l_b2[i]:
            l_br.append(0)
        else:
            l_br.append(1)
    return l_br

'''a = [1, 0, 1, 0, 1, 1, 0, 1]
b = [0, 1, 1, 1, 0, 1, 0, 0]
c = [1, 1, 0, 1]
d = [0, 0, 1, 1]

print(xor(a,b))
print(xor(c,d))'''
###

def reverse(mot):
    r_m=' '
    for i in mot:
        r_m=i+r_m
    return r_m

"""print(reverse("informatique"))"""
###

def maxliste(tab):
    m_nb=0
    for i in tab:
        if i>m_nb:
            m_nb=i
    return m_nb

'''print(maxliste([98, 12, 104, 23, 131, 9]))'''
###

def selection_enclos(animaux,num_enclos):
    t = []
    for i in animaux:
        if i['enclos'] == num_enclos:
            t.append(i)
    return t

"""animaux = [ {'nom':'Medor', 'espece':'chien', 'age':5, 'enclos':2},
 {'nom':'Titine', 'espece':'chat', 'age':2, 'enclos':5},
 {'nom':'Tom', 'espece':'chat', 'age':7, 'enclos':4},
 {'nom':'Belle', 'espece':'chien', 'age':6, 'enclos':3},
 {'nom':'Mirza', 'espece':'chat', 'age':6, 'enclos':5}]

print(selection_enclos(animaux, 5))"""
###

def tri_bulles(T):
    n = len(T)
    for i in range(n-1,0,-1):
        for j in range(i):
            if T[j] > T[j+1]:
                temp = T[j]
                T[j] = T[j+1]
                T[j+1] = temp
    return T

random.randint(1,10)
print(tri_bulles([random.randint(1,10) for i in range(0,10)]))
###

def pascal(n):
    C= [[1]]
    for k in range(1,n+1):
        Ck = [1]
        for i in range(1,k):
            Ck.append(C[k-1][i-1]+C[k-1][i])
        Ck.append(1)
        C.append(Ck)
    return C

"print(pascal(4))"
###

def rendu_glouton(arendre, solution=[], i=0):
    pieces = [100,50,20,10,5,2,1]
    if arendre == 0:
        return solution
    p = pieces[i]
    if p <= arendre :
        solution.append(p)
        return rendu_glouton(arendre - p, solution,i)
    else :
        return rendu_glouton(arendre, solution,i+1)

"print(rendu_glouton(68,[],0))"


