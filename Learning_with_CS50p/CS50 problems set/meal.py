def main():
    times = input("What time is it? ")
    hours = convert(times)

    if 7.00 <= hours <= 11.00:
        print("breakfast time")
    elif 12.00 <= hours <= 18.00:
        print("lunch time")
    elif 18.01 <= hours <= 22.00:
        print("dinner time")
    else: print("")

def convert(times):
    hours, minutes = times.split(":")
    converted_time = float(hours) + float(minutes) / 60
    return converted_time

if __name__ == "__main__":
    main()

