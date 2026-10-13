"""
Generates a seating chart, marking unavailable seats loaded from a text file.
Author: Nicholas Foster
"""

unavailable_seats = {}

# TODO: a try/except block to load the dictionary with the unavailable seats

"""
Prints a 10x10 seating chart, replacing unavailable seats with an "X"
Author: Nicholas Foster
"""
rows = "ABCDEFGHIJ"
columns = range(10)

for row in rows:
    for col in columns:
        seat = f"{row}{col}"

        if seat in unavailable_seats:
            print("[X]", end=" ")
        else:
            print(f"[{seat}]", end=" ")
            
    print()