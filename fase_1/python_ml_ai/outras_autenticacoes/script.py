import sys, os


def soma(a, b):
    return a + b


def main():
    resultado = soma(5, 7)
    print("O resultado é: ", resultado)


if __name__ == "__main__":
    main()

# no terminal: black outras_autenticacoes (formata o código)
# no terminal: flake8 outras_autenticacoes/script.py (procura possíveis melhorias de formatação de código)
