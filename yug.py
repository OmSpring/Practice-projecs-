def get_yuga(year):
    if year >= 3102:
        # Calculate the years elapsed since the beginning of Kali Yuga
        years_elapsed = year - 3102

        if years_elapsed < 1296:
            return "Kali Yuga"
        elif years_elapsed < 2592:
            return "Dvapara Yuga"
        elif years_elapsed < 3888:
            return "Treta Yuga"
        else:
            return "Satya Yuga"
    else:
        return "The year is before the beginning of Kali Yuga"

# Replace 2023 with the year you want to check
year = int (input ("Enter the year to check of which yug it was existant in "))
yuga = get_yuga(year)
print(f"The year {year} belongs to {yuga}")