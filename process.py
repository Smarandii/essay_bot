def array_to_string(a):
    responde = ''
    for i in a:
        responde = responde + i
    return responde

def count_words(s):
    symbols = [".", ",", ":", "-", "!", "?", " ", '']
    a = divide_to_words(s)
    responde = []
    counter = 0

    for i in a:
        if counter < 275:
            if i not in symbols:
                counter += 1
            responde.append(i)
        else:
            break

    if counter < 180:
        responde.append("Less than 180 words!")
        return "\nless than 180 words!\n"
    if counter >= 180 and counter < 275:
        responde.append(f"\n \n[words: {str(counter)}]")
        return responde
    if counter > 275:
        responde.append("\n \n{more than 275 words!}")
        return responde


def divide_to_words(s):
    symbols = [".", ",", ":", "-", "!", "?", " ", '']
    w = ''
    words = []
    for i in range(len(s)):
        if s[i] == "\n":
            if w != '':
                words.append(w)
                w = ''
            words.append('\n')

        elif s[i] in symbols:
            if w != '':
                words.append(w)
                w = ''
            words.append(s[i])
        else:
            w = w + s[i]
    words.append(w)
    return words


def count_mistakes(s):
    if "less than 180 words!" in s:
        return '\n0 / 14'

    m1 = 0
    m2 = 0
    m3 = 0
    m4 = 0
    m5 = 0
    k1 = 0
    k2 = 0
    k3 = 0
    k4 = 0
    k5 = 0
    mark = 0

    for i in range(len(s)):
        if (s[i].lower() == 'k' or s[i].lower() == 'к') and s[i + 1].isdigit():
            if int(s[i + 1]) == 1:
                k1 = k1 + 1
            elif int(s[i + 1]) == 2:
                k2 = k2 + 1
            elif int(s[i + 1]) == 3:
                k3 = k3 + 1
            elif int(s[i + 1]) == 4:
                print(s[i - 4] + s[i - 3])
                k4 = k4 + 1
            elif int(s[i + 1]) == 5:
                k5 = k5 + 1

    if k1 <= 1:
        mark += 3
        m1 = 3
    elif k1 == 2:
        mark += 2
        m1 = 2
    elif k1 == 3:
        mark += 1
        m1 = 1
    elif k1 > 3:
        m1 = 0

    if k2 == 0:
        mark += 3
        m2 = 3
    elif k2 == 1:
        mark += 2
        m2 = 2
    elif k2 == 2:
        mark += 1
        m2 = 1
    elif k2 >= 3:
        m2 = 0

    if k3 < 1:
        mark += 3
        m3 = 3
    elif k3 == 2 or k3 == 3:
        mark += 2
        m3 = 2
    elif k3 == 4:
        mark += 1
        m3 = 1
    elif k3 > 4:
        m3 = 0

    if k4 < 1:
        mark += 3
        m4 = 3
    elif k4 == 2:
        mark += 2
        m4 = 2
    elif k4 == 3 or k4 == 4:
        mark += 1
        m4 = 1
    elif k4 > 4:
        m4 = 0

    if k5 <= 1:
        mark += 2
        m5 = 2
    elif k5 == 2:
        mark += 2
        m5 = 2
    elif k5 == 3:
        mark += 1
        m5 = 1
    elif k5 > 3:
        m5 = 0

    responde = f'''

Good job!

K1 - {m1} / 3
K2 - {m2} / 3
K3 - {m3} / 3
K4 - {m4} / 3
K5 - {m5} / 2

Mistakes count:

K1 - {k1} 
K2 - {k2}
K3 - {k3}
K4 - {k4}
K5 - {k5} 

{str(mark)} / 14
'''
    return responde
