sum = 0
file = open("purchases.csv", "r", encoding="utf-8")
header = file.readline()
for line in file:
    data = line.strip().split(";")
    name = data[0]
    price = float(data[1])
    count = int(data[2])
    cost = round(price * count, 2)
    sum = sum + cost
    print("Товар:", name, "Цена:", price, "Количество:", count, "Стоимость:", cost)
file.close()
print("Общая сумма:", round(sum, 2))
