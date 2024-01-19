product = 1

for i in range(8):
    number = int(input("Введите число: "))
    if number > 0:
        product *= number

print(f"Произведение положительных чисел: {product}")






product = 1
count = 0

while count < 8:
    number = int(input("Введите число: "))
    if number > 0:
        product *= number
        count += 1

print(f"Произведение положительных чисел: {product}")
