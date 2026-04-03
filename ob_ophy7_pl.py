import colorsys
import multiprocessing
import sys
import os.path
import time
import tkinter as n_9
from math import floor, sqrt, inf
from tkinter import ttk, font
from typing import List, Optional, Literal
from datetime import datetime
from probleme import resoudre
a_1 = "#00dd00"
b_1 = "#ff0000"
c_1 = "_"
def d_1(e_1, f_1=(), g_1=60):
    h_1 = time.time()
    i_1 = multiprocessing.Process(target=e_1, args=f_1)
    i_1.start()
    i_1.join(g_1)
    if i_1.is_alive():
        i_1.terminate()  
        i_1.join()  
        print(f"Temps ecoule ({g_1}s) - le programme a ete arrete")
        return inf
    return time.time() - h_1
def j_1(k_1, l_1="", m_1=True, n_1=0):
    try:
        return int(k_1)
    except ValueError:
        print(f"ERREUR : '{k_1}' n'est pas un int {l_1}")
        if m_1:
            exit(0)
        else:
            return n_1
def o_1(k_1, l_1="", m_1=True, n_1=0):
    try:
        return float(k_1)
    except ValueError:
        print(f"ERREUR : '{k_1}' n'est pas un float {l_1}")
        if m_1:
            exit(0)
        else:
            return n_1
class P1:
    def __init__(self, q_1: float, r_1: float):
        self.s_1 = [q_1, r_1]
    @property
    def t_1(self):
        return self.s_1
    def u_1(self, v_1):
        return sqrt((v_1.t_1[0] - self.s_1[0]) ** 2 + (v_1.t_1[1] - self.s_1[1]) ** 2)
    def w_1(self):
        return f"({self.s_1[0]:.2f},{self.s_1[1]:.2f})"
class X1:
    def __init__(self, y_1: int, z_1: List[float]):
        self.a_2 = y_1
        self.b_2 = [
            P1(q_1, r_1)
            for q_1, r_1 in zip(z_1[::2], z_1[1::2])
        ]
    @property
    def c_2(self):
        return self.b_2
    @property
    def y_1(self):
        return self.a_2
class D2:
    def __init__(self, e_2: str, f_2: int):
        self.g_2 = e_2
        self.h_2 = f_2
        self.i_2 = [0, 0]
        self.j_2 = []
        self.k_2 = True
    @property
    def e_2(self):
        return self.g_2
    @property
    def f_2(self):
        return self.h_2
    @property
    def l_2(self):
        return self.i_2
    @property
    def m_2(self):
        return self.j_2
    @property
    def n_2(self):
        return self.k_2
    @n_2.setter
    def n_2(self, n_2: bool):
        self.k_2 = n_2
    def o_2(self, p_2: str):
        q_2 = p_2 + c_1 + self.g_2+".txt"
        if not os.path.exists(q_2):
            print("Le fichier", q_2, "n'existe pas")
            exit(0)
        with open(q_2, "r") as r_2:
            s_2 = [_.strip() for _ in r_2.readlines() if _.strip() != ""]
            t_2 = s_2.pop(0)
            self.i_2 = [o_1(_.strip(), "pour les dimensions de la plaque "+self.g_2) for _ in t_2.split()]
            if len(self.i_2) != 2:
                print("ERREUR: Le nombre de dimensions de la plaque "+self.g_2+" n'est pas correct, dans " + q_2)
                print(t_2)
                exit(0)
            for y_1, t_2 in enumerate(s_2):
                z_1 = [o_1(_.strip(), "comme coordonnee de point, dans " + q_2) for _ in t_2.split()]
                if len(z_1) % 2 != 0:
                    print(
                        "ERREUR: Le nombre de coordonnees d'un polygone n'est pas pair, dans " + q_2)
                    print(t_2)
                    exit(0)
                self.j_2.append(X1(y_1, z_1))
class U2:
    def __init__(self, v_2: float, w_2: float, x_2: List[float]):
        self.y_2 = v_2
        self.z_2 = w_2
        self.a_3 = x_2
    @property
    def v_2(self):
        return self.y_2
    @property
    def w_2(self):
        return self.z_2
    @property
    def x_2(self):
        return self.a_3
class B3:
    def __init__(self, c_3: float, x_2: List[float]):
        self.d_3 = c_3
        self.a_3 = x_2
    @property
    def c_3(self):
        return self.d_3
    @property
    def x_2(self):
        return self.a_3
class E3:
    def __init__(self, y_1: int):
        self.a_2 = y_1
        self.f_3 = [0, 0]
        self.g_3 = 0
    def h_3(self, l_2: list):
        self.f_3 = l_2
    def i_3(self, j_3: float):
        self.g_3 = j_3
    @property
    def y_1(self):
        return self.a_2
    @property
    def k_3(self):
        return self.g_3
    @property
    def l_3(self):
        return self.f_3
class M3:
    def __init__(self, n_3, o_3: D2, p_3: P1, q_3: bool):
        self.r_3 = n_3
        self.s_3 = o_3
        self.t_3 = p_3
        self.u_3 = q_3
        self.k_2 = True
    @property
    def n_3(self):
        return self.r_3
    @property
    def o_3(self):
        return self.s_3
    @property
    def p_3(self):
        return self.t_3
    @property
    def q_3(self):
        return self.u_3
    @property
    def n_2(self):
        return self.k_2
    @n_2.setter
    def n_2(self, n_2: bool):
        self.k_2 = n_2
    def v_3(self):
        q_1 = self.t_3.t_1[0] + (self.s_3.l_2[1] if self.u_3 else self.s_3.l_2[0])
        r_1 = self.t_3.t_1[1] + (self.s_3.l_2[0] if self.u_3 else self.s_3.l_2[1])
        return P1(q_1, r_1)
    def w_1(self):
        return f"{self.s_3.e_2} en {self.t_3}->{self.v_3()}"
