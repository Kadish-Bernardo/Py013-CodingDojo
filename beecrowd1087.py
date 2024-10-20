# EN - US
def queen_moves(x_queen: int, y_queen: int, x_target: int, y_target: int) -> int:
    """
    Calculates the minimum number of moves required for a queen in chess 
    to move from her current position to the target.

    Args:
        x_queen (int): Queen's current position on the x-axis.
        y_queen (int): Queen's current position on the y-axis.
        x_target (int): Target position on the x-axis.
        y_target (int): Target position on the y-axis.

    Returns:
        int: The number of moves required (0, 1, or 2).
    """
    if x_queen == x_target and y_queen == y_target:
        return 0
    elif (x_queen == x_target) or (y_queen == y_target) or abs(x_queen - x_target) == abs(y_queen - y_target):
        return 1
    else:
        return 2

def main() -> None:
    """
    Main function that runs the loop to read input and calculate the queen's moves.
    """
    while True:
        coordinates = input().split()

        # Exit condition: ['0', '0', '0', '0']
        if coordinates == ['0', '0', '0', '0']:
            break

        # Convert coordinates from string to int
        x_queen, y_queen, x_target, y_target = map(int, coordinates)

        # Call the function to calculate the moves and display the result
        result = queen_moves(x_queen, y_queen, x_target, y_target)
        print(result)

# # PT - BR
# def movimentos_dama(x_dama: int, y_dama: int, x_destino: int, y_destino: int) -> int:
#     """
#     Calcula o número mínimo de movimentos necessários para uma dama no xadrez 
#     ir de sua posição atual para o destino.

#     Args:
#         x_dama (int): Posição atual da dama no eixo x.
#         y_dama (int): Posição atual da dama no eixo y.
#         x_destino (int): Posição de destino no eixo x.
#         y_destino (int): Posição de destino no eixo y.

#     Returns:
#         int: O número de movimentos necessários (0, 1 ou 2).
#     """
#     if x_dama == x_destino and y_dama == y_destino:
#         return 0
#     elif (x_dama == x_destino) or (y_dama == y_destino) or abs(x_dama - x_destino) == abs(y_dama - y_destino):
#         return 1
#     else:
#         return 2

# def main() -> None:
#     """
#     Função principal que executa o loop para ler as entradas e calcular o número de movimentos da dama.
#     """
#     while True:
#         coordenadas = input().split()

#         # Condição de saída: ['0', '0', '0', '0']
#         if coordenadas == ['0', '0', '0', '0']:
#             break

#         # Conversão das coordenadas de string para int
#         x_dama, y_dama, x_destino, y_destino = map(int, coordenadas)

#         # Chamada da função que calcula os movimentos e exibição do resultado
#         resultado = movimentos_dama(x_dama, y_dama, x_destino, y_destino)
#         print(resultado)

if __name__ == "__main__":
    main()