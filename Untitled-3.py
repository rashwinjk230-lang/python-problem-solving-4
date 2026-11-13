
def digit_sum(number):
    number = abs(number)

    if number < 10:
        return number

    return (number % 10) + digit_sum(number // 10)


print("Sum of digits:", digit_sum(5824))

print(
    digit_sum(7),
    digit_sum(0),
    digit_sum(1000),
    digit_sum(99999)
)
