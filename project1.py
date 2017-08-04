import random
from time import sleep

playing = True


def answering():
    answer = input("What letter is missing? ")
    return answer


while playing == True:
    listofletters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                     "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    missingletter = ""
    choosingletter = random.randint(0, len(listofletters) - 1)
    missingletter = listofletters[choosingletter]
    listofletters.remove(missingletter)
    print(listofletters)
    answer = answering()
    if answer.lower() == missingletter.lower():
        print("Correct")
        sleep(1)
    else:
        print("Wrong")
        sleep(1)
    print("\n" * 20)