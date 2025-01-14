def introducir_puntos_comentarios():
    while True:
        print('Por favor, introduzca una puntuación en una escala de 1 a 5.')
        point = input()
        if point.isdecimal():
            point = int(point)
            if 1 <= point <= 5:
                print('Introduzca sus comentarios.')
                comment = input()
                post = f'punto: {point} comentario: {comment}'
                with open("data.txt", 'a') as file_pc:
                    file_pc.write(f'{post}\n')
                break
            else:
                print('Indíquelo en una escala de 1 a 5.')
        else:
            print('Introduzca los puntos de valoración como números.')

def comprobar_resultados():
    print('Resultados hasta la fecha.')
    with open("data.txt", "r") as read_file:
        print(read_file.read())

def seleccionar_proceso(num):
    if num == 1:
        introducir_puntos_comentarios()
    elif num == 2:
        comprobar_resultados()
    elif num == 3:
        print('Finalizado.')
        return True
    else:
        print('Por favor, introduzca del 1 al 3.')

def main():
    while True:
        print('Seleccione el proceso que desea aplicar.')
        print('1: Introducir puntos de evaluación y comentarios.')
        print('2: Comprobar los resultados hasta ahora.')
        print('3: Finalizar.')
        num = input()

        if num.isdecimal():
            num = int(num)
            if seleccionar_proceso(num):
                break
        else:
            print('Por favor, introduzca del 1 al 3.')

if __name__ == "__main__":
    main()
