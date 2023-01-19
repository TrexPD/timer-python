from time import sleep
from rich import print
from rich.console import Console
from rich.table import Table
from rich import box


# Função que ler apenas números inteiros!
def leia_int(msg: str) -> int or str:
    while True:
        try:
            console = Console()
            numero: int = int(console.input(msg).strip())
        except KeyboardInterrupt:
            print('\n[red]O usuário abortou, preferiu não inserir um valor válido![/]')
            break
        except:
            print('\n[yellow]Hummm... parece que você não digitou um número inteiro válido![/]')
        else:
            return numero


# Timer que funciona perfeitamente, colocando horas, minutos e segundos!
def main() -> str:
    console = Console()
    tothoras: int = leia_int('Quantas [green]horas[/] para o [b]Timer[/]: ')
    totminutos: int = leia_int('Quantos [green]minutos[/] para o [b]Timer[/]: ')
    segundos: int = leia_int('Quantos [green]segundos[/] para o [b]Timer[/]: ')
    lembrete: str = str(console.input('Digite um [yellow]lembrete[/] para quando o [b]Timer[/] chegar ao fim: ')).strip()

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
            if lembrete == '':
                print('\n\n[yellow]A [b]contagem regresiva[/] chegou ao fim![/]')
                break
            else:
                print('\n\n[b]Lembrete:[/]')
                print(f'[yellow]{lembrete.capitalize()}[/]')
                break


main()