class W3:
    def __init__(self, p_2: str):
        self.x_3 = p_2
        self.y_3 = []
        self.y_3.append(None)
        self.z_3 = 0
        self.a_4 = 0
        self.b_4 = []
        self.c_4 = []
        self.d_4 = 0
        self.e_4 = []
        if not p_2 or not os.path.exists(self.x_3+c_1+"plaques.txt"):
            print(f"L'instance {self.x_3} est introuvable")
            exit(0)
        else:
            self.f_4()
    def g_4(self) -> str:
        h_4 = "-------- STATS INSTANCE" + "\n"
        if self.b_4:
            h_4 += f"Nombre de metaux : {len(self.b_4)}\n"
            h_4 += f"Nombre d'alliages : {len(self.c_4)}\n"
        h_4 += f"Nombre de fournisseurs : {len(self.y_3) - (0 if self.b_4 else 1)}\n"
        h_4 += f"Nombre de plaques : {len(self.e_4)}\n"
        h_4 += f"Nombre total d'exmplaires de plaque : {sum([_.f_2 for _ in self.i_4])}\n"
        return h_4
    @property
    def p_2(self):
        return self.x_3
    @property
    def j_4(self):
        return self.y_3
    @property
    def k_4(self):
        return self.z_3
    @property
    def l_4(self):
        return self.a_4
    @property
    def m_4(self):
        return self.b_4
    @property
    def n_4(self):
        return self.c_4
    @property
    def o_4(self):
        return self.d_4
    @property
    def i_4(self):
        return self.e_4
    def p_4(self):
        q_2 = self.x_3 + c_1 + "fonderie.txt"
        if os.path.exists(q_2):
            with open(q_2, "r") as r_2:
                s_2 = [_.strip() for _ in r_2.readlines() if _.strip() != ""]
                t_2 = s_2.pop(0)
                q_4 = [o_1(_.strip(), "comme dimension de la tole de la fonderie") for _ in t_2.split()]
                if len(q_4) != 3:
                    print("Il manque une des 3 dimensions de la tole de la fonderie, dans "+q_2)
                    exit(0)
                self.y_3[0] = E3(0)
                self.y_3[0].h_3([q_4[0], q_4[1]])
                self.z_3 = q_4[2]
                t_2 = s_2.pop(0)
                self.a_4 = o_1(t_2, "pour le cout de fonte, dans "+q_2)
                t_2 = s_2.pop(0)
                v_2 = [o_1(_.strip(), "pour un prix d'achat de metal, dans "+q_2) for _ in t_2.split()]
                t_2 = s_2.pop(0)
                w_2 = [o_1(_.strip(), "pour une masse volumique de metal, dans "+q_2) for _ in t_2.split()]
                t_2 = s_2.pop(0)
                r_4 = [o_1(_.strip(), "pour un pourcentage minimum de metal, dans "+q_2) for _ in t_2.split()]
                t_2 = s_2.pop(0)
                s_4 = [o_1(_.strip(), "pour un pourcentage maximum de metal, dans "+q_2) for _ in t_2.split()]
                if len(w_2) != len(v_2):
                    print("ERREUR: Le nombre d'informations dans les lignes prix et masses volumiques ne sont pas egaux, dans "+q_2)
                    exit(0)
                if len(r_4) != len(v_2) or len(r_4) != len(v_2):
                    print("ERREUR: Le nombre d'informations dans les lignes prix et les pourcentages demandes ne sont pas egaux, dans "+q_2)
                    exit(0)
                for t_4 in range(len(v_2)):
                    self.b_4.append(U2(v_2[t_4], w_2[t_4], [r_4[t_4], s_4[t_4]]))
                for t_2 in s_2:
                    u_4 = [o_1(_.strip(), "pour une information d'un alliage, dans "+q_2) for _ in t_2.split()]
                    if len(u_4) != len(v_2) + 1:
                        print("ERREUR: Le nombre d'informations sur un alliage n'est pas correct, dans " + q_2)
                        print(t_2)
                        exit(0)
                    self.c_4.append(B3(u_4[0], u_4[1:]))
                r_2.close()
    def v_4(self):
        q_2 = self.x_3 + c_1 + "fournisseurs.txt"
        if not os.path.exists(q_2):
            print("Le fichier", q_2, "n'existe pas")
            exit(0)
        with open(q_2, "r") as r_2:
            s_2 = [_.strip() for _ in r_2.readlines() if _.strip() != ""]
            for t_2 in s_2:
                u_4 = [_.strip() for _ in t_2.split()]
                if len(u_4) != 4:
                    print("ERREUR: Le nombre d'informations d'un z_4 n'est pas correct, dans "+q_2)
                    print(t_2)
                    exit(0)
                w_4 = j_1(u_4[0], "pour le numero d'un fournisseur, dans "+q_2)
                x_4 = o_1(u_4[1], "pour la dimension de tole d'un fournisseur, dans "+q_2)
                y_4 = o_1(u_4[2], "pour la dimension de tole d'un fournisseur, dans "+q_2)
                v_2 = o_1(u_4[3], "pour le prix de tole d'un fournisseur, dans "+q_2)
                z_4 = E3(w_4)
                z_4.h_3([x_4, y_4])
                z_4.i_3(v_2)
                self.y_3.append(z_4)
            r_2.close()
    def a_5(self):
        q_2 = self.x_3 + c_1 + "plaques.txt"
        if not os.path.exists(q_2):
            print("Le fichier", q_2, "n'existe pas")
            exit(0)
        with open(q_2, "r") as r_2:
            s_2 = [_.strip() for _ in r_2.readlines() if _.strip() != ""]
            t_2 = s_2.pop(0)
            self.d_4 = float(t_2)
            for t_2 in s_2:
                u_4 = [_.strip() for _ in t_2.split()]
                if len(u_4) != 2:
                    print("ERREUR: Le nombre d'informations sur une plaque n'est pas correct, dans "+q_2)
                    print(t_2)
                    exit(0)
                o_3 = D2(u_4[0], j_1(u_4[1], "pour le nombre d'exemplaires de la plaque "+u_4[0]+", dans "+q_2))
                self.e_4.append(o_3)
                o_3.o_2(self.x_3)
            r_2.close()
    def f_4(self):
        self.v_4()
        self.p_4()
        self.a_5()
class B5:
    def __init__(self, y_1, l_2: List[float]):
        self.a_2 = y_1
        self.i_2 = l_2
        self.c_5 = []
        self.d_5 = [P1(0, 0)]
    @property
    def y_1(self):
        return self.a_2
    @property
    def l_2(self):
        return self.i_2
    @property
    def e_5(self):
        return self.c_5
    def f_5(self, g_5):
        self.c_5.append(g_5)
    def h_5(self, o_3):
        return [_ for _ in self.c_5 if _.o_3 == o_3]
    def i_5(self):
        j_5 = 0
        if self.c_5:
            j_5 = sum([_.o_3.l_2[0]*_.o_3.l_2[1] for _ in self.c_5])
        return j_5 / (self.i_2[0] * self.i_2[1])
class K5:
    def __init__(self, o_3: D2):
        self.s_3 = o_3
        self.l_5: List[List[int]] = []
    @property
    def o_3(self):
        return self.s_3
    @property
    def m_5(self):
        return self.l_5
    def u_1(self):
        n_5 = P1(0, 0)
        o_5 = n_5
        u_1 = 0
        for [p_5, q_5] in self.l_5:
            r_5 = self.s_3.m_2[p_5].c_2[q_5]
            u_1 += o_5.u_1(r_5)
            o_5 = r_5
        u_1 += o_5.u_1(n_5)
        return u_1
