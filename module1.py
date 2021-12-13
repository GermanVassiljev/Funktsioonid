from math import *
#def Pindala(külg_1:float, külg_2:float)->float:
#    """Riistküliku pindala leidmine
#    :param float külg_1:Riistküliku esimene külg
#    :param float külg_2:Riistküliku teine külg
#    :rtype:float
#    """
#    S=külg_1*külg_2
#    return S
#Task 1
#def arithmetic(a:float,b:float,c:str)->float:
#    """ Saab teha +,-,*,/ ja tagastab arv kui vastus on arv ja "Tundmatu tehe" kui ei saa vastus leida.
#    :param float a: Esimene arv
#    :param float b: Teine arv
#    :param str c:Aritmeetilise tehe
#    :rtype:var
#    """
#    if c == "+":
#        D=a+b
#        return D
#    elif c =="-":
#        D=a-b
#        return D
#    elif c=="*" and a!=0 or b!=0:
#        D=a*b
#        return D
#    elif c=="/" and a!=0 or b!=0:
#        D=a/b
#        return D
#    else:
#        return("неизвестная операция")
#Task 2
#def is_year_leap(a=int)->int:
#    """
#    :param int a: Aasta
#    """
#    if a%4==0:
#        return True
#    else:
#        return False
#Task 3
#def square(a:float):
#    """
#    :param float a: 
#    """
#    S=a**2
#    D=sqrt(2*S)
#    P=a**4
#    return S, D, P
#Task 4
def season(a:int):
    """
    :param int a: Seasons
    """
    if a==1 or a==12 or a==2:
        print("talv")
    elif a==3 or a==4 or a==5:
        print("kevad")
    elif a==6 or a==7 or a==8:
        print("suvi")
    elif a==9 or a==10 or a==11:
        print("sügis")