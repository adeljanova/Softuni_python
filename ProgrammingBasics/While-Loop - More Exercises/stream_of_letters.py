letter = input()
sentence = ""
counter_c = 0
counter_o = 0
counter_n = 0
different = False
while letter != "End":
    letter = input()
    if letter != "+ - * / // % ^ $ # @ ! ? & ( ) { } [ ] | '\ ":
        different = True
        continue
    if different:
        if letter == "c":
            counter_c += 1
            if counter_c > 1:
                sentence += letter
        elif letter == "o":
            counter_o += 1
            if counter_o > 1:
                sentence += letter
        elif letter == "n":
            counter_n += 1
            if counter_n > 1:
                sentence += letter
    else:
        sentence += letter
        if counter_c >= 1 and counter_n >= 1 and counter_o >= 1:
            print(sentence)
            break
    letter = input()



