def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "Leap Year"
    else:
        return "Non-Leap Year"

if __name__ == "__main__":
    year = 2020
    print(leap_year(year))