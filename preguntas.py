"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

with open ("data.csv","r") as archivo_data:
    datos = archivo_data.read()        
    columnas = datos.splitlines()        
    columnas_unidas = []
    suma_columna2 = 0
    for filas in columnas:
        columns = filas.split("\t")
        columnas_unidas.append(columns)
    data_lista = columnas_unidas

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """

    suma_columna2 = 0
    for elementos in data_lista:
        suma_columna2 += int(elementos[1])
    #print(suma_columna2)
        #print(columnas_unidas)
    return suma_columna2


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """

    letras_col_1 = ["A","B","C","D","E"]
    rta_2 = ()
    suma_letra = 0

    for letters in letras_col_1:
        suma_letra = 0
        for letras in data_lista:
            if letras[0] == letters:
                suma_letra += 1
        if  len(rta_2) == 0:    
            rta_2 = [(letters,suma_letra)]
        else: 
            rta_2.append((letters,suma_letra))
    #print(rta_2)

    return rta_2


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """

    letras_col_1 = ["A","B","C","D","E"]
    rta_3 = ()
    suma_letra = 0

    for letters in letras_col_1:
        suma_letra = 0
        for letras in data_lista:
            if letras[0] == letters:
                suma_letra += int(letras[1])
        if  len(rta_3) == 0:    
            rta_3 = [(letters,suma_letra)]
        else: 
            rta_3.append((letters,suma_letra))
    #print(rta_3)

    return rta_3


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    suma_mes = 0
    rta_4 = ()
    meses_ano = ["01","02","03","04","05","06","07","08","09","10","11","12"]
    for meses in meses_ano:
        suma_mes = 0
        for letras in data_lista:
            col_mes = letras[2]
            mes = col_mes.split("-")[1]          
            if meses == mes:
                suma_mes += 1
        if  len(rta_4) == 0:    
            rta_4 = [(meses,suma_mes)]
        else: 
            rta_4.append((meses,suma_mes))
    #print(rta_4)

    return rta_4


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    rta_5 = ()
    letras_col_1 = ["A","B","C","D","E"]
    for letters in letras_col_1:  
        valor_min = None
        valor_max = None       
        for letras in data_lista:            
            if letters == letras[0]:
                valor = int(letras[1])             
                if valor_min is None or valor < valor_min:
                    valor_min = valor
                if valor_max is None or valor > valor_max:
                    valor_max = valor            
        if  len(rta_5) == 0:    
            rta_5 = [(letters,valor_max,valor_min)]
        else: 
            rta_5.append((letters,valor_max,valor_min))

    #print(rta_5)

    return rta_5


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    dic = {}
    llaves_unicas = []
    lista_comp = []
    nueva_lista_valores = []    
    rta_6 = []
    for filas in data_lista:
        lista_colum5 = filas[4].split(",")
        lista_comp += lista_colum5  
        #print(lista_colum5)     
    for elements in lista_comp:
        key, value =  elements.split(":") 
        dic[key] = int(value) 
    llaves_unicas = set(dic.keys())  
    llaves_unicas = sorted(llaves_unicas)
    #print(llaves_unicas)    
    for x in lista_comp:  
        nueva_lista_valores.append(x.split(":"))
        #print(nueva_lista_valores)    
    for key in llaves_unicas:
        valor_min = None
        valor_max = None   
        #print(key)
        for sublista in nueva_lista_valores:
            if sublista[0] == key:
                valor = int(sublista[1])
        #print (f"{key},{valor}") 
                if valor_min is None or valor < valor_min:
                    valor_min = valor
                if valor_max is None or valor > valor_max:
                    valor_max = valor            
        if  len(rta_6) == 0:    
            rta_6 = [(key, valor_min,valor_max)]
        else: 
            rta_6.append((key,valor_min,valor_max))
    #print(rta_6)
    return rta_6


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    lo que tengo que hacer en este punto es 

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """    
    lista_comp = []
    for filas in data_lista:
        lista_colum2 = filas[1].split(",")
        lista_comp += lista_colum2 

    valores_unicos = []
    for valores in lista_comp:
        if valores not in valores_unicos:
            valores_unicos.append(valores)
            valores_unicos = sorted(valores_unicos)

    nueva_lista = [[x[0], x[1]] for x in data_lista]

    rta_7 = []    
    for key in valores_unicos: 
        #print(key)
        val_acum = []
        for sublista in nueva_lista:
            if sublista[1] == key:
                letra = sublista[0]
            #print(letra)
                val_acum.append(letra)
            #val_acum = sorted(list(set(val_acum)))
        rta_7.append((int(key),val_acum))
    #print(rta_7)
    return rta_7


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    lista_comp = []
    for filas in data_lista:
        lista_colum2 = filas[1].split(",")
        lista_comp += lista_colum2 

    valores_unicos = []
    for valores in lista_comp:
        if valores not in valores_unicos:
            valores_unicos.append(valores)
            valores_unicos = sorted(valores_unicos)

    nueva_lista = [[x[0], x[1]] for x in data_lista]

    rta_8 = []    
    for key in valores_unicos: 
        #print(key)
        val_acum = []
        for sublista in nueva_lista:
            if sublista[1] == key:
                letra = sublista[0]
            #print(letra)
                val_acum.append(letra)
            val_acum = sorted(list(set(val_acum)))
        rta_8.append((int(key),val_acum))
    
    #print(rta_8)
    return rta_8


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    dic = {}
    llaves_unicas = []
    lista_comp = []
    nueva_lista_valores = []    
    rta_9 = {}    
    for filas in data_lista:
        lista_colum5 = filas[4].split(",")
        lista_comp += lista_colum5  
        #print(lista_colum5)     
    for elements in lista_comp:
        key, value =  elements.split(":") 
        dic[key] = int(value) 
    llaves_unicas = set(dic.keys())  
    llaves_unicas = sorted(llaves_unicas)
    #print(llaves_unicas)    
    for x in lista_comp:  
        nueva_lista_valores.append(x.split(":"))
        #print(nueva_lista_valores)    
    for key in llaves_unicas:  
        #print(key)
        cont = 0
        for sublista in nueva_lista_valores:
            if sublista[0] == key:
                cont += 1
        rta_9[key] = int(cont) 
    #print(rta_9)
    return rta_9


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    nueva_list = [[x[0], x[3], x[4]] for x in data_lista]
    rta_10 = []
    for element in nueva_list:
        elementos = element[1].split(",") 
        elemento2 = element[2].split(",")
        cont_col2 = len([elem for elem in elementos if elem != ''])
        cont_col3 = len([elem for elem in elemento2 if elem != ''])
        rta_10.append((element[0],cont_col2,cont_col3))
    #print(rta_10)
    return rta_10


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    nueva_list_11 = [[x[1], x[3]] for x in data_lista]
    col_1=[]
    list_letras = []
    sorted_list = []
    for element in nueva_list_11:
        nume = element[0].split(",")
        col_1.append([nume,list(element[1].split(","))])
    for elemen in nueva_list_11:
        letras = elemen[1].split(",")        
        list_letras += letras    
    sorted_list = sorted(set(list_letras)) 

    conteo = 0
    rta_11 = {}
    for lett in sorted_list:
        conteo = 0
        for filas in col_1:
            for numm in filas[0]:
                numer = int(numm)      
            for ele in filas[1]:      
                if lett == ele:        
                    conteo += numer
            rta_11 [lett] = conteo
    #print(rta_11)   

    return rta_11


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """

    with open("data.csv","r") as datos:
        datos=[linea.replace("\n","") for linea in datos]
        datos=[linea.split("\t") for linea in datos]
        
        datos_primeracol=[n[0] for n in datos]
        datos_quintacol=[n[4] for n in datos]
        datos_quintacol=[n.split(",") for n in datos_quintacol]
        letras=[]
        lista2=[]
        lista3=[]
        diccionario={}
        diccionario_final={}

        for dato in datos_primeracol:
                if dato not in letras:
                        letras.append(dato)
        
        
        for dato in datos_quintacol:      
                diccionario={}
                for cada in dato:       
                        clave,valor=cada.split(":")
                        if clave not in diccionario:
                                diccionario[clave] = int(valor)
                        else:
                                diccionario[clave].append(int(valor))
                lista=list(diccionario.values())
                lista2.append(sum(lista))
    
            
        for m in range(len(letras)):
                lis=[]
                for letra,numeros in zip(datos_primeracol,lista2):

                        if letra==letras[m]:
                                lis.append(int(numeros))                         
                lista3.append(sum(lis))
        
        diccionario_final_desord=dict(zip(letras,lista3))

        lista_diccionario_final=sorted(diccionario_final_desord.items())
        
        for key, value in lista_diccionario_final :
                diccionario_final[key]=value

        #print(diccionario_final)
        return diccionario_final

# if __name__ == "__main__":

#     with open ("data.csv","r") as archivo_data:
#         datos = archivo_data.read()        
#         columnas = datos.splitlines()        
#         columnas_unidas = []
#         suma_columna2 = 0
#         for filas in columnas:
#             columns = filas.split("\t")
#             columnas_unidas.append(columns)
#         data_lista = columnas_unidas

#     # pregunta_01()
#     # pregunta_02()
#     # pregunta_03()
#     # pregunta_04()
#     # pregunta_05()
#     # pregunta_06()
#     # pregunta_07()
#     # pregunta_08()
#     # pregunta_09()
#     # pregunta_10()
#     # pregunta_11()
#     pregunta_12()
