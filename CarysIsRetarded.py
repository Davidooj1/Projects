import re
import csv
import time

intro = input("Mode: Search or Rapid Fire?")


if intro.lower().strip() == "rapid fire":
    def main():
        main_list = []
        chair_list = []
        minutes_list = []
        apologies_list = []
        print("y - Yes, attended\n"
              "n - No, didn't attend\n"
              "a - apology\n"
              "c - Chairman\n"
              "m - Minutes\n"
              "done/finish/quit/end - to end and print list)")

        with open ("pafra.csv") as file:
            myfile = csv.reader(file)

            for xx in myfile:
                check = input(f"{xx}?")
                if check.lower() == "y":
                    main_list.append(xx)
                elif check.lower() == "c":
                    chair_list.append(xx)
                elif check.lower() == "m":
                    minutes_list.append(xx)
                elif check.lower() == "a":
                    apologies_list.append(xx)
                elif check.lower() == "done" or check.lower() == "finish" or check.lower() == "quit" or check.lower() == "end":
                    break
                elif check.lower() == "n":
                    pass
                else:
                    print("Wrong Entry Please Start Again")
                    main()

            print(f"\nChair:")
            for chair in chair_list:
                print(", ".join(chair))

            print(f"\nMinutes:")
            for minutes in minutes_list:
                print(", ".join(minutes))

            print(f"\nAttendees:")
            for names in main_list:
                print(", ".join(names))

            print(f"\nApologies:")
            for apologies in apologies_list:
                print(", ".join(apologies))

            time.sleep(12000)
    main()


# Search Mode

if intro.lower().strip() == "search":

    print("THIS IS CAPS SENSETIVE")

    with open("pafra.csv") as file:
        myfile = csv.reader(file)

        ask = ""
        ask2 = ""
        main_list2 = []
        chair_list2 = []
        minutes_list2 = []
        apologies_list2 = []

        chairask = input("Who chaired the meeting?")
        minutesask = input("Who did the minutes?")
        for sections in myfile:
            for names in sections:
                match = re.search(chairask, names)
                match2 = re.search(minutesask, names)
                if match:
                    chair_list2.append(sections)
                elif match2:
                    minutes_list2.append(sections)

    print("For Attendees and Apologies, enter the first name and the first letter of the surname for each.")

    while ask != "stop" and ask != "done" and ask != "finish" and ask != "quit":
        with open("pafra.csv") as file:
            myfile = csv.reader(file)
            ask = input("Enter Attendees:")
            for yy in myfile:
                for zz in yy:
                    matches = re.search(ask, zz)
                    if matches:
                        main_list2.append(yy)

    while ask2 != "stop" and ask2 != "done" and ask2 != "finish" and ask2 != "quit":
        with open("pafra.csv") as file:
            myfile = csv.reader(file)
            ask2 = input("Enter Apologies:")
            for yy2 in myfile:
                for zz2 in yy2:
                    matches2 = re.search(ask2, zz2)
                    if matches2:
                        apologies_list2.append(yy2)

    print(f"\nChair:")
    for chair2 in chair_list2:
        print(", ".join(chair2))

    print(f"\nMinutes:")
    for minutes2 in minutes_list2:
        print(", ".join(minutes2))

    print(f"\nAttendees:")
    for names in main_list2:
        print(", ".join(names))

    print(f"\nApologies:")
    for apologies in apologies_list2:
        print(", ".join(apologies))






















#          ask = input("Enter name of person in meeting: ")
#          for yy in myfile:
#              for zz in yy:
#                  matches = re.search(ask.capitalize(), zz)
#                  if matches:
#                      here_listyy.append(yy)
#   print(here_listyy)







































#chairask = input("Who Chaired the meeting?")
#        minutesask = input("Who did the minutes?")
#        for sections in myfile:
#            for names in sections:
#                match = re.search(chairask, names)
#                match2 = re.search(minutesask, names)
#                if match:
#                    chair_list2.append(sections)
#                elif match2:
#                    minutes_list2.append(sections)




















