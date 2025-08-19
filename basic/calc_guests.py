"""
    The program searches a string to find the first Integer
    and returns it. If no integer or 0 is found:
        not a number.
"""

def calculate_guest(guests_input: str) -> int | str:
    if not isinstance(guests_input, str) or not guests_input:
        return "not a number"

    found_number = False
    number_string = ""

    for char in guests_input:
        if char.isnumeric():
            number_string += char
            found_number = True
        elif found_number:
            break

    if number_string:
        if number_string == "0":
            return "not a number"
        return int(number_string)

    return "not a number"


if __name__ == "__main__":
    test_str = "0"
    print(calculate_guest(test_str))