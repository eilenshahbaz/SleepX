""" Sleep application to determine sleep and wakeup time"""

from calc import *
import time
import sys


def wake_up():
    hour = int(time.strftime("%H"))
    mins = int(time.strftime("%M"))
    hour, mins = wake_up_time(hour, mins, 5)
    mins = "0{0}".format(mins) if mins < 10 else mins
    print("You should wake up at {0}:{1}".format(hour, mins))


def sleep_down(hour, minutes):
    hrs = int(hour)
    mins = int(minutes)
    hrs, mins = when_to_sleep(hrs, mins, 6)
    mins = "0{0}".format(mins) if mins < 10 else mins
    print("You should go to sleep at {0}:{1} if you want".format(hrs, mins) +
          "to wake up at {0}:{1}".format(hour, minutes))


if __name__ == '__main__':
    # try:
    print("Welcome! Would you like to determine when to "
          "1) wake up or  2) go to sleep?\n"
          "Please enter 1 or 2")
    for line in sys.stdin:
        try:
            line = line.strip()
            if line == "exit":
                break
            elif line == "1":
                wake_up()
            elif line == "2":
                times = input("When would you like to wake up? (ex. '8:00')\n")
                times = times.strip().split(":")
                sleep_down(times[0], times[1])
            else:
                print("Please choose 1) wake up or 2) sleep down "
                      "or 'exit' to quit")
        except (AssertionError, IndexError):
            print("Enter 'exit' to quit or provide a valid input")
