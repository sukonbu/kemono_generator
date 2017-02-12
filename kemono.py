# -*- coding: utf-8 -*-
import random

list = ["け", "も", "の"]
nokemono = ["の", "け", "も", "の"]
mononoke = ["も", "の", "の", "け"]

nokemono_list = ["", "", "", ""]
kemono_list = ["", "", ""]
nokemono_count = 0
count = 0

while True:
    count += 1
    rand_str = list[random.randint(0, len(list) - 1)]
    print(rand_str, end='')
    kemono_list.pop(0)
    kemono_list.append(rand_str)
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
    if kemono_list == list:
        print(" ")
        print("あなたは" + str(count) + "回でけものになりました ")
        break
