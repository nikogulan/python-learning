def main():
    meal = convert(input("What time is it? "))
    if 7.00 <= meal <= 8.00:
        print("breakfast time")
    elif 12.00 <= meal <= 13.00:
        print("lunch time")
    elif 18.00 <= meal <= 19.00:
        print("dinner time")
    else:
        pass


def convert(time):
    if time.endswith("pm"):
        time_pm = time.removesuffix("pm")
        h, m = time_pm.split(":")
        hours = int(h)
        minutes = int(m)
        return float(((hours + 12) * 60 + minutes) / 60)
    elif time.endswith("am"):
        time_am = time.removesuffix("am")
        h, m = time_am.split(":")
        hours = int(h)
        minutes = int(m)
        return float((hours * 60 + minutes) / 60)
    else:
        h, m = time.split(":")
        hours = int(h)
        minutes = int(m)
        return float((hours * 60 + minutes) / 60)


if __name__ == "__main__":
    main()
