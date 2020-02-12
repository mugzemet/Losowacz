import random

print("Wprowadź kolejno dane do losowania. \nJeżeli chcesz zakończyć wprowadzanie danych - naciśnij Enter.\n")

data = []
random_data = []


def start():
    ask = input("Podaj pierwszy tytuł: ")
    if ask != "":
        data.append(ask)
    else:
        fail()

def cont():
    ask = input("Podaj kolejny tytuł: ")
    while ask != "":
        data.append(ask)
        ask = input("Podaj kolejny tytuł: ")
    else:
        end()

def end():
    print("\nOk, mamy to. Losowacz wygenerował Twoją przypadkową listę:")
    tries = len(data)
    while tries > 0:
        losowacz = random.choice(data)
        random_data.append(losowacz)
        data.remove(losowacz)
    else:
        print(random_data)
        input("\n\nAby zakończyć program, naciśnij klawisz Enter.")

def fail():
    print("Przykro mi, nie mam z czego losować.")
    input("\n\nAby zakończyć program, naciśnij klawisz Enter.")

start()
cont()



