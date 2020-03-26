

def libres(sudoku):
    '''
    con esta función haremos una lista con los cuadrados libres
    '''
    libre = []
    for i in range(len(sudoku)):
        for j in range(len(sudoku[i - 1])):
            if sudoku[i][j] == 0:
                libre.append([i,j])

    return libre


def cuadrados(sudoku):
    '''
        esta función devolverá una lista con los numeros en cada cuadrado
    '''
    cuadrado = []
    cuadrado1 = []
    cuadrado2 = []
    cuadrado3 = []
    cuadrado4 = []
    cuadrado5 = []
    cuadrado6 = []
    cuadrado7 = []
    cuadrado8 = []
    cuadrado9 = []
    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            if i < 3:
                if j < 3:
                    cuadrado1.append(sudoku[i][j])
                elif j >= 3 and j < 6:
                    cuadrado2.append(sudoku[i][j])
                else:
                    cuadrado3.append(sudoku[i][j])
            elif i >= 3 and i < 6:
                if j < 3:
                    cuadrado4.append(sudoku[i][j])
                elif j >= 3 and j < 6:
                    cuadrado5.append(sudoku[i][j])
                else:
                    cuadrado6.append(sudoku[i][j])
            else:
                if j < 3:
                    cuadrado7.append(sudoku[i][j])
                elif j >= 3 and j < 6:
                    cuadrado8.append(sudoku[i][j])
                else:
                    cuadrado9.append(sudoku[i][j])


    cuadrado.append(cuadrado1)
    cuadrado.append(cuadrado2)
    cuadrado.append(cuadrado3)
    cuadrado.append(cuadrado4)
    cuadrado.append(cuadrado5)
    cuadrado.append(cuadrado6)
    cuadrado.append(cuadrado7)
    cuadrado.append(cuadrado8)
    cuadrado.append(cuadrado9)
    return cuadrado


def opciones(i,j,sudoku):
    '''
        esta función devolverá una lista con las opciones validas para el hueco
    '''
    cuadrado = cuadrados(sudoku)

    lista_opciones = []

    lista_H = sudoku[i]
    lista_V = [sudoku[x][j] for x in range(len(sudoku))]
    lista_C =[]

    if i < 3:
        if j < 3:
            lista_C = cuadrado[0]
        elif j >= 3 and j < 6:
            lista_C = cuadrado[1]
        else:
            lista_C = cuadrado[2]
    elif i >= 3 and i < 6:
        if j < 3:
            lista_C = cuadrado[3]
        elif j >= 3 and j < 6:
            lista_C = cuadrado[4]
        else:
            lista_C = cuadrado[5]
    else:
        if j < 3:
            lista_C = cuadrado[6]
        elif j >= 3 and j < 6:
            lista_C = cuadrado[7]
        else:
            lista_C = cuadrado[8]

    opcion = 1
    while opcion <= 9:
        puntuacion = 0
        if  opcion not in lista_H:
            puntuacion += 1
        if opcion not in lista_V:
            puntuacion += 1
        if opcion not in lista_C:
            puntuacion += 1
        if puntuacion == 3:
            lista_opciones.append(opcion)
        opcion += 1
    return lista_opciones



def resolver(espacios_usados, opciones_usadas, vuelto):
    '''
        esta función resuelve el sudoku mediante regresión
    '''
    global sudoku
    lista_libres = libres(sudoku)

    # si no hay mas espacios acaba 
    if len(lista_libres) == 0:
        return sudoku

    # si sigue habiendo espacios
    else:
        for i,j in lista_libres:
            lista_opciones = opciones(i, j ,sudoku)
            reser = []
            if len(opciones_usadas) != 0:
                reser = opciones_usadas[-1]
            if vuelto:
                reser = opciones_usadas.pop()
                for op in reser:
                    lista_opciones.remove(op)
            if len(lista_opciones) == 0:
                lugar_anterior = espacios_usados.pop()
                x, y = lugar_anterior
                sudoku[x][y] = 0
                resolver(espacios_usados, opciones_usadas, True)
                return sudoku
            else:
                for opcion in lista_opciones:
                    if vuelto:
                        reser.append(opcion)
                        opciones_usadas.append(reser)
                    else:
                        opciones_usadas.append([opcion])
                    espacios_usados.append(lista_libres.pop(0))
                    sudoku[i][j] = opcion
                    resolver(espacios_usados, opciones_usadas, False)
                    return sudoku

sudoku = [[0,9,0,0,7,4,0,0,1],[0,0,0,0,2,0,5,0,9],[0,2,4,0,9,0,8,6,7],[4,0,0,0,8,1,9,2,5],[0,0,9,0,0,0,6,0,0],[1,6,5,9,3,0,0,0,8],[9,5,7,0,6,0,1,8,0],[6,0,1,0,4,0,0,0,0,],[8,0,0,7,1,0,0,5,0]]

sudoku = resolver([],[],False)

for i in sudoku:
    print(i)

