n = int(input("Enter a positive whole number: "))

total = 0

for number in range(1, n + 1):
    total = total + number

print(f"Sum of 1 to {n} = {total}")
