"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """

    letters = ("A","B","C","D")
    for i in range(number):
        yield letters[i%len(letters)]



def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    
    rows = number // 4 # 4 seats per row
    additional = number % 4 # incomplete rows
    letters = generate_seat_letters(4)
    
    for i in range(1, rows+1):
        i += 1 if i >= 13 else 0
        for j in ("A","B","C","D"):
            yield f"{i}{j}"
    for _ in range(additional):
        yield f"{rows+1}{next(letters)}"

    # yield from (f"{i if i < 13 else i + 1}{_}" for i in range(1,rows+1) for _ in letters)
    # yield from (f"{rows+1}{_}" for _ in generate_seat_letters(additional))
    
    # oof. 2 lines and I used ChatGPT. and the variables take up lines! 
    # And it doesn't work
            
        
    
    # letters = generate_seat_letters(number)

    # number = number if number < 13 else number + 1
    
    # for row in range(1, (number // 4)+1):
    #     if row == 13:
    #         continue
    #     for letter in range(4):
    #         yield f"{row}{next(letters)}" # If letters are constant, why not use tuple of letters?

    # for seat in range(1, number % 4 + 1):
    #     row = number // 4 + 1
    #     if row == 13:
    #         row += 1
    #     yield f"{row}{next(letters)}"

    

def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """

    return dict(zip(passengers, generate_seats(len(passengers)))) # ouch. 

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    return (f"{_}{flight_id}".ljust(12,"0") for _ in seat_numbers)
