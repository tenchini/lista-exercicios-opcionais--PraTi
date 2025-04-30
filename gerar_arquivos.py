# gerar_arquivos.py
from exercises import exercises
import textwrap
import os


def formatar_enunciado(enunciado, largura=78):
    """Formata o enunciado para caber em linhas de até 'largura' caracteres"""
    # Remove o número do exercício (ex: "1. ") do início
    texto = enunciado.split(". ", 1)[1] if ". " in enunciado else enunciado

    # Quebra o texto em linhas e formata
    linhas_formatadas = []
    for linha in texto.split("\n"):
        if linha.strip() == "":
            linhas_formatadas.append(" *")
        else:
            linhas_formatadas.extend(textwrap.wrap(linha, width=largura))
    return linhas_formatadas


def criar_arquivos_js():
    """Cria os arquivos JS com os enunciados formatados"""
    # Cria a pasta 'exercicios' se não existir
    if not os.path.exists("exercicios"):
        os.makedirs("exercicios")

    for i, exercicio in enumerate(exercises, start=1):
        # Formata o número com dois dígitos
        numero = f"{i:02d}"
        nome_arquivo = f"exercicios/ex{numero}.js"

        # Formata o enunciado
        linhas_enunciado = formatar_enunciado(exercicio)

        # Escreve o arquivo
        with open(nome_arquivo, "w", encoding="utf-8") as f:
            f.write("/**\n")
            f.write(f" * Exercício {i}\n")
            f.write(" *\n")

            # Escreve cada linha do enunciado
            for linha in linhas_enunciado:
                if linha.startswith("-") or linha.startswith("*"):
                    f.write(f" * {linha}\n")
                else:
                    f.write(f" * {linha}\n" if linha.strip() else " *\n")

            f.write(" */\n\n")
            f.write("// Sua solução aqui\n")


if __name__ == "__main__":
    criar_arquivos_js()
    print("Arquivos JS gerados com sucesso na pasta 'exercicios'!")
