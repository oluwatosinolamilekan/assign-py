def hailstone_sequence(initial_number):
    sequence = [initial_number]

    while sequence[-1] != 1:
        if sequence[-1] % 2 == 0:
            sequence.append(sequence[-1] // 2)
        else:
            sequence.append(3 * sequence[-1] + 1)

    return sequence

if __name__ == "__main__":
    initial_number = int(input("Enter the initial number for the hailstone sequence: "))
    result_sequence = hailstone_sequence(initial_number)
    print("Hailstone sequence:", result_sequence)
