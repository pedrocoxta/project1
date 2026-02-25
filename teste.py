"""Comparador simples de dois números.

Uso:
- executar sem argumentos: pede os números via input()
- executar com dois argumentos: `python teste.py 5 3`
"""

from __future__ import annotations
import sys

def ler_numero(text: str) -> float:
    while True:
        try:
            return float(input(text))
        except ValueError:
            print('Entrada inválida. Digite um número válido.')

def formato(n: float) -> str:
    if n.is_integer():
        return str(int(n))
    return str(n)

def main(args: list[str]) -> None:
    if len(args) >= 3:
        try:
            a = float(args[1])
            b = float(args[2])
        except ValueError:
            print('Argumentos inválidos. Devem ser números.')
            return
    else:
        a = ler_numero('Digite o primeiro número: ')
        b = ler_numero('Digite o segundo número: ')

    print()  # linha em branco antes do resultado
    if a > b:
        print(f'{formato(a)} é maior que {formato(b)}')
    elif a < b:
        print(f'{formato(a)} é menor que {formato(b)}')
    else:
        print(f'{formato(a)} é igual a {formato(b)}')

if __name__ == '__main__':
    main(sys.argv)

