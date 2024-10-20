# EN - US
def calculate_sum_of_range(numbers: list[int]) -> None:
    """
    Calculates and prints the numbers in the range between two positive integers,
    along with the sum of these numbers.

    Args:
        numbers (list[int]): A list containing two integers defining the range.
    """
    total_sum = 0
    numbers.sort()  # Sort the values to ensure the correct sequence

    for i in range(numbers[0], numbers[1] + 1):
        total_sum += i
        print(i, end=" ")

    print(f"Sum={total_sum}")

def main() -> None:
    """
    Main function that controls the input loop and the execution of the sum calculation.
    The loop ends when one of the input numbers is less than or equal to zero.
    """
    while True:
        numbers = [int(e) for e in input().split()]

        # Check if both numbers are positive
        if numbers[0] > 0 and numbers[1] > 0:
            calculate_sum_of_range(numbers)
        else:
            break

# # PT - BR
# def calcular_soma_intervalo(x: list[int]) -> None:
#     """
#     Calcula e imprime os números no intervalo entre dois valores inteiros positivos e a soma desses números.

#     Args:
#         x (list[int]): Lista contendo dois números inteiros para definir o intervalo.
#     """
#     soma = 0
#     x.sort()  # Ordena os valores para garantir a sequência correta

#     for i in range(x[0], x[1] + 1):
#         soma += i
#         print(i, end=" ")

#     print(f"Sum={soma}")

# def main() -> None:
#     """
#     Função principal que controla o loop de leitura de entrada e execução do cálculo da soma do intervalo.
#     O loop termina quando um dos dois números inseridos for menor ou igual a zero.
#     """
#     while True:
#         numeros = [int(e) for e in input().split()]

#         # Verifica se ambos os números são positivos
#         if numeros[0] > 0 and numeros[1] > 0:
#             calcular_soma_intervalo(numeros)
#         else:
#             break

if __name__ == "__main__":
    main()