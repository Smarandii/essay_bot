# -*- coding: utf-8 -*-
from spellchecker import SpellChecker
import process

spell = SpellChecker()

symbols = [".", ",", ":", "-", "!", "?", " ", '', '\n']


def find_mistakes(s):
    responde = process.array_to_string(process.count_words(s))
    responde = process.array_to_string(words(responde))
    responde = process.array_to_string(comma(responde))
    responde = process.array_to_string(shortcut(responde))

    return responde


def shortcut(s):
    a = process.divide_to_words(s)

    def check_forshortcut(word):
        shortcuts = ["'re", "`re", "`m", "'m", "n`t", "n't", "`ll", "'ll"]
        for letter in word:
            if letter == "'" or letter == "`":
                for shortcut in shortcuts:
                    if shortcut in word:
                        return True
        return False

    responde = []
    for i in a:
        if check_forshortcut(i):
            responde.append(i + "(K1 ❌)(Shortcuts isn't allowed!)")
        else:
            responde.append(i)
    return responde


def comma(s):
    a = process.divide_to_words(s)
    yes_comma = ['which', 'but']
    no_comma = ['that', 'because']
    for i in range(len(a)):
        if a[i].lower() in yes_comma:
            if a[i - 2] != ',' and a[i - 1] != ',':
                a[i] = a[i] + '(K5 ❌)(Missing comma)'
        if a[i].lower() in no_comma:
            if a[i - 2] == ',' or a[i - 1] == ',':
                a[i] = a[i] + '(K5 ❌)(Extra comma)'
    return a


def words(a):
    a = process.divide_to_words(a)
    responde = []

    for i in a:
        if i == "i":
            responde.append(i + f"(К5 ❌)(Expect \"I\" instead of  \"i\" !) ")
        elif (i not in symbols) and spell.correction(i.lower()) != i.lower() and ('[' not in i) and (']' not in i):
            responde.append(i + f"(К5 ❌)")
        else:
            responde.append(i)

    return responde