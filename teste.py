from cmath import sqrt
import statistics
import numpy as np
import math
import scipy.stats as st
from scipy.stats import t as t_student

def bilateral_conhecido(m, s, n, x, alpha):  
    z = (x - m) / np.sqrt((s**2) / n)

    print(z)

    z1 = st.norm.ppf(((100-(alpha/2))/100), loc=0, scale=1)
    z2 = st.norm.ppf(1-((100-(alpha/2))/100), loc=0, scale=1)

    if z > z2 and z < z1:
        print("Decide-se não rejeitar a hipótese inicial pois tcalc pertence à RNR")
    else:
        print("Decide-se rejeitar a hipótese inicial pois tcalc pertence à RC")

def esquerda_conhecido(m, s, n, x, alpha):
    z = (x - m) / np.sqrt((s**2) / n)

    print(z)

    z2 = st.norm.ppf(1-((100-(alpha))/100), loc=0, scale=1)

    if z > z2 :
        print("Decide-se não rejeitar a hipótese inicial pois tcalc pertence à RNR")
    else:
        print("Decide-se rejeitar a hipótese inicial pois tcalc pertence à RC")

def direita_conhecido(m, s, n, x, alpha):
    z = (x - m) / np.sqrt((s**2) / n)
    
    print(z)
        
    z1 = st.norm.ppf(((100-(alpha))/100), loc=0, scale=1)

    if z < z1:
        print("Decide-se não rejeitar a hipótese inicial pois tcalc pertence à RNR")
    else:
        print("Decide-se rejeitar a hipótese inicial pois tcalc pertence à RC")


def bilateral_desconhecido(m, s, n, x, alpha):
    z = (x - m) / np.sqrt((s**2) / n)
    phi = n - 1

    print(z)

    z1 = t_student.ppf(1 - ((alpha/100)) / 4, phi)
    z2 = t_student.ppf((alpha/100) / 4, phi)

    if z > z2 and z < z1:
        print("Decide-se não rejeitar a hipótese inicial pois tcalc pertence à RNR")
    else:
        print("Decide-se rejeitar a hipótese inicial pois tcalc pertence à RC")

def esquerda_desconhecido(m, s, n, x, alpha):
    z = (x - m) / np.sqrt((s**2) / n)
    phi = n - 1
    
    print(z)

    z2 = t_student.ppf((alpha/100), phi)

    if z > z2:
        print("Decide-se não rejeitar a hipótese inicial pois tcalc pertence à RNR")
    else:
        print("Decide-se rejeitar a hipótese inicial pois tcalc pertence à RC")

def direita_desconhecido(m, s, n, x, alpha):
    z = (x - m) / np.sqrt((s**2) / n)
    phi = n - 1

    print(z)
    
    z1 = t_student.ppf(1 - ((alpha/100)), phi)

    if z < z1:
        print("Decide-se não rejeitar a hipótese inicial pois tcalc pertence à RNR")
    else:
        print("Decide-se rejeitar a hipótese inicial pois tcalc pertence à RC")


def bilateral_proprocao_normal(p, p0, q0, n, alpha):
    z = (p0 - p) / np.sqrt((p0 * q0) / n)

    print(z)

    z1 = st.norm.ppf(((100-(alpha/2))/100), loc=0, scale=1)
    z2 = st.norm.ppf(1-((100-(alpha/2))/100), loc=0, scale=1)

    if z > z2 and z < z1:
        print("Decide-se não rejeitar a hipótese inicial pois tcalc pertence à RNR")
    else:
        print("Decide-se rejeitar a hipótese inicial pois tcalc pertence à RC")

def esquerda_proprocao_normal(p, p0, q0, n, alpha):
    z = (p0 - p) / np.sqrt((p0 * q0) / n)

    print(z)

    z2 = st.norm.ppf(1-((100-(alpha))/100), loc=0, scale=1)

    if z > z2 :
        print("Decide-se não rejeitar a hipótese inicial pois tcalc pertence à RNR")
    else:
        print("Decide-se rejeitar a hipótese inicial pois tcalc pertence à RC")

def direita_proprocao_normal(p, p0, q0, n, alpha):
    z = (p0 - p) / np.sqrt((p0 * q0) / n)

    print(z)

    z1 = st.norm.ppf(((100-(alpha))/100), loc=0, scale=1)

    print(z1)

    if z < z1:
        print("Decide-se não rejeitar a hipótese inicial pois tcalc pertence à RNR")
    else:
        print("Decide-se rejeitar a hipótese inicial pois tcalc pertence à RC")


def bilateral_diferenca_media(m, s, n, d, alpha):
    z = (d - m) / np.sqrt((s**2) / 10)
    phi = n - 1

    print(z)

    z1 = t_student.ppf(1 - ((alpha/100)) / 4, phi)
    z2 = t_student.ppf((alpha/100) / 4, phi)

    if z > z2 and z < z1:
        print("Decide-se não rejeitar a hipótese inicial pois tcalc pertence à RNR")
    else:
        print("Decide-se rejeitar a hipótese inicial pois tcalc pertence à RC")

def esquerda_diferenca_media(m, s, n, d, alpha):
    z = (d - m) / np.sqrt((s**2) / 10)

    phi = n - 1

    print(z)

    z2 = t_student.ppf((alpha/100), phi)

    if z > z2:
        print("Decide-se não rejeitar a hipótese inicial pois tcalc pertence à RNR")
    else:
        print("Decide-se rejeitar a hipótese inicial pois tcalc pertence à RC")

def direita_diferenca_media(m, s, n, d, alpha):
    z = (d - m) / np.sqrt((s**2) / 10)
    phi = n - 1

    print(z)

    z1 = t_student.ppf(1 - ((alpha/100)), phi)

    if z < z1:
        print("Decide-se não rejeitar a hipótese inicial pois tcalc pertence à RNR")
    else:
        print("Decide-se rejeitar a hipótese inicial pois tcalc pertence à RC")
