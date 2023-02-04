import pygame
import programms.button
import random
import programms.Cara
import programms.liste


L = 600
H = 900

x = 0
y = 0

xb1 = 0
yb1 = 0

xb2 = 0
yb2 = 200

xb3 = 0
yb3 = 600

xb4 = 0
yb4 = 400


pygame.display.set_caption("Générateur_App")
screen = pygame.display.set_mode((L, H))
bg = pygame.image.load('assets/bg.png')

b = programms.button.Button
run = True

clic_objectif = False
clic_objectif_get = False
clic_reset = False
clic_event = False
clic_event_get = False
clic_monarch = False
clic_monarch_get = False

test_monarch = False
test_objectif = False

info = pygame.image.load('assets/info.png')
info_hit = info.get_rect()
info_hit.x = 0
info_hit.y = 800

info2 = pygame.image.load('assets/info2.png')
info2_hit = info2.get_rect()
info2_hit.x = 0
info2_hit.y = 0

info3 = pygame.image.load('assets/info3.png')
info3_hit = info3.get_rect()
info3_hit.x = 0
info3_hit.y = 0

info4 = pygame.image.load('assets/info4.png')
info4_hit = info4.get_rect()
info4_hit.x = 0
info4_hit.y = 0

v = 1
n = 1

###


class Objectif():
    def __init__(self):
        self.objectif = None
        self.running = True
        self.liste = None
        self.c = programms.Cara.Cara('vide', 10, 230)
        self.result = ' '
        self.espace = 10

    def choice(self):
        self.liste = programms.liste.liste_all()
        self.objectif = self.liste
        return ((self.objectif))

    def épeler(self, mot):
        self.n_liste = []
        mot = str(mot)
        for lettre in mot:
            if lettre == '[' or lettre == ']' or lettre == "'" or lettre == '"' or lettre == '{' or lettre == '}':
                pass
            elif lettre == ' ' or lettre == ':':
                self.n_liste.append('vide')

            elif lettre == ',':
                self.n_liste.append('return')
            else:
                self.n_liste.append(lettre)
        return self.n_liste


o = Objectif()


def o_execute():

    o.choice()
    o.épeler(o.objectif)

    for i in o.n_liste:
        o.c.add()
        o.c.ret(i)
        o.c.mot(i)


###


class Event():
    def __init__(self):

        self.c = programms.Cara.Cara('vide', 10, 230)
        self.running = True
        self.liste = programms.liste.liste_event()
        self.result = ' '

    def random_event(self, lieux):
        self.result = self.liste[lieux][random.randint(0, 3)]
        return self.result

    def épeler(self, mot):
        self.n_liste = []
        mot = str(mot)
        for lettre in mot:
            if lettre == '[' or lettre == ']' or lettre == "'" or lettre == '"' or lettre == '{' or lettre == '}':
                pass
            elif lettre == ' ' or lettre == ':':
                self.n_liste.append('vide')

            elif lettre == ',':
                self.n_liste.append('return')
            else:
                self.n_liste.append(lettre)
        return self.n_liste


e = Event()


def e_execute(v):

    e.random_event(v)
    e.épeler(e.result)
    for i in e.n_liste:
        e.c.add()
        e.c.ret(i)
        e.c.mot(i)

###


class Monarque():
    def __init__(self):

        self.c = programms.Cara.Cara('vide', 20, 230)
        self.running = True
        self.liste_u = programms.liste.liste_unite()
        self.liste_ud = programms.liste.liste_ud()
        self.liste_ad = programms.liste.liste_ad()
        self.result1 = ' '
        self.result2 = ' '
        self.result3 = []

    def choice(self, monarque):
        self.result2 = self.liste_ud[monarque]

        self.result3.append(self.liste_ad[monarque][random.randint(0, 2)])
        self.result3.append(self.liste_ad[monarque][random.randint(3, 5)])
        self.result3.append(self.liste_ad[monarque][random.randint(6, 8)])
        return self.result2, self.result3
        """ self.result3"""

    def épeler(self, mot):
        self.n_liste = []
        mot = str(mot)
        for lettre in mot:
            if lettre == '[' or lettre == ']' or lettre == "'" or lettre == '"' or lettre == '{' or lettre == '}':
                pass
            elif lettre == ' ' or lettre == ':':
                self.n_liste.append('vide')

            elif lettre == ',':
                self.n_liste.append('return')
            else:
                self.n_liste.append(lettre)
        return self.n_liste


m = Monarque()


def m_execute(n):
    m.choice(n)

    m.épeler(m.result2)
    for i in m.n_liste:
        m.c.add()
        m.c.ret(i)
        m.c.mot(i)

    m.épeler(m.result3)
    for j in m.n_liste:
        m.c.add()
        m.c.ret(j)
        m.c.mot(j)


###
rst = pygame.image.load(f"assets/nb/{v}.png")
rst_hit = rst.get_rect()
rst_hit.x = 250
rst_hit.y = 260

