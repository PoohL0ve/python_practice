"""
    A simple function that prints:
        + - - - - + - - - - +
        |         |         |
        |         |         |
        |         |         |
        |         |         |
        + - - - - + - - - - +
        |         |         |
        |         |         |
        |         |         |
        |         |         |
        + - - - - + - - - - +
"""

# function for the line containing the plus sign and the dash
def line_across() :
    print("+ - - - - + - - - - +")

# function for the bars
def dash_down() :
    print("|         |         |")

# function to print the bars 4 times
def four_times() :
    dash_down()
    dash_down()
    dash_down()
    dash_down()

def print_grid() :
    line_across()
    four_times()
    line_across()
    four_times()
    line_across()
   



# test for function
if __name__ == "__main__" :
    print_grid()