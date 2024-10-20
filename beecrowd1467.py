# EN - US
def identify_different_value(a: int, b: int, c: int) -> str:
    """
    Identifies and returns which value is different from the others or returns '*' if all are the same.

    Args:
        a (int): First value.
        b (int): Second value.
        c (int): Third value.

    Returns:
        str: "A", "B", "C", or "*", depending on which value is different or if all are the same.
    """
    if a != b and a != c:
        return "A"
    elif b != a and b != c:
        return "B"
    elif c != a and c != b:
        return "C"
    else:
        return "*"

def main() -> None:
    """
    Main function that reads input, calls the function to identify the different value,
    and prints the result until the end of input is reached.
    """
    while True:
        try:
            a, b, c = map(int, input().split())
            result = identify_different_value(a, b, c)
            print(result)
        except EOFError:
            break

# PT - BR
# def identificar_valor_diferente(a: int, b: int, c: int) -> str:
#     """
#     Identifica e retorna qual valor é diferente dos outros dois ou retorna '*' se todos forem iguais.

#     Args:
#         a (int): Primeiro valor.
#         b (int): Segundo valor.
#         c (int): Terceiro valor.

#     Returns:
#         str: "A", "B", "C" ou "*", dependendo de qual valor for diferente ou se todos forem iguais.
#     """
#     if a != b and a != c:
#         return "A"
#     elif b != a and b != c:
#         return "B"
#     elif c != a and c != b:
#         return "C"
#     else:
#         return "*"

# def main() -> None:
#     """
#     Função principal que lê as entradas, chama a função para identificar o valor diferente,
#     e imprime o resultado até encontrar o fim da entrada.
#     """
#     while True:
#         try:
#             a, b, c = map(int, input().split())
#             resultado = identificar_valor_diferente(a, b, c)
#             print(resultado)
#         except EOFError:
#             break

if __name__ == "__main__":
    main()