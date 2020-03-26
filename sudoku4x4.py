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

    for i in range(len(sudoku)):
            for j in range(len(sudoku[i])):
                if i < 2:
                    if j < 2:
                        cuadrado1.append(sudoku[i][j])
                    else:
                        cuadrado2.append(sudoku[i][j])
                else:
                    if j < 2:
                        cuadrado3.append(sudoku[i][j])
                    else:
                        cuadrado4.append(sudoku[i][j])

    cuadrado.append(cuadrado1)
    cuadrado.append(cuadrado2)
    cuadrado.append(cuadrado3)
    cuadrado.append(cuadrado4)

    return cuadrado


def opciones(i,j,sudoku):
    '''
        esta función devolverá una lista con las opciones validas para el hueco
    '''
    global cuadrado

    lista_opciones = []

    lista_H = sudoku[i]
    lista_V = [sudoku[x][j] for x in range(len(sudoku))]
    lista_C =[]

    if i < 2:
        if j < 2:
            lista_C = cuadrado[0]
        else:
            lista_C = cuadrado[1]
    else:
        if j < 2:
            lista_C = cuadrado[2]
        else:
            lista_C = cuadrado[3]

    opcion = 1
    while opcion <= 4:
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


### resolver
def resolver(espacios_usados, opciones_usadas, vuelto):
    global sudoku
    lista_libres = libres(sudoku)

    if len(lista_libres) == 0:
        return sudoku

    else:
        i, j = lista_libres[0]
        lista_opciones = opciones(i, j ,sudoku)    
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

sudoku = [[0,0,4,0],[4,0,3,0],[0,4,0,3],[0,1,0,0]]
cuadrado = cuadrados(sudoku)

print(resolver([], [], False))
