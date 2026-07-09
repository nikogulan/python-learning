grocerys = {}

while True:
    try:
        item = input().lower()
        if item not in grocerys:
            grocerys[item] = 1
        elif item in grocerys:
            grocerys[item] += 1
    except EOFError:
        break

sorted_list = sorted(grocerys.items())

for item, count in sorted_list:
    print(count, item.upper())



