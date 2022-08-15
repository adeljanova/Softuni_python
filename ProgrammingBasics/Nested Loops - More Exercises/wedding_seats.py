last_sector = input()
first_sector_rows = int(input())
odd_row_places = int(input())
counter = 0
for sector in range(ord('A'), ord(last_sector) + 1):
    if sector > ord('A'):
        first_sector_rows += 1
    for rows in range(1, first_sector_rows + 1):
        if rows % 2 != 0:
            for place in range(97, odd_row_places + 97):
                print(f"{chr(sector)}{rows}{chr(place)}")
                counter += 1
        else:
            for place in range(97, odd_row_places + 99):
                print(f"{chr(sector)}{rows}{chr(place)}")
                counter += 1
print(counter)