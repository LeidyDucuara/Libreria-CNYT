"""
Elaborado por Leidy Marcela Ducuara
Número de carnet 2164403
Descripción: A lo largo de esta librería se definirán funciones que nos permitiran manipular número complejos,que se representaran la mayoria de las veces como
un arreglo [a,b]
"""

import math

def suma(c1,c2):
    """
    La función suma recibe dos números: c1 y c2 (que deben ser listas de longitud dos) y 
    retorna un número complejo de la misma forma, correspondiente a la operación c1 + c2
    """
    return [c1[0]+c2[0],c1[1]+c2[1]]

def resta(c1,c2):
    """
    La función resta recibe dos números: c1 y c2 (que deben ser listas de longitud dos) y 
    retorna un número complejo de la misma forma, correspondiente a la operación c1 - c2
    """
    return [c1[0]-c2[0],c1[1]-c2[1]]

def multiplicacion(c1,c2):
    """
    La función multiplicación recibe dos números: c1 y c2 (que deben ser listas de longitud dos) y 
    retorna un número complejo de la misma forma, correspondiente a la operación c1 * c2
    """
    return[c1[0]*c2[0]-c1[1]*c2[1],c1[0]*c2[1]+c1[1]*c2[0]]


def conjugado(c1):
    """
    La función conjugado recibe un número: c1 (que debe ser una lista de longitud dos) y 
    retorna el conjugado del mismo número y de la misma forma
    """
    if c1[1] > 0:
        return [c1[0],c1[1]*(-1)]
    else:
        return [c1[0],abs(c1[1])]

def division(c1,c2):
    """
    La función división recibe dos números: c1 y c2 (que deben ser listas de longitud dos) y 
    retorna un número complejo de la misma forma, correspondiente a la operación c1 / c2, recurriendo
    a la multiplicación arriba y abajo por el conjugado del número complejo c2
    """
    con = conjugado(c2)
    num = multiplicacion(c1,con)
    den = multiplicacion(c2,con)
    return [num[0]/den[0],num[1]/den[0]]

def imprimir(c1):
    #return complex(c1[0],c1[1])
    """
    La función imprimir recibe un número complejo de la forma [a,b] y lo devuelve de la forma a+bi 
    """
    if c1[1] >= 0:
        return str(c1[0]) +"+"+ str(c1[1]) +"i"
    else:
        return str(c1[0]) + str(c1[1]) +"i"

def modulo(c1):
    """
    La función modulo recibe un número: c1 (que debe ser una lista de longitud dos) y 
    retorna un número correspondiente a la raiz de (c1[0]^2+c1[1]^2)
    """
    return math.sqrt(c1[0]**2+c1[1]**2)

def fase(c1):
    """
    La función fase recibe un número: c1 (que debe ser una lista de longitud dos) y 
    retorna un número correspondiente al angulo θ en radianes
    """
    return math.atan2(c1[1],c1[0])

def conv_a_polar(c1):
    """
    La función con_a_polar recibe un número: c1 (que debe ser una lista de longitud dos) y debe estar 
    en forma cartesiana para que la función retorne el mismo número en forma polar [p,θ], para esto emplearemos
    funciones creadadas con anterioridad como lo son modulo y fase(radianes)
    """
    return[modulo(c1),fase(c1)]

def conv_a_cartesiana(c1):
    """
    La función conv_a_cartesiana recibe un número: c1 (que debe ser una lista de longitud dos) y debe estar 
    en forma polar para que la función retorne el mismo número en forma cartesiana [a,b], donde a = p*cos(θ) 
    y b = p*sen(θ)
    """
    return [round(c1[0]*math.sin(c1[1]),2), round(c1[0]*math.cos(c1[1]),2)]

def imprimir_po_exponencial(c1):
    """
    La función imprimir_po_exponensial recibe un número: c1 (que debe ser una lista de longitud dos) y debe estar 
    en forma polar para que la función retorne el mismo número complejo pero de la forma exponensial (pe^(iθ))
    """
    return str(c1[0]) + "e^"+ str(c1[1]) + "i"

def imprimir_ca_exponencial(c1):
    """
    La función imprimir_ca_exponensial recibe un número: c1 (que debe ser una lista de longitud dos) y debe estar 
    en forma cartesiana [a,b] para que la función retorne el mismo número complejo pero de la forma exponensial (pe^(iθ))
    """
    return str(modulo(c1)) + "e^"+ str(fase(c1)) + "i"

def potencia(n,c1): 
    """
    La función potencia recibe un número: c1 (que debe ser una lista de longitud dos) y debe estar 
    en forma cartesiana [a,b] y un número n que será la potencia que queremos del número complejo, la función debe retornar 
    un número [c,d] donde el módulo es la potencia n-ésima del módulo original y su argumento (ángulo en radianes) es n veces 
    el argumento dado.
    """
    m_f = conv_a_polar(c1)
    return [m_f[0]**n,m_f[1]*n]
