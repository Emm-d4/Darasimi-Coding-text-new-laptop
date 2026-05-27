ROMAN_VALUES = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

def roman_to_int(s: str) -> int:
    s = s.upper()
    total = 0
    prev_value = 0

    for ch in reversed(s):
        if ch not in ROMAN_VALUES:
            raise ValueError(f"Invalid Roman numeral character: {ch}")
        value = ROMAN_VALUES[ch]
        if value < prev_value:
            total -= value
        else:
            total += value
            prev_value = value
    return total

def int_to_roman(num: int) -> str:
    if not (1 <= num <= 3999):
        raise ValueError("Number must be between 1 and 3999")

    mapping = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    result = []
    for value, symbol in mapping:
        while num >= value:
            result.append(symbol)
            num -= value
    return "".join(result)

def main():
    print("Roman Numeral Converter")
    print("1) Roman → Integer")
    print("2) Integer → Roman")
    choice = input("Choose 1 or 2: ").strip()

    if choice == "1":
        roman = input("Enter Roman numeral: ").strip()
        try:
            value = roman_to_int(roman)
            print(f"{roman} = {value}")
        except ValueError as e:
            print("Error:", e)
    elif choice == "2":
        num_str = input("Enter integer (1–3999): ").strip()
        try:
            num = int(num_str)
            roman = int_to_roman(num)
            print(f"{num} = {roman}")
        except (ValueError, TypeError) as e:
            print("Error:", e)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
