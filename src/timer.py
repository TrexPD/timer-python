from time import sleep
from rich import print
from rich.console import Console
from rich.table import Table
from rich import box
from re import findall
from typing import Tuple, Optional


def validador_horario_em_regex() -> Optional[Tuple[int, int, int]]:
    while True:
        try:
            console = Console()
            tempo_do_usuario: str = console.input("Digite o tempo no formato 'HH:MM:SS': ")
            horario = findall("^\d{2}.\d{2}.\d{2}$", tempo_do_usuario)
            if not horario:
                print('[yellow]Hummm... parece que você não digitou um formato válido![/]')
                continue

        except KeyboardInterrupt:
            print('[red]O usuário abortou, preferiu não inserir um valor válido![/]')
            break
        except:
            print('[yellow]Hummm... parece que você não digitou um formato válido![/]')
        else:
            return int(horario[0][:2]), int(horario[0][3:5]), int(horario[0][6:])


# Timer que funciona perfeitamente, colocando horas, minutos e segundos!
def main() -> str:
    console = Console()
    tothoras, totminutos, segundos = validador_horario_em_regex()

    lembrete: str = str(console.input('Digite um [yellow]lembrete[/] para quando o [yellow]Timer[/] chegar ao fim: ')).strip()

    print(Table('Contagem regresiva iniciada!', box=box.SIMPLE_HEAD))

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
        for contador in range(segundos, -1, -1):
            print(' {:02d}:{:02d}:{:02d}'.format(tothoras, totminutos, contador), end='\r')
            sleep(1)
        if tothoras >= 1 and totminutos == 0:
            tothoras -= 1
            totminutos = 59
            continue

        elif totminutos >= 1 and contador == 0:
            totminutos -= 1
            segundos = 59
            continue

        elif totminutos == 0 and contador == 0:
            print('\n\n[b]Lembrete:[/]')
            if lembrete == '':
                print('\n[yellow]A [b]contagem regresiva[/] chegou ao fim![/]')
                break
            else:
                print(f'\n[yellow]{lembrete.upper()}[/]')
                break

if __name__ == "__main__":
    main()