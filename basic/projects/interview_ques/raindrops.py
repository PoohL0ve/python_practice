"""Raindrops

Display string values that mimics sounds based on the 'clean'
division of values
"""

# Store sounds
sounds = {"pling": 3, "plang": 5, "plong": 7}

def get_sound(number: int) -> str:
    """Builds a raindrop sound based on whether the given
    input can be cleanly divisible (no-remainders) by the
    values in a given set.
    """

    # Check that number is an integer
    if not isinstance(number, int):
        raise ValueError("The value must be an integer.")

    # Store values to avoid duplicates
    # unique_values = set(sounds.values())

    raindrop = ""

    for key, value in sounds.items():
        if number % value == 0:
            raindrop += key.capitalize()

    if len(raindrop) == 0:
        raindrop += str(number)

    return raindrop

print(get_sound(34))
