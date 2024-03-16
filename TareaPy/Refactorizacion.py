def procesamiento():
    print('Seleccione la acción que desea realizar:')
    print('1: Ingresar un punto de evaluación y un comentario')
    print('2: Ver los resultados hasta ahora')
    print('3: Salir')

while True:
    procesamiento()
    num = input()

    if num.isdecimal():
        num = int(num)

        if num == 1:
            while True:
                print('Ingrese una evaluación del 1 al 5:')
                point = input()
                if point.isdecimal():
                    point = int(point)
                    if 1 <= point <= 5:
                        print('Ingrese un comentario:')
                        comment = input()
                        post = f'Punto de evaluación: {point} Comentario: {comment}'
                        file_pc = open("data.txt", 'a')
                        file_pc.write(f'{post}\n')
                        file_pc.close()
                        break
                    else:
                        print('Ingrese un valor del 1 al 5.')
                else:
                    print('Por favor, ingrese un punto de evaluación válido (número).')
        elif num == 2:
            print('Resultados hasta ahora:')
            read_file = open("data.txt", "r")
            print(read_file.read())
            read_file.close()
        elif num == 3:
            print('Saliendo del programa...')
            break
        else:
            print('Ingrese un número del 1 al 3.')
    else:
        print('Ingrese un número del 1 al 3.')

