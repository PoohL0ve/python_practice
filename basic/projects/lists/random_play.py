
def all_targets_hit(attempts_for_each_target: list) -> bool:
    """Checks if any item in a list of sublists is True.

    Args:
        sublists (list): A list containing sublists to check.

    Returns:
        bool: True if any item is True, False otherwise.
    """
    size = len(attempts_for_each_target)
    count = 0
    for item in attempts_for_each_target:
        if any(item):
            count += 1

    if count == size:
        return True
    
    return False

if __name__ == "__main__":
    shots = [
        [True, False, False],
        [False, False, True]
    ]
    print(all_targets_hit(shots))