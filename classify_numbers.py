def classify_numbers_in_range(upper_limit):
    for num in range(2, upper_limit + 1):
        divisors_sum = sum([i for i in range(1, num) if num % i == 0])
        if divisors_sum < num:
            print(f"{num} is deficient")
        elif divisors_sum == num:
            print(f"{num} is perfect")
        else:
            print(f"{num} is abundant")

if __name__ == "__main__":
    upper_limit = int(input("Enter the upper number for the range: "))
    classify_numbers_in_range(upper_limit)
