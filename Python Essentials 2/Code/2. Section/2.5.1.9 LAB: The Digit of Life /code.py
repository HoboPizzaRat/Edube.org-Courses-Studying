

# takes the number input
# sums all digits together
# repeats the given digitsum by calling itself
# until digitsum is single digit
def digitSumCalculator(digitSum):
    digits = list(str(digitSum))
    digit_sum = 0
    for digit in digits:
        digit_sum += int(digit)
    if digit_sum >= 10:
        return digitSumCalculator(digit_sum)
    else:
        return digit_sum



print("Give me your birthday on format YYYYMMDD: ")
input = int(input("give input:"))
result = digitSumCalculator(input)
print("Single digit sum is:", result)

