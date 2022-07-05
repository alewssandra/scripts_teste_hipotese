import numpy as np
import scipy.stats as st
from scipy.stats import t as t_student

"""
    Conhecido = tem valor de variancia (sigma^2)
    Desconhecido = não tem valor de variancia (sigma^2)

    Desvio padrão = sigma
    Variancia = sigma^2

    !!Todas as funções recebem o valor do Desvio padrão e não da variancia!!


    != : Bilateral
    <  : Esquerda
    >  : Direita
"""

def bilateral_media_populacao_normal_conhecido(m, s, n, x, alpha):  
    z = (x - m) / np.sqrt((s**2) / n)

    z1 = st.norm.ppf(((100-(alpha/2))/100), loc=0, scale=1)
    z2 = st.norm.ppf(1-((100-(alpha/2))/100), loc=0, scale=1)

    print("{} < z:{} < {}".format(z2, z, z1))

    if z > z2 and z < z1:
        print("Decide-se não rejeitar a hipótese inicial pois tcalc pertence à RNR")
    else:
        print("Decide-se rejeitar a hipótese inicial pois tcalc pertence à RC")

def esquerda_media_populacao_normal_conhecido(m, s, n, x, alpha):
    z = (x - m) / np.sqrt((s**2) / n)

    z2 = st.norm.ppf(1-((100-(alpha))/100), loc=0, scale=1)

    print("z:{} > {}".format(z, z2))

    if z > z2 :
        print("Decide-se não rejeitar a hipótese inicial pois tcalc pertence à RNR")
    else:
        print("Decide-se rejeitar a hipótese inicial pois tcalc pertence à RC")

def direita_media_populacao_normal_conhecido(m, s, n, x, alpha):
    z = (x - m) / np.sqrt((s**2) / n)
            
    z1 = st.norm.ppf(((100-(alpha))/100), loc=0, scale=1)

    print("z:{} < {}".format(z, z1))

    if z < z1:
        print("Decide-se não rejeitar a hipótese inicial pois tcalc pertence à RNR")
    else:
        print("Decide-se rejeitar a hipótese inicial pois tcalc pertence à RC")


def bilateral_media_populacao_normal_desconhecido(m, s, n, x, alpha):
    z = (x - m) / np.sqrt((s**2) / n)
    phi = n - 1

    z1 = t_student.ppf(1 - ((alpha/100)) / 4, phi)
    z2 = t_student.ppf((alpha/100) / 4, phi)

    print("{} < z:{} < {}".format(z2, z, z1))

    if z > z2 and z < z1:
        print("Decide-se não rejeitar a hipótese inicial pois tcalc pertence à RNR")
    else:
        print("Decide-se rejeitar a hipótese inicial pois tcalc pertence à RC")

def esquerda_media_populacao_normal_desconhecido(m, s, n, x, alpha):
    z = (x - m) / np.sqrt((s**2) / n)
    phi = n - 1
    
    z2 = t_student.ppf((alpha/100), phi)

    print("z:{} > {}".format(z, z2))

    if z > z2:
        print("Decide-se não rejeitar a hipótese inicial pois tcalc pertence à RNR")
    else:
        print("Decide-se rejeitar a hipótese inicial pois tcalc pertence à RC")

def direita_media_populacao_normal_desconhecido(m, s, n, x, alpha):
    z = (x - m) / np.sqrt((s**2) / n)
    phi = n - 1
    
    z1 = t_student.ppf(1 - ((alpha/100)), phi)

    print("z:{} < {}".format(z, z1))

    if z < z1:
        print("Decide-se não rejeitar a hipótese inicial pois tcalc pertence à RNR")
    else:
        print("Decide-se rejeitar a hipótese inicial pois tcalc pertence à RC")


def bilateral_proprocao_populacao_normal(p, p0, q0, n, alpha):
    z = (p0 - p) / np.sqrt((p0 * q0) / n)

    z1 = st.norm.ppf(((100-(alpha/2))/100), loc=0, scale=1)
    z2 = st.norm.ppf(1-((100-(alpha/2))/100), loc=0, scale=1)

    print("{} < z:{} < {}".format(z2, z, z1))

    if z > z2 and z < z1:
        print("Decide-se não rejeitar a hipótese inicial pois tcalc pertence à RNR")
    else:
        print("Decide-se rejeitar a hipótese inicial pois tcalc pertence à RC")

def esquerda_proprocao_populacao_normal(p, p0, q0, n, alpha):
    z = (p0 - p) / np.sqrt((p0 * q0) / n)

    z2 = st.norm.ppf(1-((100-(alpha))/100), loc=0, scale=1)

    print("z:{} > {}".format(z, z2))

    if z > z2 :
        print("Decide-se não rejeitar a hipótese inicial pois tcalc pertence à RNR")
    else:
        print("Decide-se rejeitar a hipótese inicial pois tcalc pertence à RC")

