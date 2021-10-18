# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 11:38:30 2021

@author: Mohamed
"""
#import math
from math import *
import datetime 

def message_imc(imc):
    if imc<16.5:
        return "dénutrition ou famine"
    elif 16.5<=imc<18.5:
        return "maigreur"
    elif 18.5<=imc<25:
        return "corpulence normale"
    elif 25<=imc<30:
        return "surpoids"
    elif 30<=imc<35:
        return "obésité modérée"
    elif 35<=imc<=40:
        return "obésité sévère"
    else:
        return "obésité morbide"

def test_mess(k):
    for i in range(10):
        print(message_imc(k))
        k=k+3

def est_bissextile(x):
    return x%4==0 or x%400==0

def test_biss(t):
    for i in range(10):
        print(est_bissextile(t))
        t=t+2

def discriminant(a,b,c):
    return b*b -4*a*c

def racine_unique(a,b):
    return -b/(2*a)

def racine_double(a,b,delta,num):
    if num==1:
        return (-b+sqrt(delta))/(2*a)
    if num==2:
        return (-b - sqrt(delta))/(2*a)

def str_equation(a,b,c):
    print(str(a)+"x2 +",str(b)+"x +",str(c)+"=0")    
    
def solution_equation(a,b,c):
    if delta<0:
        print("Solution de l'equation")
        str_equation(a, b, c)
        print("Pas de racine réelle")
    elif delta==0:
        print("Solution de l'equation")
        str_equation(a,b,c)
        print("Racine unique")
        print("X=",racine_unique(a,b))
    else :
        print("Solution de l'equation")
        str_equation(a,b,c)
        print("Deux racines :")
        print("X1=",racine_double(a,b,delta,1))
        print("X2=",racine_double(a,b,delta,2))
        
def test_equation(a,b,c):
    global delta
    for i in range(5):
        delta=discriminant(a,b,c)
        solution_equation(a,b,c)
        a=a+1
        c=c+2
        print("\n")

def date_est_valide(jour,mois,annee):
    return est_bissextile(annee)==True

def saisie_date_naissance():
    print("Veuillez saisir une année")
    anneeSaisie = int(input())

    print("Veuillez saisir un mois")
    moisSaisie = int(input())

    print("Veuillez saisir un jour")
    jourSaisie = int(input())

    date_naissance = datetime.date(anneeSaisie, moisSaisie, jourSaisie)

    return(date_naissance)


def age(date_naissance):

    today = datetime.datetime.now()


    calculAgeAnnee = int(today.year) - date_naissance.year
    calculAgeMois = int(today.month) - date_naissance.month
    calculAgeJour = int(today.day) - date_naissance.day

    age = calculAgeAnnee

    if calculAgeMois > 0:
        age = age - 1
    elif calculAgeJour > 0:
        age = age - 1


    return(age)

def est_majeur():
    return age(date_naissance)>=18
    
def test_acces():
    saisie_date_naissance()
    if est_majeur()==True:
        print("Bonjour, vous avez ",age(date_naissance()),"ans, Accès autorisé ")
    else:
        print("Désolé, vous avez ",age(date_naissance()),"ans, Accès interdit ")
    
    
k=15
t=2000
test_mess(k)
test_biss(t)
test_equation(5,10,1)
date_est_valide(31,12,2000)
#print(age(date_naissance()))
#print(est_majeur())
test_acces()
