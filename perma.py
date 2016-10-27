#!/usr/bin/env python3
"""The PERMA-Profiler by Kern and Butler, but in Python!"""

import collections
import csv
import json
import os
import sys
import time

playing = True
mainMenu = True
quiz = False


class colour:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def anyKey():
    try:
        input("Press any key.")
    except SyntaxError:
        pass
    return


def cleanScreen():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')
    return


def doQuiz():
    cleanScreen()

    P = []
    N = []
    E = []
    R = []
    M = []
    A = []
    H = []
    LON = 0
    HAP = 0

    scale1 = (colour.BOLD + "0 = Never, 5 = About half the time, 10 = Always" +
              colour.END)
    scale2 = (colour.BOLD + "0 = Terrible, 5 = Average, 10 = Excellent" +
              colour.END)
    scale3 = (colour.BOLD + "0 = Not at all, 5 = Somewhat, 10 = Completely" +
              colour.END)

    questions = collections.OrderedDict()
    questions["How much of the time do you feel you are making progress"
              " towards accomplishing your goals?"] = scale1
    questions["How often do you become absorbed in what you are doing?"]\
        = scale1
    questions["In general, how often do you feel joyful?"] = scale1
    questions["In general, how often do you feel anxious?"] = scale1
    questions["How often do you achieve the important goals you have set for"
              " yourself?"] = scale1
    questions["In general, how would you say your health is?"] = scale2
    questions["In general, to what extent do you lead a purposeful and"
              " meaningful life?"] = scale3
    questions["To what extent do you receive help and support from others when"
              " you need it?"] = scale3
    questions["In general, to what extent do you feel that what you do in your"
              " life is valuable and worthwhile?"] = scale3
    questions["In general, to what extent do you feel excited and interested"
              " in things?"] = scale3
    questions["How lonely do you feel in your daily life?"] = scale3
    questions["How satisfied are you with your current physical health?"]\
        = scale3
    questions["In general, how often do you feel positive?"] = scale1
    questions["In general, how often do you feel angry?"] = scale1
    questions["How often are you able to handle your responsibilities?"]\
        = scale1
    questions["In general, how often do you feel sad?"] = scale1
    questions["How often do you lose track of time while doing something you"
              " enjoy?"] = scale1
    questions["Compared to others of your same age and sex, how is your"
              " health?"] = scale2
    questions["To what extent do you feel loved?"] = scale3
    questions["To what extent do you generally feel you have a sense of"
              " direction in your life?"] = scale3
    questions["How satisfied are you with your personal relationships?"]\
        = scale3
    questions["In general, to what extent do you feel contented?"] = scale3
    questions["Taking all things together, how happy would you say you are?"]\
        = scale3

    usr = input("What name should I store the results under? ")
    cleanScreen()

    active = True
    while active:
        i = 1
        for question, scale in questions.items():
            print(("%d / 23") % i)
            print("Pick a number between 0 and 10 that best represents your"
                  " answer regarding the past week.\n")
            print(scale)
            print(question)
            try:
                answer = int(input("\nAnswer: "))
            except ValueError:
                cleanScreen()
                print(colour.RED + "That is not a number." + colour.END)
                printLine()
                break
            else:
                if answer == 99:
                    active = False
                    return
                elif answer > 10:
                    cleanScreen()
                    print(colour.RED + "Answer is too big. Choose a number"
                          " between 0 and 10 only." + colour.END)
                    printLine()
                    break
                elif answer < 0:
                    cleanScreen()
                    print(colour.RED + "Answer is too small. Choose a number"
                          " between 0 and 10 only." + colour.END)
                    printLine()
                    break
                else:
                    if (i == 1) or (i == 5) or (i == 15):
                        A.append(answer)
                    elif (i == 2) or (i == 10) or (i == 17):
                        E.append(answer)
                    elif (i == 3) or (i == 13) or (i == 22):
                        P.append(answer)
                    elif (i == 4) or (i == 14) or (i == 16):
                        N.append(answer)
                    elif (i == 6) or (i == 12) or (i == 18):
                        H.append(answer)
                    elif (i == 7) or (i == 9) or (i == 20):
                        M.append(answer)
                    elif (i == 8) or (i == 19) or (i == 21):
                        R.append(answer)
                    elif i == 11:
                        LON = answer
                    elif i == 23:
                        HAP = answer

                    i += 1
                    cleanScreen()
                    continue

        while i == 24:
            overall = ((sum(P)+sum(E)+sum(R)+sum(M)+sum(A)+HAP)/15)
            P = (sum(P)/3)
            N = (sum(N)/3)
            E = (sum(E)/3)
            R = (sum(R)/3)
            M = (sum(M)/3)
            A = (sum(A)/3)
            H = (sum(H)/3)
            xdate = (time.strftime("%d/%m/%Y"))
            xtime = (time.strftime(" %H:%M:%S"))
            i += 1

        while i == 25:
            print(colour.BOLD + "Results:" + colour.END)
            print(xdate + xtime)
            print("\nPositive Emotion: %.2f" % P)
            print("Negative Emotion: %.2f" % N)
            print("Engagement: %.2f" % E)
            print("Relationships: %.2f" % R)
            print("Meaning: %.2f" % M)
            print("Accomplishment: %.2f" % A)
            print("Health: %.2f" % H)
            print("Lonliness: %d.00" % LON)
            print(("Overall Wellbeing: %0.2f") % overall)
            printLine()
            print("What would you like to do?")
            print("1. Export to JSON\n2. Export to CSV\n0. Cancel and"
                  " Continue\n99. Cancel and Exit")
            selection = input("\nSelection: ")

            if selection == "99":
                active = False
                exitGame()
            elif selection == "1":
                jsonData = {usr: {xdate: {xtime: {"P": P, "N": N, "E": E,
                                                  "R": R, "M": M, "A": A,
                                                  "H": H, "LON": LON,
                                                  "HAP": HAP, "OW": overall
                                                  }}}}
                with open('PERMA.json', 'a') as outfile:
                    json.dump(jsonData, outfile, sort_keys=True, indent=4,
                              separators=(',', ':'), ensure_ascii=False)
                cleanScreen()
                print(colour.GREEN + "JSON file saved" + colour.END)
                printLine()
            elif selection == "2":
                f = open("PERMA.csv", 'a')
                try:
                    thedatawriter = csv.writer(f)
                    thedatawriter.writerow(("NAME", "DATE", "P", "E", "R", "M",
                                            "A", "H", "N", "LON", "HAP", "OW"))
                    thedatawriter.writerow((usr, xdate, P, E, R, M, A, H, N,
                                            LON, HAP, overall))
                finally:
                    f.close()
                    cleanScreen()
                    print(colour.GREEN + "CSV file saved" + colour.END)
                    printLine()
            else:
                active = False
                return


