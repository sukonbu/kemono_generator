# -*- coding: utf-8 -*-
import random

list = ["け", "も", "の"]
nokemono = ["の", "け", "も", "の"]
mononoke = ["も", "の", "の", "け"]
mokemoke = ["も", "け", "も", "け"]
nokemono_list = ["", "", "", ""]
count = 0

while True:
    count += 1
    rand_str = list[random.randint(0, len(list) - 1)]
    print(rand_str, end='')
    nokemono_list.pop(0)
    nokemono_list.append(rand_str)
    # print(str(kemono_list) + str(nokemono_list))
    if nokemono_list == nokemono:
        print(" ")
        print("あなたは" + str(count) + "回でフレンズではなくなりました ")
        break
    if nokemono_list == mononoke:
        print(" ")
        print("あなたは" + str(count) + "回でシシ神になりました ")
        break
    if nokemono_list == mokemoke:
        print(" ")
        print("あなたは" + str(count) + "回でもけもけを通常召喚しました ")
        break
    if nokemono_list[1:] == list:
        print(" ")
        print("あなたは" + str(count) + "回でけものになりました ")
        break