###

cp = pygame.image.load(f"assets/pr/{n}.png")
cp_hit = cp.get_rect()
cp_hit.x = 0
cp_hit.y = 400

###


while run:

    screen.blit(bg, (x, y))

    """print(clic_objectif,
          clic_objectif_get,
          clic_event,
          clic_event_get,
          clic_monarch,
          clic_monarch_get,
          clic_reset)"""

    if clic_objectif_get == True:
        for j in o.c.liste:
            screen.blit(j.lettre, (j.lettre_rect.x, j.lettre_rect.y))
        screen.blit(info2, (info2_hit.x, info2_hit.y))

    if clic_event == True:
        screen.blit(rst, (rst_hit.x, rst_hit.y))
        screen.blit(info, (info_hit.x, info_hit.y))

    if clic_event_get == True:
        for j in e.c.liste:
            screen.blit(j.lettre, (j.lettre_rect.x, j.lettre_rect.y))
        screen.blit(info3, (info3_hit.x, info3_hit.y))

    if clic_monarch == True:
        screen.blit(info4, (info4_hit.x, info4_hit.y))
        screen.blit(cp, (cp_hit.x, cp_hit.y))

    if clic_monarch_get == True:
        for k in m.c.liste:
            screen.blit(k.lettre, (k.lettre_rect.x, k.lettre_rect.y))
        screen.blit(info4, (info4_hit.x, info4_hit.y))

    if clic_monarch_get == True:
        bg = pygame.image.load('assets/bg2.png')
    else:
        bg = pygame.image.load('assets/bg.png')

    btn1 = pygame.image.load('assets/objectif.png')
    btn1_btn = b(xb1, yb1, btn1, 1)

    btn2 = pygame.image.load('assets/event.png')
    btn2_btn = b(xb2, yb2, btn2, 1)

    btn3 = pygame.image.load('assets/menu.png')
    btn3_btn = b(xb3, yb3, btn3, 1)

    btn4 = pygame.image.load('assets/monarque.png')
    btn4_btn = b(xb4, yb4, btn4, 1)

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
            pygame.quit()

        if clic_event == True:
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_UP:
                    if v < 14:
                        v += 1
                        rst = pygame.image.load(f"assets/nb/{v}.png")
                if i.key == pygame.K_DOWN:
                    if v > 1:
                        v -= 1
                        rst = pygame.image.load(f"assets/nb/{v}.png")

                if i.key == pygame.K_RETURN:
                    clic_event = False
                    clic_event_get = True
                    e_execute(v)

        if clic_monarch == True:
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_UP:
                    if n < 7:
                        n += 1
                        cp = pygame.image.load(f"assets/pr/{n}.png")
                        print(n)
                if i.key == pygame.K_DOWN:
                    if n > 1:
                        n -= 1
                        cp = pygame.image.load(f"assets/pr/{n}.png")
                        print(n)

                if i.key == pygame.K_RETURN:
                    if test_monarch == False:
                        clic_monarch = False
                        clic_monarch_get = True
                        test_monarch = True
                        m_execute(n)
                        print("m_t_f")
                    else:
                        clic_monarch = False
                        clic_monarch_get = True
                        print("m_t_t")

    if clic_objectif == True:
        clic_reset = True

    if btn1_btn.draw(screen) and clic_objectif == False:
        if clic_objectif_get == False:
            if test_objectif == False:
                yb1 = 1000
                yb2 = 1000
                yb4 = 1000
                yb3 = 600
                print('test1')
                clic_objectif = True
                clic_objectif_get = True
                o_execute()
                test_objectif = True
            else:
                yb1 = 1000
                yb2 = 1000
                yb4 = 1000
                yb3 = 600
                clic_objectif = True
                clic_objectif_get = True

    if clic_event == True:
        clic_reset = True

    if btn2_btn.draw(screen) and clic_event == False:
        clic_event = True
        info_hit.y = 0
        yb1 = 1000
        yb2 = 1000
        yb4 = 1000
        yb3 = 600

    if clic_monarch == True:
        clic_reset = True

    if btn4_btn.draw(screen) and clic_monarch == False:
        if test_monarch == False:
            if clic_monarch_get == False:
                yb1 = 1000
                yb2 = 1000
                yb4 = 1000
                yb3 = 600
                clic_monarch = True
        else:
            yb1 = 1000
            yb2 = 1000
            yb4 = 1000
            yb3 = 600
            clic_monarch_get = True
            clic_reset = True

    if btn3_btn.draw(screen):
        yb1 = 000
        yb2 = 200
        yb3 = 600
        yb4 = 400
        clic_monarch_get = False
        clic_monarch = False
        clic_event = False
        clic_event_get = False
        clic_objectif = False
        clic_objectif_get = False
        clic_reset = False
        e.c.clean()

    pygame.display.flip()
