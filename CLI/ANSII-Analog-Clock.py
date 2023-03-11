import math
import time
import curses

def draw_clock(stdscr, hour, minute, second):
    # Clear the screen
    stdscr.clear()

    # Get the size of the terminal window
    height, width = stdscr.getmaxyx()

    # Calculate the center point of the screen
    center_y = height // 2
    center_x = width // 2

    # Calculate the radius of the clock face
    radius = min(center_y, center_x) - 4

    # Draw the clock face
    for y in range(-radius, radius + 1):
        x = int(math.sqrt(radius ** 2 - (y * 2 / 3) ** 2) * 2)
        stdscr.addstr(center_y + y, center_x - x // 2, '-' * x)

    # Draw the hour markings
    for i in range(12):
        angle = math.radians(i * 30)
        x = int((radius - 2) * math.sin(angle))
        y = int((radius - 2) * math.cos(angle) * 0.75)
        stdscr.addstr(center_y - y, center_x + x, str(i or 12))

    # Draw the minute markings
    for i in range(60):
        if i % 5:
            angle = math.radians(i * 6)
            x = int((radius - 1) * math.sin(angle))
            y = int((radius - 1) * math.cos(angle) * 0.75)
            stdscr.addstr(center_y - y, center_x + x, '.')

    # Draw the hour hand
    hour_angle = (hour % 12 + minute / 60) * 30
    hour_x = int((radius - 8) * math.sin(math.radians(hour_angle)))
    hour_y = int((radius - 8) * math.cos(math.radians(hour_angle)) * 0.75)
    stdscr.addstr(center_y - hour_y, center_x + hour_x, 'H')

    # Draw the minute hand
    minute_angle = minute * 6
    minute_x = int((radius - 4) * math.sin(math.radians(minute_angle)))
    minute_y = int((radius - 4) * math.cos(math.radians(minute_angle)) * 0.75)
    stdscr.addstr(center_y - minute_y, center_x + minute_x, 'M')

    # Draw the second hand
    second_angle = second * 6
    second_x = int((radius - 2) * math.sin(math.radians(second_angle)))
    second_y = int((radius - 2) * math.cos(math.radians(second_angle)) * 0.75)
    stdscr.addstr(center_y - second_y, center_x + second_x, 'S')

    # Refresh the screen
    stdscr.refresh()

def main(stdscr):
    # Turn off cursor blinking
    curses.curs_set(0)

    # Set the refresh rate to 50 milliseconds
    stdscr.timeout(50)

    # Loop forever
    while True:
        # Get the current time
        now = time.localtime()

        # Draw the clock
        draw_clock(stdscr, now.tm_hour, now.tm_min, now.tm_sec)

        # Wait for the next second
        stdscr.getch()

if __name__ == '__main__':
    curses.wrapper(main)