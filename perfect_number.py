def is_perfect_number(num):
    divisors_sum = sum([i for i in range(1, num) if num % i == 0])
    return divisors_sum == num

if __name__ == "__main__":
    number_to_check = int(input("Please enter a number to check: "))
    if is_perfect_number(number_to_check):
        print(f"{number_to_check} is perfect")
    else:
        print(f"{number_to_check} is not perfect")