class S5:
    def __init__(self, t_5: W3):
        self.u_5 = t_5
        self.v_5: float = 0
        self.w_5: float = 0
        self.x_5: Optional[E3] = None
        self.y_5 = [0 for _ in self.u_5.m_4]
        self.z_5 = [0 for _ in self.u_5.n_4]
        self.a_6: List[B5] = []
        self.b_6: List[K5] = [K5(_) for _ in self.u_5.i_4]
        self.c_6 = []
        self.d_6 = []
        self.e_6()
        if self.f_6():
            self.g_6()
            if self.x_5.y_1 == 0:
                self.h_6()
                self.i_6()
                self.j_6()
            self.k_6()
            self.l_6()
            self.m_6()
            self.n_6()
        else:
            for o_3 in self.u_5.i_4:
                o_3.n_2 = False
        self.k_2 = self.f_6() and sum(len(o_6[1]) for o_6 in self.c_6) == 0
    def f_6(self):
        return self.x_5 is not None
    @property
    def p_6(self):
        return self.v_5
    @property
    def q_6(self):
        return self.w_5
    @property
    def n_2(self):
        return self.k_2
    @property
    def r_6(self):
        return self.a_6
    @property
    def s_6(self):
        return self.b_6
    @property
    def t_6(self):
        return self.y_5
    @property
    def u_6(self):
        return self.z_5
    @property
    def z_4(self):
        return self.x_5
    @property
    def v_6(self):
        return self.c_6
    def e_6(self):
        q_2 = self.u_5.p_2 + "_sol.txt"
        if not os.path.exists(q_2):
            print(f"Le fichier {q_2} est introuvable")
            return
        with open(q_2) as r_2:
            s_2 = [_.strip() for _ in r_2.readlines() if _.strip() != ""]
            t_2 = s_2.pop(0)
            q_4 = [_.strip() for _ in t_2.split()]
            if len(q_4) != 3:
                print(f"ERREUR: format 'cout numFournisseur nbToles' non respecte, r_2 {q_2}, {t_2}")
                if len(q_4) < 3:
                    exit(0)
            self.v_5 = o_1(q_4[0], f"pour le cout, fichier {q_2}, {t_2}")
            w_6 = j_1(q_4[1], f"pour le numero de fournisseur, fichier {q_2}, {t_2}")
            self.x_5 = next((f for f in self.u_5.j_4 if f and f.y_1 == w_6), None)
            if not self.x_5:
                print(f"ERREUR: fournisseur {w_6} inconnu, fichier {q_2}")
                exit(0)
            x_6 = j_1(q_4[2], f"pour le nombre de toles, fichier {q_2}, {t_2}")
            if x_6 < 0:
                print(f"ERREUR: nombre de toles {x_6} impossible, fichier {q_2}")
                exit(0)
            self.a_6 = [B5(_, self.x_5.l_3) for _ in range(x_6)]
            if self.x_5.y_1 == 0:
                t_2 = s_2.pop(0)
                q_4 = [_.strip() for _ in t_2.split()]
                if len(q_4) != len(self.u_5.m_4)+len(self.u_5.n_4):
                    print(f"ERREUR: la ligne ne contient pas les {len(self.u_5.m_4)+len(self.u_5.n_4)} poids de metaux et alliages attendus, fichier {q_2}, {t_2}")
                    exit(0)
                self.y_5 = [o_1(_, f"pour un poids de metal achete, fichier {q_2}, {t_2}") for _ in q_4[:len(self.u_5.m_4)]]
                self.z_5 = [o_1(_, f"pour un poids d'alliage recycle, fichier {q_2}, {t_2}") for _ in q_4[len(self.u_5.m_4):]]
                if min(self.y_5+self.z_5) < -1e-6:
                    print(f"ERREUR: au moins un poids est negatif, fichier {q_2}, {t_2}")
                    exit(0)
            y_6 = [_.e_2 for _ in self.u_5.i_4]
            while s_2:
                t_2 = s_2.pop(0)
                q_4 = [_.strip() for _ in t_2.split()]
                if q_4[0] in y_6:
                    z_6 = q_4.pop(0)
                    o_3 = next((_ for _ in self.u_5.i_4 if _.e_2 == z_6), None)
                    if o_3 is None:
                        print(f"ERREUR: nom de plaque {z_6} inconnu, fichier {q_2}, {t_2}")
                        exit(0)
                    a_7 = next((_ for _ in self.b_6 if _.o_3 == o_3), None)
                    if len(q_4) % 2 != 0:
                        print(f"ERREUR: le trajet du laser de la plaque {z_6} n'est pas decrit pas un nombre pair d'informations, r_2 {q_2}, {t_2}")
                        exit(0)
                    while q_4:
                        p_5 = q_4.pop(0)
                        p_5 = j_1(p_5, f"pour un numero de polygone de la plaque {z_6}, fichier {q_2}, {t_2}")
                        if p_5 < 0 or p_5 >= len(o_3.m_2):
                            print(f"ERREUR: numero {p_5} de polygone de la plaque {z_6} non compris entre 0 et {len(o_3.m_2)-1}, fichier {q_2}, {t_2}")
                            exit(0)
                        q_5 = q_4.pop(0)
                        q_5 = j_1(q_5, f"pour un numero de point du polygone {p_5} de la plaque {z_6}, fichier {q_2}, {t_2}")
                        if q_5 < 0 or q_5 >= len(o_3.m_2[p_5].c_2):
                            print(f"ERREUR: numero {q_5} de point du polygone {p_5} de la plaque {z_6} non compris entre 0 et {len(o_3.m_2[p_5].c_2)-1}, fichier {q_2}, {t_2}")
                            exit(0)
                        a_7.m_5.append([p_5, q_5])
                elif q_4[0].isdigit():
                    if len(q_4) != 5:
                        print(f"ERREUR: la ligne ne respecte pas le format demande 'num_tole nom_plaque x y touner01', r_2 {q_2}, {t_2}")
                        exit(0)
                    b_7 = j_1(q_4[0], f"pour le numero de tole, fichier {q_2}, {t_2}")
                    if b_7 < 0 or b_7 >= len(self.a_6):
                        print(f"ERREUR: numero de tole {b_7} non compris entre 0 et {len(self.a_6)-1}, fichier {q_2}, {t_2}")
                        exit(0)
                    o_3 = next((_ for _ in self.u_5.i_4 if _.e_2 == q_4[1]), None)
                    if o_3 is None:
                        print(f"ERREUR: nom de plaque {q_4[1]} inconnu, fichier {q_2}, {t_2}")
                        exit(0)
                    q_1 = o_1(q_4[2], f"pour une coordonnee x de decoupe, fichier {q_2}, {t_2}")
                    r_1 = o_1(q_4[3], f"pour une coordonnee y de decoupe, fichier {q_2}, {t_2}")
                    q_3 = j_1(q_4[4], f"pour une rotation 0 ou 1 de decoupe, fichier {q_2}, {t_2}")
                    if q_3 not in [0, 1]:
                        print(f"ERREUR: {q_3} n'est pas une rotation 0 ou 1 de decoupe, fichier {q_2}, {t_2}")
                        exit(0)
                    self.a_6[b_7].f_5(M3(self.a_6[b_7], o_3, P1(q_1, r_1), q_3==1))
                else:
                    print(f"ERREUR: le premier mot {q_4[0]} de la ligne n'est ni un nom de plaque ni un numero de tole, fichier {q_2}, {t_2}")
                    exit(0)
    def c_7(self):
        d_7 = self.y_5.copy()
        for e_7, f_7 in enumerate(self.u_5.n_4):
            for g_7 in range(len(self.u_5.m_4)):
                d_7[g_7] += self.z_5[e_7] * f_7.x_2[g_7]
        return d_7
    def h_7(self):
        d_7 = self.c_7()
        i_7 = [0 for _ in range(len(self.u_5.m_4))]
        for g_7, j_7 in enumerate(self.u_5.m_4):
            i_7[g_7] = d_7[g_7] * 1000 / j_7.w_2
        return i_7
    def k_7(self):
        return sum(self.y_5[t_4] * self.u_5.m_4[t_4].v_2 for t_4 in range(len(self.u_5.m_4)))
    def l_4(self):
        i_7 = self.h_7()
        return self.u_5.l_4 * sum(i_7)
    def l_7(self):
        if not self.x_5:
            return 0
        if self.x_5.y_1 == 0:
            return self.l_4() + self.k_7()
        else:
            return self.x_5.k_3 * len(self.a_6)
    def o_4(self):
        return self.u_5.o_4 * sum([_.u_1() * _.o_3.f_2 for _ in self.b_6])
    def h_4(self):
        h_4 = "-------- STATS DE VOTRE SOLUTION\n"
        if not self.f_6():
            h_4 += f"Aucune solution fournie\n"
        else:
            h_4 += f"Nombre de toles : {len(self.a_6)}\n"
            h_4 += f"Cout annonce : {self.v_5}\n\n"
            h_4 += "-------- VERIFICATION DE VOTRE SOLUTION\n"
            m_7 = "OUI" if sum(len(o_6[1]) + len(o_6[2]) for o_6 in [self.c_6[0]]) == 0 else "NON"
            h_4 += f"Evaluation correcte : {m_7}\n"
            n_7 = "OUI" if sum(len(o_6[1]) for o_6 in self.c_6) == 0 else "NON"
            h_4 += f"Solution realisable : {n_7}\n"
            if self.d_6:
                h_4 += "\n-------- DETAIL DU COUT REEL\n"
                for o_7 in self.d_6:
                    h_4 += o_7 + "\n"
            if sum(len(p_7[1]) + len(p_7[2]) for p_7 in self.c_6):
                h_4 += "\n-------- SYNTHESE DES PROBLEMES\n"
                for p_7 in self.c_6:
                    if len(p_7[1]) + len(p_7[2]) > 0:
                        h_4 += f"{p_7[0]} : {len(p_7[1])} erreurs, {len(p_7[2])} warnings\n"
                h_4 += "\n-------- DETAIL DES PROBLEMES\n"
                for p_7 in self.c_6:
                    if len(p_7[1]) + len(p_7[2]) > 0:
                        h_4 += "\n" + p_7[0] + " :\n"
                        for o_6 in p_7[1][:20]: h_4 += f"* ERREUR : {o_6}\n"
                        if len(p_7[1]) > 20: h_4 += f"  ... et {len(p_7[1]) - 20} autres\n"
                        for o_6 in p_7[2][:20]: h_4 += f"* WARNING : {o_6}\n"
                        if len(p_7[2]) > 20: h_4 += f"  ... et {len(p_7[2]) - 20} autres\n"
        return h_4
    def g_6(self):
        p_7 = ["Verification du cout reel", [], []]
        self.c_6.insert(0, p_7)
        o_4 = self.o_4()
        l_7 = self.l_7()
        self.d_6.append(f"Cout des trajets de laser : {o_4:10.2f}")
        self.d_6.append(f"Cout des toles            : {l_7:10.2f}")
        if self.x_5.y_1 == 0:
            self.d_6.append(f"     dont achat de metaux : {self.k_7():10.2f}")
            self.d_6.append(f"       et fonte/laminage  : {self.l_4():10.2f}")
            self.x_5.i_3(l_7 / len(self.a_6))
        self.w_5 = l_7 + o_4
        if abs(self.w_5 - self.v_5) > 0.05:
            p_7[2].insert(0, f"Le cout reel est de {self.w_5:.2f} au lieu de {self.v_5:.2f} annonce")
    def h_6(self):
        p_7 = ["Verification du volume de metal fondu", [], []]
        self.c_6.append(p_7)
        q_7 = self.u_5.j_4[0].l_3[0]
        r_7 = self.u_5.j_4[0].l_3[1]
        s_7 = self.u_5.k_4
        t_7 = sum(self.h_7())
        u_7 = 0.001
        v_7 = int(floor(u_7 + t_7/(q_7*r_7*s_7)))
        w_7 = len(self.a_6) * self.u_5.k_4 * self.x_5.l_3[0] * self.x_5.l_3[1]
        if v_7 < len(self.a_6):
            p_7[1].append(f"Le volume de metal fondu est {t_7:.2f} cm3 < {len(self.a_6)} x {q_7:.1f} x {r_7:.1f} x {s_7:.1f} = {w_7:.2f} cm3")
    def i_6(self):
        p_7 = ["Verification du respect des stocks d'alliage", [], []]
        self.c_6.append(p_7)
        for e_7 in range(len(self.u_5.n_4)):
            if self.z_5[e_7] > self.u_5.n_4[e_7].c_3 + 1e-3:
                p_7[1].append(f"Le poids utilise de l'alliage {e_7} est de {self.z_5[e_7]:.3f} kg > {self.u_5.n_4[e_7].c_3:.3f} kg en stock")
    def j_6(self):
        p_7 = ["Verification de la composition de l'alliage demande par le client", [], []]
        self.c_6.append(p_7)
        t_6 = self.c_7()
        x_7 = sum(t_6)
        if x_7 < 1e-3:
            p_7[1].append(f"Le poids de metal fondu est trop faible pour calculer des pourcentages")
            return
        for g_7 in range(len(self.u_5.m_4)):
            y_7 = t_6[g_7]/x_7
            z_7 = self.u_5.m_4[g_7].x_2
            if y_7 < z_7[0] - 1e-3:
                p_7[1].append(f"Le pourcentage en poids obtenu du metal {g_7} est de {y_7*100:.1f} % inferieur a {100*z_7[0]:.1f} %")
            if y_7 > z_7[1] + 1e-3:
                p_7[1].append(f"Le pourcentage en poids obtenu du metal {g_7} est de {y_7*100:.1f} % superieur a {100*z_7[1]:.1f} %")
    def k_6(self):
        p_7 = ["Verification des chevauchements des plaques dans les toles", [], []]
        self.c_6.append(p_7)
        for a_8, n_3 in enumerate(self.a_6):
            b_8 = []
            for c_8 in n_3.e_5:
                (d_8, e_8) = c_8.p_3.t_1
                (f_8, g_8) = c_8.v_3().t_1
                b_8.append((d_8, f_8, e_8, g_8, c_8))
            b_8.sort(key=lambda h_8: h_8[0])
            n = len(b_8)
            for t_4 in range(n):
                i_8, j_8, k_8, l_8, m_8 = b_8[t_4]
                for n_8 in range(t_4 + 1, n):
                    o_8, p_8, q_8, r_8, s_8 = b_8[n_8]
                    if o_8 >= j_8 - 1e-3:
                        break
                    if max(k_8, q_8) < min(l_8, r_8) - 1e-3:
                        p_7[1].append(f"Tole {a_8}, {m_8.o_3.e_2} chevauche {s_8.o_3.e_2}")
                        m_8.n_2 = False
                        s_8.n_2 = False
    def l_6(self):
        p_7 = ["Verification des debordements des toles", [], []]
        self.c_6.append(p_7)
        for a_8, n_3 in enumerate(self.a_6):
            (t_8, u_8) = n_3.l_2
            for c_8 in n_3.e_5:
                (d_8, e_8) = c_8.p_3.t_1
                (f_8, g_8) = c_8.v_3().t_1
                if d_8 < -1e-3 or e_8 < -1e-3 or f_8 > t_8 + 1e-3 or g_8 > u_8 + 1e-3:
                    p_7[1].append(f"Tole {a_8}, {c_8.o_3.e_2} deborde de la tole de dimensions {t_8:.2f} x {u_8:.2f}")
                    c_8.n_2 = False
    def m_6(self):
        p_7 = ["Verification du nombre d'exemplaires de chaque plaque", [], []]
        self.c_6.append(p_7)
        e_5 = [r_5 for a_8 in self.a_6 for r_5 in a_8.e_5]
        for o_3 in self.u_5.i_4:
            v_8 = [_ for _ in e_5 if _.o_3 == o_3]
            if len(v_8) != o_3.f_2:
                p_7[1].append(f"Plaque {o_3.e_2}, {len(v_8)} fois dans les toles pour une demande de {o_3.f_2}")
    def n_6(self):
        p_7 = ["Verification da la perforation de tous les polygones de chaque plaque", [], []]
        self.c_6.append(p_7)
        for t_4, o_3 in enumerate(self.u_5.i_4):
            w_8 = [_[0] for _ in self.b_6[t_4].m_5]
            for p_5 in range(len(o_3.m_2)):
                x_8 = len([_ for _ in w_8 if _ == p_5])
                if x_8 != 1:
                    p_7[1].append(f"Plaque {o_3.e_2}, le polygone {p_5} est perfore {x_8} fois")
                    o_3.n_2 = False
