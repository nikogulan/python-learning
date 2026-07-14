months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ")

    if "/" in date:
        try:
            month, day, year = date.split("/")

            month = int(month)
            day = int(day)

            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{year}-{month:02}-{day:02}")
                break
        except ValueError:
            continue

    else:
        try:
            month, day, year = date.replace(",", " ").split()
            day = int(day)

            if month not in months or not 1 <= day <= 31 or not "," in date:
                continue

            month_number = months.index(month) + 1

            print(f"{year}-{month_number:02}-{day:02}")
            break

        except ValueError:
            continue
