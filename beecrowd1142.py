# EN - US
def print_sequence_with_pum(total_lines: int) -> None:
    """
    Prints a sequence of numbers followed by "PUM" for the given number of lines.
    Each line consists of three numbers followed by the word "PUM".

    Args:
        total_lines (int): The number of lines to be printed.
    """
    for i in range(total_lines):
        for j in range(3):
            print((4 * i) + j + 1, end=" ")
        print("PUM")

def main() -> None:
    """
    Main function to read input and call the function to print the sequence with "PUM".
    """
    total_lines = int(input())
    print_sequence_with_pum(total_lines)

# # PT - BR
# def imprimir_sequencia_com_pum(total_linhas: int) -> None:
#     """
#     Imprime uma sequência de números seguida por "PUM" para o número de linhas fornecido.
#     Cada linha consiste em três números seguidos pela palavra "PUM".

#     Args:
#         total_linhas (int): O número de linhas a serem impressas.
#     """
#     for i in range(total_linhas):
#         for j in range(3):
#             print((4 * i) + j + 1, end=" ")
#         print("PUM")

# def main() -> None:
#     """
#     Função principal que lê a entrada e chama a função para imprimir a sequência com "PUM".
#     """
#     total_linhas = int(input())
#     imprimir_sequencia_com_pum(total_linhas)

if __name__ == "__main__":
    main()