def y_8(z_8: int, t_4: int, a_9: float, b_9: float):
    c_9 = t_4 / z_8  
    h_8, d_9, e_9 = colorsys.hls_to_rgb(c_9, b_9, a_9)
    return '#{:02x}{:02x}{:02x}'.format(int(h_8 * 255), int(d_9 * 255), int(e_9 * 255))
class F9:
    def __init__(self, t_5: W3, g_9: S5, h_4: str, h_9):
        self.u_5 = t_5
        self.i_9 = g_9
        self.j_9 = [y_8(8, _, 0.9, 0.6) for _ in range(20)]
        self.k_9 = [y_8(8, _, 0.5, 0.9) for _ in range(20)]
        self.l_9 = "#0095db"
        self.m_9 = n_9.Tk()
        self.m_9.title(f"Checker - Projet informatique 2026 - {self.u_5.p_2}")
        self.m_9.minsize(width=900, height=600)
        o_9 = ttk.Style(self.m_9)
        o_9.theme_use("default")
        o_9.configure("Black.TLabel", background="black", foreground="white", font=("Arial", 11, "bold"))
        self.p_9 = ttk.Notebook(self.m_9)
        self.q_9(h_4)
        self.r_9()
        self.s_9()
        if self.u_5.j_4[0]:
            self.t_9()
        self.p_9.pack(expand=1, fill='both')
        self.u_9(h_9)
        self.m_9.mainloop()
    def q_9(self, h_4: str):
        v_9 = ttk.Frame(self.p_9)
        self.p_9.add(v_9, text=" Log ")
        w_9 = ttk.Frame(v_9)
        w_9.pack(padx=5, pady=5, expand=True, fill="both")
        x_9 = n_9.Text(w_9, wrap="none")  
        x_9.insert("1.0", h_4)
        x_9.config(state="normal")  
        x_9.config(font=font.Font(family="Monospace", size=10))
        y_9 = ttk.Scrollbar(w_9, orient="vertical", command=x_9.yview)
        z_9 = ttk.Scrollbar(w_9, orient="horizontal", command=x_9.xview)
        x_9.config(yscrollcommand=y_9.set, xscrollcommand=z_9.set)
        x_9.grid(row=0, column=0, sticky="nsew")
        y_9.grid(row=0, column=1, sticky="ns")
        z_9.grid(row=1, column=0, sticky="ew")
        w_9.grid_rowconfigure(0, weight=1)  
        w_9.grid_columnconfigure(0, weight=1)  
        v_9.grid_rowconfigure(0, weight=1)
        v_9.grid_columnconfigure(0, weight=1)
    def r_9(self):
        v_9 = ttk.Frame(self.p_9)
        self.p_9.add(v_9, text=' Toles ')
        if not self.i_9.z_4:
            w_9 = n_9.Frame(v_9)
            w_9.pack(side="top", fill="both", expand=True)
            a_10 = n_9.Label(w_9, text=" Fournisseur non defini ", anchor="center")
            a_10.pack(side="top", fill="both", expand=True)
            return
        b_10 = n_9.Frame(v_9)
        b_10.pack(side="top", fill="x", padx=10, pady=5)
        n_9.Label(b_10, text="  Tole: ").pack(side="left")
        c_10 = ttk.Combobox(b_10, state="readonly", width=7)
        c_10.pack(side="left")
        n_9.Label(b_10, text="    ").pack(side="left")
        n_9.Label(b_10, text="  Plaque: ").pack(side="left")
        d_10 = ttk.Combobox(b_10, state="readonly", width=7)
        d_10.pack(side="left")
        c_10.bind("<<ComboboxSelected>>", lambda e_10: f_10())
        d_10.bind("<<ComboboxSelected>>", lambda e_10: f_10())
        g_10 = ttk.Frame(v_9)
        g_10.pack(fill="both", expand=True)
        g_10.columnconfigure(0, weight=1)  
        g_10.columnconfigure(1, weight=0)  
        g_10.rowconfigure(0, weight=1)  
        h_10 = ttk.Frame(g_10)
        h_10.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        h_10.rowconfigure(0, weight=1)
        h_10.columnconfigure(0, weight=1)
        i_10 = n_9.Canvas(h_10, bg="white")
        i_10.pack(side="left", fill="both", expand=True)
        i_10.bind("<Configure>", lambda e_10: j_10())
        k_10 = n_9.Scrollbar(h_10, orient="vertical", command=i_10.yview)
        k_10.pack(side="right", fill="y")
        i_10.configure(yscrollcommand=k_10.set)
        l_10 = ttk.Frame(g_10)
        l_10.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        m_10 = ["Fournisseur", "Dimensions", "Prix", "Utilisation", "Realisable"]
        n_10 = []
        for t_4, o_10 in enumerate(m_10):
            a_10 = ttk.Label(l_10, text=o_10 + " : ")
            a_10.grid(row=t_4 + 1, column=0, sticky="w", padx=0, pady=2)
            p_10 = ttk.Label(l_10, text="N/A")
            p_10.grid(row=t_4 + 1, column=1, sticky="w", padx=0, pady=2)
            n_10.append(p_10)
        q_10 = ttk.Frame(l_10)
        q_10.grid(row=len(m_10) + 1, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
        l_10.rowconfigure(len(m_10) + 1, weight=1)  
        q_10.columnconfigure(0, weight=1)  
        q_10.columnconfigure(1, weight=0)  
        r_10 = ["Tole", "Plaque", "x", "y", "dimx", "dimy"]
        s_10 = [40, 100, 60, 60, 60, 60]
        t_10: List[Literal["center", "e"]] = ["center", "center", "e", "e", "e", "e"]
        u_10 = ttk.Treeview(q_10, columns=r_10, show="headings")
        u_10.tag_configure("rouge", background=b_1)
        for t_4 in range(len(r_10)):
            u_10.heading(r_10[t_4], text=r_10[t_4])
            u_10.column(r_10[t_4], width=s_10[t_4], anchor=t_10[t_4])
        u_10.grid(row=0, column=0, sticky="nsew")
        u_10.columnconfigure(0, weight=1)
        v_10 = ttk.Scrollbar(q_10, orient="vertical", command=u_10.yview)
        u_10.configure(yscrollcommand=v_10.set)
        u_10.bind("<<TreeviewSelect>>", lambda e_10: j_10())
        u_10.grid(row=0, column=0, sticky="nsew")  
        v_10.grid(row=0, column=1, sticky="ns")  
        q_10.grid_rowconfigure(0, weight=1)  
        w_10 = []
        x_10 = []
        y_10 = []
        def j_10():
            nonlocal y_10
            z_10 = sorted(list({_[1] for _ in y_10}), key=lambda _: _.y_1)
            a_11 = u_10.selection()
            b_11 = u_10.index(u_10.selection()[0]) if a_11 else -10
            c_11 = 40
            d_11 = 10
            e_11 = 10
            f_11 = self.i_9.z_4.l_3[0]
            g_11 = max(1, i_10.winfo_width() - c_11 - d_11) / f_11
            h_11 = self.i_9.z_4.l_3[1]
            i_11 = max(1, i_10.winfo_height() - 2*d_11) / h_11
            j_11 = min(g_11, i_11)
            k_11 = (self.i_9.z_4.l_3[0] * j_11)
            l_11 = (self.i_9.z_4.l_3[1] * j_11)
            i_10.delete("all")
            m_11 = i_10.yview()
            n_11 = c_11 + d_11 + k_11
            o_11 = 2 * d_11 + len(z_10)*(l_11+e_11) - e_11
            i_10.create_rectangle(0, 0, n_11, o_11, outline="white")
            p_11 = None
            q_11 = float(c_11)
            r_11 = float(d_11 - e_11)
            s_11 = q_11 + k_11
            t_11 = r_11 - l_11
            u_11 = -1
            v_11 = None
            for w_11 in y_10:
                x_11 = w_11[0]
                y_11 = w_11[1]
                z_11 = w_11[2]
                if x_11:
                    u_11 += 1
                if y_11 != p_11:
                    r_11 += l_11 + e_11
                    t_11 = r_11 - l_11
                    p_11 = y_11
                    i_10.create_text(5, t_11 + 10, text=f"{y_11.y_1:4d} ", anchor="w", font=("Arial", 8))
                    i_10.create_rectangle(q_11, r_11, s_11, t_11, fill="grey75", outline="grey75")
                if z_11:
                    a_12 = self.u_5.i_4.index(z_11.o_3)
                    if x_11:
                        b_12 = self.j_9[a_12 % len(self.j_9)]
                        c_12 = "black"
                    else:
                        b_12 = self.k_9[a_12 % len(self.k_9)]
                        c_12 = "grey50"
                    d_8 = q_11 + (j_11 * z_11.p_3.t_1[0])
                    e_8 = r_11 - (j_11 * z_11.p_3.t_1[1])
                    f_8 = q_11 + (j_11 * z_11.v_3().t_1[0])
                    g_8 = r_11 - (j_11 * z_11.v_3().t_1[1])
                    d_8 = min(s_11, max(q_11, d_8))
                    e_8 = min(r_11, max(t_11, e_8))
                    f_8 = min(s_11, max(q_11, f_8))
                    g_8 = min(r_11, max(t_11, g_8))
                    i_10.create_rectangle(d_8, e_8, f_8, g_8, fill=b_12, outline=c_12)
                    if x_11 and u_11 == b_11:
                        v_11 = z_10.index(y_11)
                        d_12 = (d_8 + f_8) / 2
                        e_12 = (e_8 + g_8) / 2
                        h_8 = 5
                        i_10.create_oval(d_12 - h_8, e_12 - h_8, d_12 + h_8, e_12 + h_8, outline="black", fill="white")
            i_10.configure(scrollregion=i_10.bbox("all"))
            if v_11 is not None:
                n = len(z_10)
                f_12 = (i_10.winfo_height() / (l_11 + e_11)) - 2
                g_12 = max(0.0, min(v_11 / n, (n - f_12) / n))
                i_10.yview_moveto(g_12)
            else:
                i_10.yview_moveto(m_11[0])
        def f_10():
            nonlocal w_10, x_10, y_10
            h_12: B5 = w_10[c_10.current() - 1] if c_10.current() > 0 else None
            i_12: D2 = x_10[d_10.current() - 1] if d_10.current() > 0 else None
            if h_12:
                j_12 = [h_12]
            elif i_12:
                j_12 = [_ for _ in self.i_9.r_6 if _.h_5(i_12)]
            else:
                j_12 = [_ for _ in self.i_9.r_6]
            w_10 = sorted([_ for _ in self.i_9.r_6], key=lambda _: _.y_1)
            if i_12:
                w_10 = [_ for _ in w_10 if _.h_5(i_12)]
            x_10 = sorted([_ for _ in self.u_5.i_4], key=lambda _: _.e_2)
            if h_12:
                x_10 = [_ for _ in x_10 if h_12.h_5(_)]
            c_10['values'] = ["Toutes"] + [f"{_.y_1}" for _ in w_10]
            d_10['values'] = ["Toutes"] + [f"{_.e_2}" for _ in x_10]
            if c_10.current() == -1:
                c_10.set(c_10['values'][0])
            if d_10.current() == -1:
                d_10.set(d_10['values'][0])
            y_10 = []
            for n_3 in j_12:
                if not n_3.e_5:
                    x_11 = (h_12 is None)
                    y_10.append([x_11, n_3, None])
                else:
                    for r_5 in n_3.e_5:
                        x_11 = (i_12 is None or i_12 == r_5.o_3)
                        y_10.append([x_11, n_3, r_5])
            k_12 = 0
            n_10[k_12].config(text=f"{self.i_9.z_4.y_1}")
            k_12 += 1
            n_10[k_12].config(text=f"{self.i_9.z_4.l_3[0]:.1f} x {self.i_9.z_4.l_3[1]:.1f}")
            k_12 += 1
            n_10[k_12].config(text=f"{self.i_9.z_4.k_3:.1f}" + \
                                                  (" (estime)" if self.i_9.z_4.y_1 == 0 else ""))
            if h_12 is None:
                k_12 += 1
                n_10[k_12].config(text="-")
                k_12 += 1
                n_10[k_12].config(text="-")
            else:
                k_12 += 1
                n_10[k_12].config(text=f"{h_12.i_5()*100:.1f} %")
                k_12 += 1
                n_2 = len([_ for _ in h_12.e_5 if not _.n_2]) == 0
                n_10[k_12].config(text=("  oui  " if n_2 else "  non  "),
                                                 background=(a_1 if n_2 else b_1))
            for z_11 in u_10.get_children():
                u_10.delete(z_11)
            for l_12 in y_10:
                if l_12[0] and l_12[2]:
                    n_3 = l_12[1]
                    g_5 = l_12[2]
                    o_3 = g_5.o_3
                    d_8, e_8 = g_5.p_3.t_1
                    f_8, g_8 = g_5.v_3().t_1
                    t_2 = [n_3.y_1, o_3.e_2, f"{d_8:.2f}", f"{e_8:.2f}", f"{f_8-d_8:.2f}", f"{g_8-e_8:.2f}"]
                    u_10.insert("", "end", values=t_2,
                                        tags=["" if g_5.n_2 else "rouge",])
            j_10()
        f_10()
    def s_9(self):
        v_9 = ttk.Frame(self.p_9)
        self.p_9.add(v_9, text=' Laser ')
        g_10 = ttk.Frame(v_9)
        g_10.pack(fill="both", expand=True)
        g_10.columnconfigure(0, weight=1)  
        g_10.columnconfigure(1, weight=0)  
        g_10.rowconfigure(0, weight=1)  
        h_10 = ttk.Frame(g_10)
        h_10.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        h_10.rowconfigure(0, weight=1)
        h_10.columnconfigure(0, weight=1)
        i_10 = n_9.Canvas(h_10, bg="white")
        i_10.pack(side="left", fill="both", expand=True)
        i_10.bind("<Configure>", lambda e_10: j_10())
        l_10 = ttk.Frame(g_10)
        l_10.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        d_10 = ttk.Combobox(l_10, state="readonly")
        d_10['values'] = sorted([_.e_2 for _ in self.u_5.i_4])
        d_10.set(d_10['values'][0])
        a_10 = ttk.Label(l_10, text="Plaque" + " : ")
        a_10.grid(row=1, column=0, sticky="w", padx=0, pady=2)
        d_10.grid(row=1, column=1, sticky="w", padx=0, pady=2)
        d_10.bind("<<ComboboxSelected>>", lambda e_10: f_10())
        m_10 = ["Dimensions", "Nb polygones", "Nb exemplaires", "Longueur laser", "Realisable"]
        n_10 = []
        for t_4, o_10 in enumerate(m_10):
            a_10 = ttk.Label(l_10, text=o_10 + " : ")
            a_10.grid(row=t_4 + 2, column=0, sticky="w", padx=0, pady=2)
            p_10 = ttk.Label(l_10, text="N/A")
            p_10.grid(row=t_4 + 2, column=1, sticky="w", padx=0, pady=2)
            n_10.append(p_10)
        q_10 = ttk.Frame(l_10)
        q_10.grid(row=len(m_10) + 2, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
        l_10.rowconfigure(len(m_10) + 2, weight=1)  
        q_10.columnconfigure(0, weight=1)  
        q_10.columnconfigure(1, weight=0)  
        r_10 = ["poly", "pt", "x", "y", "dist"]
        s_10 = [40, 40, 60, 60, 60]
        t_10: List[Literal["center", "e"]] = ["center", "center", "e", "e", "e"]
        u_10 = ttk.Treeview(q_10, columns=r_10, show="headings")
        u_10.tag_configure("origine", background="#dddddd")
        for t_4 in range(len(r_10)):
            u_10.heading(r_10[t_4], text=r_10[t_4])
            u_10.column(r_10[t_4], width=s_10[t_4], anchor=t_10[t_4])
        u_10.grid(row=0, column=0, sticky="nsew")
        u_10.columnconfigure(0, weight=1)
        v_10 = ttk.Scrollbar(q_10, orient="vertical", command=u_10.yview)
        u_10.configure(yscrollcommand=v_10.set)
        u_10.bind("<<TreeviewSelect>>", lambda e_10: j_10())
        u_10.grid(row=0, column=0, sticky="nsew")  
        v_10.grid(row=0, column=1, sticky="ns")  
        q_10.grid_rowconfigure(0, weight=1)  
        m_12 = ttk.Frame(l_10)
        m_12.grid(row=len(m_10) + 3, column=0, columnspan=2, padx=5, pady=5, sticky="w")
        a_10 = ttk.Label(m_12, text="Affichage" + " : ")
        a_10.grid(row=0, column=0, sticky="w", padx=0, pady=2)
        n_12 = n_9.BooleanVar(value=True)  
        o_12 = n_9.BooleanVar(value=True)  
        p_12 = ttk.Checkbutton(m_12, text="Plaque", variable=n_12, command=lambda: j_10())
        p_12.grid(row=0, column=1, padx=5, pady=2)
        q_12 = ttk.Checkbutton(m_12, text="Laser", variable=o_12, command=lambda: j_10())
        q_12.grid(row=0, column=2, padx=5, pady=2)
        def j_10():
            r_12 = "#ffee00"
            o_3: D2 = next(_ for _ in self.u_5.i_4 if _.e_2 == d_10.get())
            a_7: K5 = self.i_9.s_6[self.u_5.i_4.index(o_3)]
            a_11 = u_10.selection()
            b_11 = u_10.index(u_10.selection()[0]) if a_11 else len(a_7.m_5)+1
            d_11 = 10
            f_11 = o_3.l_2[0]
            g_11 = max(1, i_10.winfo_width() - 2 * d_11) / f_11
            h_11 = o_3.l_2[1]
            i_11 = max(1, i_10.winfo_height() - 2 * d_11) / h_11
            j_11 = min(g_11, i_11)
            k_11 = (o_3.l_2[0] * j_11)
            l_11 = (o_3.l_2[1] * j_11)
            i_10.delete("all")
            n_11 = k_11 + 2 * d_11
            o_11 = l_11 + 2 * d_11
            i_10.create_rectangle(0, 0, n_11, o_11, outline="white")
            q_11 = d_11
            r_11 = d_11 + l_11
            if n_12.get():
                i_10.create_rectangle(q_11, r_11, q_11 + k_11, r_11 - l_11, fill=r_12, outline="black")
                s_12 = [False] * len(o_3.m_2)
                for t_12 in range(min(b_11, len(a_7.m_5))):
                    s_12[a_7.m_5[t_12][0]] = True
                for t_12, u_12 in enumerate(o_3.m_2):
                    v_12 = [(q_11 + j_11 * p_3.t_1[0], r_11 - j_11 * p_3.t_1[1]) for p_3 in u_12.c_2]
                    if s_12[t_12]:
                        w_12 = "white" if o_3.e_2[0:min(6,len(o_3.e_2))] != "qrcode" else "black"
                        i_10.create_polygon(v_12, fill=w_12, outline="black", width=1)
                    else:
                        i_10.create_polygon(v_12, fill="", outline="#bbbbbb", width=1)
            if o_12.get():
                i_10.create_rectangle(q_11 - 5, r_11 - 5, q_11 + 5, r_11 + 5, fill="green", outline="green")
                x_12 = [q_11, r_11]
                for y_12 in range(min(b_11, len(a_7.m_5))):
                    [t_12, q_5] = a_7.m_5[y_12]
                    r_5 = o_3.m_2[t_12].c_2[q_5]
                    x_12 += [q_11 + j_11 * r_5.t_1[0], r_11 - j_11 * r_5.t_1[1]]
                if b_11 > len(a_7.m_5):
                    x_12 += [q_11, r_11]
                if len(x_12) > 2:
                    i_10.create_line(x_12, fill="red", width=3)
                h_8 = 5
                d_12, e_12 = x_12[len(x_12) - 2:]
                i_10.create_oval(d_12 - h_8, e_12 - h_8, d_12 + h_8, e_12 + h_8, outline="red", fill="red")
        def f_10():
            o_3: D2 = next(_ for _ in self.u_5.i_4 if _.e_2 == d_10.get())
            a_7: K5 = self.i_9.s_6[self.u_5.i_4.index(o_3)]
            k_12 = 0
            n_10[k_12].config(text=f"{o_3.l_2[0]:.1f} x {o_3.l_2[1]:.1f}")
            k_12 += 1
            n_10[k_12].config(text=f"{len(o_3.m_2)}")
            k_12 += 1
            n_10[k_12].config(text=f"{o_3.f_2}")
            k_12 += 1
            n_10[k_12].config(text=f"{a_7.u_1():.2f}")
            k_12 += 1
            n_2 = o_3.n_2
            n_10[k_12].config(text=("  oui  " if n_2 else "  non  "),
                                             background=(a_1 if n_2 else b_1))
            for z_11 in u_10.get_children():
                u_10.delete(z_11)
            z_12 = 0
            a_13 = P1(0,0)
            t_2 = ["", "", f"{a_13.t_1[0]:.2f}", f"{a_13.t_1[1]:.2f}", f"{z_12:.2f}"]
            u_10.insert("", "end", values=t_2, tags=["origine",])
            for [t_12, q_5] in a_7.m_5:
                p_3 = o_3.m_2[t_12].c_2[q_5]
                z_12 += a_13.u_1(p_3)
                t_2 = [str(t_12), str(q_5), f"{p_3.t_1[0]:.2f}", f"{p_3.t_1[1]:.2f}", f"{z_12:.2f}"]
                u_10.insert("", "end", values=t_2)
                a_13 = p_3
            p_3 = P1(0,0)
            z_12 += a_13.u_1(p_3)
            t_2 = ["", "", f"{p_3.t_1[0]:.2f}", f"{p_3.t_1[1]:.2f}", f"{z_12:.2f}"]
            u_10.insert("", "end", values=t_2, tags=["origine",])
            j_10()
        f_10()
    def t_9(self):
        v_9 = ttk.Frame(self.p_9)
        self.p_9.add(v_9, text=' Fonderie ')
        ttk.Label(v_9, text=" Informations sur les metaux  ", style="Black.TLabel").pack(side="top", anchor="w", padx=5)
        w_9 = ttk.Frame(v_9)
        w_9.pack(padx=5, pady=5, expand=False, fill="x")
        r_10 = ["Metal"] + [f"M{g_7+1}" for g_7 in range(len(self.u_5.m_4))] + [""]
        s_10 = [100] + [40 for _ in self.u_5.m_4] + [100]
        u_10 = ttk.Treeview(w_9, columns=r_10, show="headings", height=4)
        for t_4 in range(len(r_10)):
            u_10.heading(r_10[t_4], text=r_10[t_4])
            u_10.column(r_10[t_4], width=s_10[t_4], anchor="e" if t_4 > 0 else "w")
        u_10.pack(fill="x")
        t_2 = ["Prix (euros/kg)"] + [f"{g_7.v_2:.3f}" for g_7 in self.u_5.m_4] + [""]
        u_10.insert("", "end", values=t_2)
        t_2 = ["Masse volumique (g/cm3)"] + [f"{g_7.w_2:.3f}" for g_7 in self.u_5.m_4] + [""]
        u_10.insert("", "end", values=t_2)
        t_2 = ["% min client"] + [f"{100*g_7.x_2[0]:.1f}%" for g_7 in self.u_5.m_4] + [""]
        u_10.insert("", "end", values=t_2)
        t_2 = ["% max client"] + [f"{100*g_7.x_2[1]:.1f}%" for g_7 in self.u_5.m_4] + [""]
        u_10.insert("", "end", values=t_2)
        ttk.Label(v_9, text=" Informations sur les alliages en stock  (% en poids)", style="Black.TLabel").pack(side="top", anchor="w", padx=5)
        w_9 = ttk.Frame(v_9)
        w_9.pack(padx=5, pady=5, expand=False, fill="x")
        r_10 = ["Metal"] + [f"M{g_7+1}" for g_7 in range(len(self.u_5.m_4))] + ["Stock (kg)"]
        s_10 = [100] + [40 for _ in self.u_5.m_4] + [100]
        u_10 = ttk.Treeview(w_9, columns=r_10, show="headings", height=len(self.u_5.n_4))
        for t_4 in range(len(r_10)):
            u_10.heading(r_10[t_4], text=r_10[t_4])
            u_10.column(r_10[t_4], width=s_10[t_4], anchor="e" if t_4 > 0 else "w")
        u_10.pack(fill="x")
        for e_7, f_7 in enumerate(self.u_5.n_4):
            t_2 = [f"Alliage {e_7+1}"] + [f"{100*f_7.x_2[g_7]:.1f}%" for g_7 in range(len(self.u_5.m_4))] + [f"{f_7.c_3:.3f}"]
            u_10.insert("", "end", values=t_2)
        d_7 = self.i_9.c_7()
        i_7 = self.i_9.h_7()
        x_7 = sum(d_7)
        b_13 = sum(i_7)
        ttk.Label(v_9, text=" Production des toles  ", style="Black.TLabel").pack(side="top", anchor="w", padx=5)
        w_9 = ttk.Frame(v_9)
        w_9.pack(padx=5, pady=5, expand=False, fill="x")
        r_10 = ["Metal"] + [f"M{g_7+1}" for g_7 in range(len(self.u_5.m_4))] + ["Poids (kg)"]
        s_10 = [100] + [40 for _ in self.u_5.m_4] + [100]
        u_10 = ttk.Treeview(w_9, columns=r_10, show="headings", height=len(self.u_5.n_4)+4)
        for t_4 in range(len(r_10)):
            u_10.heading(r_10[t_4], text=r_10[t_4])
            u_10.column(r_10[t_4], width=s_10[t_4], anchor="e" if t_4 > 0 else "w")
        u_10.pack(fill="x")
        t_2 = ["Achat metaux (kg)"] + [f"{self.i_9.t_6[g_7]:.3f}" for g_7 in range(len(self.u_5.m_4))] + [""]
        u_10.insert("", "end", values=t_2)
        for e_7, f_7 in enumerate(self.u_5.n_4):
            t_2 = [f"Alliage {e_7+1} (kg)"] + [f"{f_7.x_2[g_7]*self.i_9.u_6[e_7]:.3f}" for g_7 in range(len(self.u_5.m_4))] + \
                    [f"{self.i_9.u_6[e_7]:.3f}"]
            u_10.insert("", "end", values=t_2)
        t_2 = [f"Total (kg)"] + [f"{d_7[g_7]:.3f}" for g_7 in range(len(self.u_5.m_4))] + \
                [f"{x_7:.3f}"]
        u_10.insert("", "end", values=t_2)
        if x_7 < 1e-5:
            t_2 = [f"Total (% du poids)"] + [f"-" for _ in range(len(self.u_5.m_4))] + [""]
        else:
            t_2 = [f"Total (% du poids)"] + [f"{100*d_7[g_7]/x_7:.1f}%" for g_7 in range(len(self.u_5.m_4))] + \
                    [""]
        u_10.insert("", "end", values=t_2)
        t_2 = [f"Total (cm3)"] + [f"{i_7[g_7]:.2f}" for g_7 in range(len(self.u_5.m_4))] + \
                [f"{b_13:.2f}"]
        u_10.insert("", "end", values=t_2)
        q_7 = self.u_5.j_4[0].l_3[0]
        r_7 = self.u_5.j_4[0].l_3[1]
        s_7 = self.u_5.k_4
        c_13 = q_7 * r_7 * s_7
        u_7 = 0.001
        v_7 = int(floor(u_7 + b_13/(q_7*r_7*s_7)))
        d_13 = max(0, b_13 - v_7 * c_13)
        ttk.Label(w_9, text=f"Volume d'une tole : {q_7:.1f} x {r_7:.1f} x {s_7:.1f} = {c_13:.2f} cm3").pack(side="top", anchor="w", padx=5)
        ttk.Label(w_9, text=f"Nombre de toles obtenues : floor({b_13:.2f} / {c_13:.2f} + eps) = {v_7}   avec eps={u_7}").pack(side="top", anchor="w", padx=5)
        ttk.Label(w_9, text=f"Volume fondu non utilise : {d_13:.2f} cm3").pack(side="top", anchor="w", padx=5)
    def u_9(self, h_9):
        w_9 = ttk.Frame(self.m_9)
        w_9.pack(fill="x", padx=10, pady=5)
        e_13 = ttk.Label(w_9, text=h_9)
        e_13.pack(side="left", padx=5)
        ttk.Label(w_9, text=" ").pack(side="left", padx=10)
        ttk.Label(w_9, text=self.u_5.p_2).pack(side="left", padx=10)
        ttk.Label(w_9, text=" ").pack(side="left", padx=10)
        f_13 = ttk.Label(w_9)
        if self.i_9.n_2:
            f_13.config(text=" realisable ", background="dark green", foreground="white")
        else:
            f_13.config(text=" non realisable ", background="red", foreground="white")
        f_13.pack(side="left", padx=5)
        ttk.Label(w_9, text=" ").pack(side="left", padx=100)
        g_13 = ttk.Button(w_9, text="Quitter", command=self.m_9.destroy)
        g_13.pack(side="right", padx=5)
class H13:
    def __init__(self):
        self.i_13 = datetime.now().strftime("%d/%m/%Y a %H:%M")
        self.j_13 = 10
        self.k_13 = True
        self.l_13 = 60
        self.m_13 = -1
        self.n_13 = ""
        self.o_13 = 0
        self.x_3 = ""
        self.u_5 = None
        self.i_9 = None
    @property
    def p_2(self):
        return self.x_3
    @property
    def g_1(self):
        return self.l_13
    def p_13(self, q_13, r_13):
        s_13 = lambda t_13: t_13.lower() in ["true", "oui", "yes"]
        q_13 = q_13.strip().upper()
        r_13 = r_13.strip()
        if q_13 == "INSTANCE":
            self.x_3 = r_13
        elif q_13 == "VISUALISER":
            self.k_13 = s_13(r_13)
        elif q_13 == "TIME_MAX":
            self.l_13 = j_1(r_13, "pour la valeur de TIME_MAX dans CONFIG", False, 60)
        elif q_13 == "LEVEL_PRINT":
            self.j_13 = j_1(r_13, "pour la valeur de LEVEL_PRINT dans CONFIG", False, 10)
    def run(self):
        if self.j_13:
            print("Checker - Projet informatique 2026 - GI")
            print("Auteur : Olivier.Briant@grenoble-inp.fr")
        self.n_13 += f"Checker lance sur l'instance {self.x_3} le {self.i_13}\n"
        self.n_13 += f"Probleme resolu en  {self.m_13:.2f} secondes\n\n"
        self.u_5 = W3(self.x_3)
        self.n_13 += self.u_5.g_4() + "\n"
        self.i_9 = S5(self.u_5)
        self.n_13 += self.i_9.h_4()
        if self.j_13 > 2:
            print(f"Ecriture de {self.u_5.p_2}_log.txt")
        with open(f"{self.u_5.p_2}_log.txt", "w") as r_2:
            r_2.write(self.n_13)
        if self.k_13: F9(self.u_5, self.i_9, self.n_13, self.i_13)
def run():
    u_13: H13 = H13()
    if len(sys.argv) > 1:
        v_13 = ['INSTANCE', 'TIMEMAX', 'VISUALISER']
        for t_4 in range(1, len(sys.argv)):
            u_13.p_13(v_13[t_4 - 1], sys.argv[t_4])
    elif os.path.exists("CONFIG"):
        with open("CONFIG", "r") as w_13:
            for x_13 in w_13.readlines():
                if '=' not in x_13: continue
                (y_13, z_13) = x_13.split("=")
                u_13.p_13(y_13, z_13)
    if not u_13.p_2:
        print("Aucune instance definie")
        exit(1)
    if os.path.exists(f"{u_13.p_2}_sol.txt"):
        os.remove(f"{u_13.p_2}_sol.txt")
    a_14 = d_1(resoudre, f_1=(u_13.p_2,), g_1=u_13.g_1 + 1)
    if a_14 != inf:
        u_13.m_13 =a_14
    u_13.run()
if __name__ == "__main__":
    run()
