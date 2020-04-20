#!/usr/bin/python3

'''
Modulo para ser llamado de otros programas con: import,
from import, as, *, etc
'''

__author__ = 'Juan Camarena'
__copyright__ = 'Peru 2016'
__credits__ = 'codigofacilito'

__license__ = 'GLP'
__version__ = '1.0.1'
__maintainer__ = "Yo mi xd"
__email__ = 'jqcamarena@gmail.com'
__status__ = 'Developer'


def media(*arg):
    '''Regresa el promedio del vector (tupla) ingresado'''
    s = 0
    for i in arg:
        s+=i
    return s/len(arg)

def moda(*arg):
    ''''Regresa la moda de los numeros ingresados, devuelve tupla de
([vector de modas],frecuencia max)'''
    n = len (arg)
    k=list(arg)
    k.sort(reverse = False)
    #print(k)
    vm=[] #vector de modas
    mt=k[0] #moda temporal
    mi=0 #moda inicial = 0
    i=0     #indice de recorrido de bucle
    while(i<n-1):
        m=k.count(k[0])
        if (m>=mi):
            if(m==mi):
                vm.append(k[0])
            else:
                if(len(vm)>0):
                    vm=[]
                mi=m
                mt=k[0]
                vm.append(k[0])  
        k.remove(k[0])
        i+=1
    return vm,mi

def mediana(*arg):
    ''''Regresa la mediana de los numeros ingresados, devuelve tupla de
([vector de modas],frecuencia max)'''
    k=list(arg)
    k.sort()
    n = len (arg)
    #print(k)
    if (n%2==0):
        
        return (k[n//2-1]+k[n//2])/2
    else:
        return k[n//2]
    
def varianza(*arg):
    n = len (arg)
    k = list(arg)
    sp = 0
    for i in arg:
        sp+=i
    p = sp/n
    s = 0
    for i in arg:
        s = s+pow(i - p,2)
    #return pow(s/n,0.5)
    return s/n

if __name__ == '__main__':
    print (moda(14,6,4,6,13,14,6,12,4,15,4,14))
