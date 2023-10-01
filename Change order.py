listData = ["Lewis", "Russel", "Alonso", "Leclerc", "Alex"]

a = 0

while a < (len(listData) - 1) // 2:
    b = listData[a]
    listData[a] = listData[len(listData) - 1 - a]
    listData[len(listData) - a - 1] = b
    a += 1

print(listData)