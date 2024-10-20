# EN - US
def main() -> None:
    """
    Reads a number of inputs and counts how many are within the range 10 to 20 (inclusive)
    and how many are outside that range.
    """
    in_count = 0
    out_count = 0
    total_numbers = int(input())

    for _ in range(total_numbers):
        number = int(input())
        if 10 <= number <= 20:
            in_count += 1
        else:
            out_count += 1

    print(f"{in_count} in")
    print(f"{out_count} out")

# # PT - BR
# def main() -> None:
#     """
#     Lê uma quantidade de entradas e conta quantas estão dentro do intervalo de 10 a 20 (inclusive)
#     e quantas estão fora desse intervalo.
#     """
#     contador_in = 0
#     contador_out = 0
#     total_numeros = int(input())

#     for _ in range(total_numeros):
#         numero = int(input())
#         if 10 <= numero <= 20:
#             contador_in += 1
#         else:
#             contador_out += 1

#     print(f"{contador_in} in")
#     print(f"{contador_out} out")

if __name__ == "__main__":
    main()