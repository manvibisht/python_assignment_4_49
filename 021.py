def sum_of_digits(n):
    total = sum(int(d) for d in str(abs(n)))
    print("Sum of digits:", total)

sum_of_digits(456)