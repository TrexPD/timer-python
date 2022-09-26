from time import sleep


# Função que ler apenas números inteiros!
def leia_int(msg):
    while True:
        try:
            numero: int = int(input(msg))
        except KeyboardInterrupt:
            print(
                '\n\033[1;31mO usuario abartou, preferiu não inserir um valor válido!\033[m'
            )
            break
        except:
            print(
                '\033[1;31mHummm... parece que você não digitou um número inteiro válido!\033[m'
            )
        else:
            return numero


# Perfumaria...
def caixa_dialogo(dialogo=''):
    print('--' * len(dialogo))
    print(f'| \033[1;30m{dialogo.center(53)}\033[m')
    print('--' * len(dialogo))


# Timer que funciona perfeitamente, colocando horas, minutos e segundos!
def timer():
    tothoras: int = leia_int('Quantas \033[1;32mhoras\033[m para o "Timer": ')
    totminutos: int = leia_int('Quantos \033[1;32mminutos\033[m para o "Timer": ')
    segundos: int = leia_int('Quantos \033[1;32msegundos\033[m para o "Timer": ')
    lembrete: str = str(
        input('Digite um \033[1;33mlembrete\033[m para o "Timer": ')
    ).strip()
    print('')
    caixa_dialogo('Contagem regresiva iniciada! ')

    # Define a quantidade de horas, minutos e segundos!
    while True:
        if segundos >= 60:
            totminutos += 1
            segundos -= 60
        elif totminutos >= 60:
            tothoras += 1
            totminutos -= 60
        else:
            break

    # Faz a contagem regressiva e verifica se o tempo chegou ao fim, ao chegar um lembrete será mostrado!
    while True:
        for i in range(segundos, -1, -1):
            print(
                '\033[1;31m {:02d}:{:02d}:{:02d}\033[m'.format(
                    tothoras, totminutos, i
                ),
                end='\r',
            )
            sleep(1)
        if tothoras >= 1 and totminutos == 0:
            tothoras -= 1
            totminutos = 59
            continue

        elif totminutos >= 1 and i == 0:
            totminutos -= 1
            segundos = 59
            continue

        elif totminutos == 0 and i == 0:
            if lembrete == '':
                print('\033[1;33mO Timer chegou ao fim!\033[m')
                break
            else:
                print('')
                print('')
                print('\033[1;30mLembrete:\033[m')
                print(f'\033[1;33m{lembrete}\033[m')
                break


timer()