def direita_proprocao_populacao_normal(p, p0, q0, n, alpha):
    z = (p0 - p) / np.sqrt((p0 * q0) / n)

    z1 = st.norm.ppf(((100-(alpha))/100), loc=0, scale=1)

    print("z:{} < {}".format(z, z1))

    if z < z1:
        print("Decide-se não rejeitar a hipótese inicial pois tcalc pertence à RNR")
    else:
        print("Decide-se rejeitar a hipótese inicial pois tcalc pertence à RC")


def bilateral_diferenca_media(m, s, n, d, alpha):
    z = (d - m) / np.sqrt((s**2) / 10)
    phi = n - 1

    z1 = t_student.ppf(1 - ((alpha/100)) / 4, phi)
    z2 = t_student.ppf((alpha/100) / 4, phi)

    print("{} < z:{} < {}".format(z2, z, z1))

    if z > z2 and z < z1:
        print("Decide-se não rejeitar a hipótese inicial pois tcalc pertence à RNR")
    else:
        print("Decide-se rejeitar a hipótese inicial pois tcalc pertence à RC")

def esquerda_diferenca_media(m, s, n, d, alpha):
    z = (d - m) / np.sqrt((s**2) / 10)

    phi = n - 1

    z2 = t_student.ppf((alpha/100), phi)

    print("z:{} > {}".format(z, z2))

    if z > z2:
        print("Decide-se não rejeitar a hipótese inicial pois tcalc pertence à RNR")
    else:
        print("Decide-se rejeitar a hipótese inicial pois tcalc pertence à RC")

def direita_diferenca_media(m, s, n, d, alpha):
    z = (d - m) / np.sqrt((s**2) / 10)
    phi = n - 1

    z1 = t_student.ppf(1 - ((alpha/100)), phi)

    print("z:{} < {}".format(z, z1))

    if z < z1:
        print("Decide-se não rejeitar a hipótese inicial pois tcalc pertence à RNR")
    else:
        print("Decide-se rejeitar a hipótese inicial pois tcalc pertence à RC")


def bilateral_variancia_media_conhecido(s_2, x, n, alpha):
    z = x / s_2

    z1 = st.chi2.ppf(((100-(alpha/2))/100), n)
    z2 = st.chi2.ppf(1-((100-(alpha/2))/100), n)

    print("{} < z:{} < {}".format(z2, z, z1))

    if z > z2 and z < z1:
        print("Decide-se não rejeitar a hipótese inicial pois tcalc pertence à RNR")
    else:
        print("Decide-se rejeitar a hipótese inicial pois tcalc pertence à RC")

def esquerda_variancia_media_conhecido(s_2, x, n, alpha):
    z = x / s_2

    z2 = st.chi2.ppf(1-((100-alpha)/100), n)

    print("z:{} > {}".format(z, z2))

    if z > z2 :
        print("Decide-se não rejeitar a hipótese inicial pois tcalc pertence à RNR")
    else:
        print("Decide-se rejeitar a hipótese inicial pois tcalc pertence à RC")

def direita_variancia_media_conhecido(s_2, x, n, alpha):
    z = x / s_2

    z1 = st.chi2.ppf(((100-(alpha))/100), n)

    print("z:{} < {}".format(z, z1))

    if z < z1:
        print("Decide-se não rejeitar a hipótese inicial pois tcalc pertence à RNR")
    else:
        print("Decide-se rejeitar a hipótese inicial pois tcalc pertence à RC")


def bilateral_variancia_media_desconhecido(s_2, x, n, alpha):
    z = x / s_2

    z1 = st.chi2.ppf(((100-(alpha/2))/100), n-1)
    z2 = st.chi2.ppf(1-((100-(alpha/2))/100), n-1)

    print("{} < z:{} < {}".format(z2, z, z1))

    if z > z2 and z < z1:
        print("Decide-se não rejeitar a hipótese inicial pois tcalc pertence à RNR")
    else:
        print("Decide-se rejeitar a hipótese inicial pois tcalc pertence à RC")

def esquerda_variancia_media_desconhecido(s_2, x, n, alpha):
    z = x / s_2

    z2 = st.chi2.ppf(1-((100-alpha)/100), n-1)

    print("z:{} > {}".format(z, z2))

    if z > z2 :
        print("Decide-se não rejeitar a hipótese inicial pois tcalc pertence à RNR")
    else:
        print("Decide-se rejeitar a hipótese inicial pois tcalc pertence à RC")

def direita_variancia_media_desconhecido(s_2, x, n, alpha):
    z = x / s_2

    z1 = st.chi2.ppf(((100-(alpha))/100), n-1)

    print("z:{} < {}".format(z, z1))

    if z < z1:
        print("Decide-se não rejeitar a hipótese inicial pois tcalc pertence à RNR")
    else:
        print("Decide-se rejeitar a hipótese inicial pois tcalc pertence à RC")