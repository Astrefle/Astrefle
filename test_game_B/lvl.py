import pygame
from pygame import*
from pygame.version import PygameVersion
from random import*
from ennemies import*
pygame.init()

p1 = P1()
mob = essaim_x()
mob1 = essaim_y()
mob2 = rayon_y()
mob3 = rayon_x()


def essaim(lvl_stage):

    if lvl_stage < 720:
        for i in mob.l_p2:
            i.moove()

        if len(mob.l_p2) < 1:
            mob.ennemies1()
        for i in mob.l_p2:
            if i.p2_hit.x < 0:
                mob.l_p2.remove(i)
        for i in mob1.l_p3:
            i.moove()
        if len(mob1.l_p3) < 1:
            mob1.ennemies1()
        for i in mob1.l_p3:
            if i.p3_hit.y < 0:
                mob1.l_p3.remove(i)

    if lvl_stage < 1440 and lvl_stage >= 720:
        for i in mob.l_p2:
            i.moove_f()
        if len(mob.l_p2) < 2:
            mob.ennemies1()
        for i in mob.l_p2:
            if i.p2_hit.x < 0:
                mob.l_p2.remove(i)
        for i in mob1.l_p3:
            i.moove_f()
        if len(mob1.l_p3) < 2:
            mob1.ennemies1()
        for i in mob1.l_p3:
            if i.p3_hit.y < 0:
                mob1.l_p3.remove(i)

    if lvl_stage < 2880 and lvl_stage >= 1440:
        for i in mob.l_p2:
            i.moove_ff()
        if len(mob.l_p2) < 3:
            mob.ennemies1()
        for i in mob.l_p2:
            if i.p2_hit.x < 0:
                mob.l_p2.remove(i)
        for i in mob1.l_p3:
            i.moove_ff()
        if len(mob1.l_p3) < 3:
            mob1.ennemies1()
        for i in mob1.l_p3:
            if i.p3_hit.y < 0:
                mob1.l_p3.remove(i)
    if lvl_stage > 2900:
        for i in mob.l_p2:
            mob.l_p2.remove(i)
        for i in mob1.l_p3:
            mob1.l_p3.remove(i)


def rayon(lvl_stage):
    if lvl_stage < 720:
        if len(mob2.l_ray) < 2 and len(mob3.l_rax) < 1:
            mob3.ray1()
            mob2.ray1()
        for i in mob2.l_ray:
            if lvl_stage > 360:
                i.moove_m()
            else:
                i.moove_p()
        for i in mob2.l_ray:
            if p1.p1_hit.x == i.ray_hit.x:
                p1.pv -= 1
                print(p1.pv)
        for i in mob3.l_rax:
            if lvl_stage > 360:
                i.moove_m()
            else:
                i.moove_p()
        for i in mob3.l_rax:
            if p1.p1_hit.x == i.rax_hit.y:
                p1.pv -= 1
                print(p1.pv)

    if lvl_stage < 1440 and lvl_stage > 720:
        if len(mob2.l_ray) < 3 and len(mob3.l_rax) < 2:
            mob3.ray1()
            mob2.ray1()
        for i in mob2.l_ray:
            if lvl_stage > 1080:
                i.moove_m()
            else:
                i.moove_p()
        for i in mob2.l_ray:
            if p1.p1_hit.x == i.ray_hit.x:
                p1.pv -= 1
                print(p1.pv)
        for i in mob3.l_rax:
            if lvl_stage > 1080:
                i.moove_m()
            else:
                i.moove_p()
        for i in mob3.l_rax:
            if p1.p1_hit.x == i.rax_hit.y:
                p1.pv -= 1
                print(p1.pv)
    if lvl_stage < 2160 and lvl_stage > 1440:
        if len(mob2.l_ray) < 4 and len(mob3.l_rax) < 3:
            mob3.ray1()
            mob2.ray1()
        for i in mob2.l_ray:
            if lvl_stage > 1800:
                i.moove_m()
            else:
                i.moove_p()
        for i in mob2.l_ray:
            if p1.p1_hit.x == i.ray_hit.x:
                p1.pv -= 1
                print(p1.pv)
        for i in mob3.l_rax:
            if lvl_stage > 1800:
                i.moove_m()
            else:
                i.moove_p()
        for i in mob3.l_rax:
            if p1.p1_hit.x == i.rax_hit.y:
                p1.pv -= 1
                print(p1.pv)