def exitGame():
    cleanScreen()
    playing = False
    # print("Thank you for playing!")
    # anyKey()
    cleanScreen()
    sys.exit()


def invalidSelection():
    cleanScreen()
    print(colour.RED + "Invalid selection!" + colour.END)
    printLine()
    return


def printLine():
    print("__________________________\n")
    return


while playing:
    cleanScreen()

    while mainMenu:
        print(colour.BOLD + "Welcome!" + colour.END)
        print("\n1. Take Questionnaire\n99. Exit")
        menuChoice = input("\nSelection: ")

        if menuChoice == "99":
            exitGame()
        elif menuChoice == "1":
            cleanScreen()
            mainMenu = False
            quiz = True
        else:
            invalidSelection()

    while quiz:
        cleanScreen()
        print(colour.BOLD + "Welcome to the PERMA Profiler Questionnaire." +
              colour.END)
        print("This questionnaire has twenty-three questions and should take"
              " no longer than ten minute to complete.\n\n1. Start Quiz\n"
              "0. Back\n99. Exit")
        menuChoice = input("\nSelection: ")

        if menuChoice == "99":
            exitGame()
        elif menuChoice == "1":
            quiz = False
            doQuiz()
            quiz = True
        elif menuChoice == "0":
            quiz = False
            mainMenu = True
        else:
            invalidSelection()

__author__ = "Jinco"
__copyright__ = "Copyright 2016, Jinco"
__credits__ = ["Kern, M. L.", "Butler, J."]
__license__ = "GPLv3"
__version__ = "0.1.0"
__maintainer__ = "Jinco"
__status__ = "Development"
