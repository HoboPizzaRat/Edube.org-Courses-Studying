def is_prime(num):
    for divider in range(2, num//2):
        if num % divider == 0:
            return False
    return True

for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()
