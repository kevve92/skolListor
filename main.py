listan = []
keep_alive = True

while keep_alive:
    print('''vad vill du göra
    1. lägga till elev
    2. ta bort elev
    3. se listan 
    0. stäng av programmet

       ''')

    number_from_user = int(input())
    if number_from_user == 1:
        print("vad heter eleven du vill lägga till? ")
        listan.append(input())

    elif number_from_user == 2:
        print("vilken av eleverna vill du ta bort? ")
        listan.remove(input())

    elif number_from_user == 3:
        listan.sort()
        print(listan)
    elif number_from_user == 0:
        print("hej då ha ett bra liv :) ")
        keep_alive = False

    else:
        print("jag förstår inte vad du menar försök igen:) ")