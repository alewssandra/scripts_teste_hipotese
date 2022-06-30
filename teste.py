import statistics
import numpy as np
import math
import scipy.stats as st
from scipy.stats import t as t_student

# Se vc não conhecer a média use n-1 nos graus de lib
def teste_chi_bilateral(h0,graus,var,alpha):
    chicalc=graus*var/h0
    print("qui_quad_calc",chicalc)

    X1=st.chi2.ppf((alpha/100)/2,graus)
    X2=st.chi2.ppf(1-(alpha/100)/2,graus)
    print("O valor do qui1 é:",X1, "O valor de qui2 é:", X2)

    if chicalc>X1 and chicalc<X2:
        print("Decide-se não rejeitar a hipótese inicial pois tcalc pertence à RNR")
    else:
        print("Decide-se rejeitar a hipótese inicial pois tcalc pertence à RC")

def teste_chi_esquerda(h0,graus,var,alpha):
    chicalc=graus*var/h0
    print("qui_quad_calc",chicalc)

    X=st.chi2.ppf(alpha/100,graus)
    
    print("O valor do qui_quadrado é:",X)

    if chicalc > X:
        print("Decide-se não rejeitar a hipótese inicial pois tcalc pertence à RNR")
    else:
        print("Decide-se rejeitar a hipótese inicial pois tcalc pertence à RC")


def teste_chi_direita(h0,graus,var,alpha):
    chicalc=graus*var/h0
    print("qui_quad_calc",chicalc)

    X=st.chi2.ppf(1-alpha/100,graus)

    print("O valor do qui_quadrado é:",X)

    if chicalc <X:
        print("Decide-se não rejeitar a hipótese inicial pois tcalc pertence à RNR")
    else:
     print("Decide-se rejeitar a hipótese inicial pois tcalc pertence à RC")



def bilateral(m, s_2, n, x, alpha, z_cacl_func):
    z_cale = z_cacl_func(m, s_2, n, x, alpha)
    
    z1 = st.norm.ppf(((100-(alpha/2))/100), loc=0, scale=1)
    z2 = st.norm.ppf(1-((100-(alpha/2))/100), loc=0, scale=1)

    if z_cale > z2 and z_cale < z1:
        print("Decide-se não rejeitar a hipótese inicial pois tcalc pertence à RNR")
    else:
        print("Decide-se rejeitar a hipótese inicial pois tcalc pertence à RC")

def esquerda(m, s_2, n, x, alpha, z_cacl_func):
    z_cale = z_cacl_func(m, s_2, n, x, alpha)
    
    z2 = st.norm.ppf(1-((100-(alpha))/100), loc=0, scale=1)

    if z_cale > z2 :
        print("Decide-se não rejeitar a hipótese inicial pois tcalc pertence à RNR")
    else:
        print("Decide-se rejeitar a hipótese inicial pois tcalc pertence à RC")

def direita(m, s_2, n, x, alpha, z_cacl_func):
    z_cale = z_cacl_func(m, s_2, n, x, alpha)
    
    z1 = st.norm.ppf(((100-(alpha))/100), loc=0, scale=1)

    if z_cale < z1:
        print("Decide-se não rejeitar a hipótese inicial pois tcalc pertence à RNR")
    else:
        print("Decide-se rejeitar a hipótese inicial pois tcalc pertence à RC")

def teste_populacoes_normais_conhecidas(m, s_2, n, x, alpha, metodo):
    z_calc_func = lambda m, s_2, n, x, alpha: (x - m) / (np.sqrt(s_2 / n))

    metodo(m, s_2, n, x, alpha, z_calc_func)

def bilateral_desconhecido(n, alpha, z):
    z_cale = z
    phi = n - 1
    
    z1 = t_student.ppf(1 - ((alpha/100)) / 4, phi)
    z2 = t_student.ppf((alpha/100) / 4, phi)

    print(z1, z2, z_cale)

    if z_cale > z2 and z_cale < z1:
        print("Decide-se não rejeitar a hipótese inicial pois tcalc pertence à RNR")
    else:
        print("Decide-se rejeitar a hipótese inicial pois tcalc pertence à RC")

def esquerda_desconhecido(n, alpha, z):
    z_cale = z
    phi = n - 1
    
    z2 = t_student.ppf((alpha/100), phi)

    print(z2)

    if z_cale > z2:
        print("Decide-se não rejeitar a hipótese inicial pois tcalc pertence à RNR")
    else:
        print("Decide-se rejeitar a hipótese inicial pois tcalc pertence à RC")

def direita_desconhecido(n, alpha, z):
    z_cale = z
    phi = n - 1
    
    z1 = t_student.ppf(1 - ((alpha/100)), phi)

    print(z1)

    if z_cale < z1:
        print("Decide-se não rejeitar a hipótese inicial pois tcalc pertence à RNR")
    else:
        print("Decide-se rejeitar a hipótese inicial pois tcalc pertence à RC")

# teste_populacoes_normais_conhecidas(206, 12, 30, 210, 10, direita)
#print(t_student.ppf(5/100, 24))

z = (25.3 - 26) / (np.sqrt(5.86 / 10))
print(z)

print(direita_desconhecido(10, 10, 4.22))
