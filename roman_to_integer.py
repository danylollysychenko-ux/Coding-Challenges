roman_to_integer = {"I": 1,
                    "V": 5,
                    "X": 10,
                    "L": 50,
                    "C": 100,
                    "D": 500,
                    "M": 1000}


enter = input("Enter roman numerals: ").upper().strip()
n = len(enter)
total = 0

for i in range(n - 1):
    current_val = roman_to_integer[enter[i]]
    next_val = roman_to_integer[enter[i + 1]]

    if current_val < next_val:
        total -= current_val

    else:
        total += current_val

total += roman_to_integer[enter[n - 1]]
print(total)