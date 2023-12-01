import time
import sys


def move_ascii_art_right(ascii_art, max_spaces, delay=0.1):
    lines = ascii_art.split("\n")
    for spaces in range(max_spaces):
        print("\n" * 100)  # Move down 100 lines to clear the previous art
        print("\033[F" * (len(lines) + 100))  # Move cursor back up
        print("\n".join([" " * spaces + line for line in lines]))
        time.sleep(delay)
        sys.stdout.flush()  # Flush output for real-time display


ascii_art = """
    ______
        _\ _~-\___
=  = ==(____AA____D
            \_____\___________________,-~~~~~~~`-.._
            /     o O o o o o O O o o o o o o O o  |\_
            `~-.__ NaN-Air ___..----..                  )
                    `---~~\___________/------------```````
                    =  ===(_________D
"""

# Move the ASCII art to the right over 20 spaces with a 0.1-second delay
move_ascii_art_right(ascii_art, 20)
