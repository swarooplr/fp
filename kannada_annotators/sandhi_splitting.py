# -*- coding: utf-8 -*-


def lopa(wordset,word):
    splits = []
    if len(word) <= 2:
        return splits

    for i in range(3,len(word)-2):

        if ord(word[i]) >= 3262 and ord(word[i]) <= 3286:
            possible_first = set()
            possible_second = set()

            possible_second.add(unichr(ord(word[i]) - 56) + word[i + 1:])

            deeraga_sandhis =  (3262, 3264, 3266, 3271, 3275)
            if ord(word[i]) in deeraga_sandhis:
                possible_second.add(unichr(ord(word[i]) - 57) + word[i + 1:])

            possible_first.add(word[:i])
            for j in range(3262,3287):
                    first = word[:i]+unichr(j)
                    possible_first.add(first)

            for first in possible_first:
                for second in possible_second:
                    if wordset.is_present(first) and wordset.is_present(second):
                        splits.append((first,second))
    return splits


def aagama(wordset,word):
    splits = []

    if len(word) <= 2:
        return splits

    # 3247 is ಯ 3253 is ವ

    for i in range(2,len(word)-1):
        if ord(word[i]) == 3247 or ord(word[i]) == 3253:
            if ord(word[i+1]) >= 3262 and ord(word[i+1]) <= 3286:
                first = word[:i]
                second = unichr(ord(word[i+1]) - 56) + word[i+2:]
                if wordset.is_present(first) and wordset.is_present(second):
                    splits.append((first,second))
            else:
                first = word[:i]
                second = unichr(3205) + word[i + 1:]
                if wordset.is_present(first) and wordset.is_present(second):
                    splits.append((first, second))

    return splits


def aadesha(wordset,word):
    splits = []

    if len(word) <=2:
        return splits

    for i in range(2,len(word)-2):
        if ord(word[i]) == 3223 or ord(word[i]) == 3238 or ord(word[i]) == 3244:
            first = word[:i]
            second = unichr(ord(word[i])-2) + word[i+1:]
            if wordset.is_present(first) and wordset.is_present(second):
                splits.append((first,second))

    return splits


def savarnadeerga(wordset,word):
    splits = []

    if len(word) <= 2:
        return splits

    for i in range(2,len(word)-2):
        if ord(word[i]) == 3262 or ord(word[i]) == 3264 or ord(word[i]) == 3266:
            possible_first = set()
            possible_second = set()

            possible_first.add(word[:i+1])
            if ord(word[i]) == 3262:
                possible_first.add(word[:i])
            else:
                possible_first.add(word[:i]+unichr(ord(word[i])-1))

            deeraga_sandhis =  (3262, 3264, 3266, 3271, 3275)
            possible_second.add(unichr(ord(word[i]) - 56) + word[i + 1:])
            if ord(word[i]) in deeraga_sandhis:
                possible_second.add(unichr(ord(word[i])-57) + word[i+1:])
            else:
                possible_second.add(unichr(ord(word[i])-55) + word[i+1:])


            for first in possible_first:
                for second in possible_second:
                    if wordset.is_present(first) and wordset.is_present(second):
                        splits.append((first, second))

    return splits


def guna(wordset, word):
    splits = []

    if len(word) <= 2:
        return splits

    for i in range(2, len(word) - 1):
        if ord(word[i]) == 3271:
            possible_first = set()
            possible_second = set()
            possible_first.add(word[:i])
            possible_first.add(word[:i]+unichr(3262))
            possible_second.add(unichr(3207)+word[i+1:])
            possible_second.add(unichr(3208)+word[i+1:])
            for first in possible_first:
                for second in possible_second:
                    if wordset.is_present(first) and wordset.is_present(second):
                        splits.append((first, second))

        if ord(word[i]) == 3275:
            possible_first = set()
            possible_second = set()
            possible_first.add(word[:i])
            possible_first.add(word[:i] + unichr(3262))
            possible_second.add(unichr(3209) + word[i + 1:])
            possible_second.add(unichr(3210) + word[i + 1:])
            for first in possible_first:
                for second in possible_second:
                    if wordset.is_present(first) and wordset.is_present(second):
                        splits.append((first, second))

        # if ord(word[i]) == 3277:
        #     possible_first = set()
        #     possible_second = set()
        #     possible_first.add(word[:i])
        #     possible_first.add(word[:i] + unichr(3262))
        #     possible_second.add(unichr(3211) + word[i + 1:])
        #     for first in possible_first:
        #         for second in possible_second:
        #             if wordset.is_present(first) and wordset.is_present(second):
        #                 splits.append((first, second))
    return splits

def vurdhi(wordset, word):
    splits = []

    if len(word) <= 2:
        return splits

    for i in range(2, len(word) - 1):
        if ord(word[i]) == 3272:
            possible_first = set()
            possible_second = set()
            possible_first.add(word[:i])
            possible_first.add(word[:i]+unichr(3262))
            possible_second.add(unichr(3215)+word[i+1:])
            possible_second.add(unichr(3216)+word[i+1:])
            for first in possible_first:
                for second in possible_second:
                    if wordset.is_present(first) and wordset.is_present(second):
                        splits.append((first, second))

        if ord(word[i]) == 3276:
            possible_first = set()
            possible_second = set()
            possible_first.add(word[:i])
            possible_first.add(word[:i] + unichr(3262))
            possible_second.add(unichr(3219) + word[i + 1:])
            possible_second.add(unichr(3220) + word[i + 1:])
            for first in possible_first:
                for second in possible_second:
                    if wordset.is_present(first) and wordset.is_present(second):
                        splits.append((first, second))

    return splits


def yann(wordset, word):
    splits = []

    if len(word) <= 2:
        return splits

    for i in range(2, len(word) - 3):
        if ord(word[i]) == 3277 and ord(word[i+1]) == 3247:
            possible_first = set()
            possible_second = set()
            possible_first.add(word[:i]+unichr(3263))
            possible_first.add(word[:i]+unichr(3264))

            if 3211 <= ord(word[i+2]) <= 3253:
                possible_second.add(unichr(3205)+word[i+2:])
                possible_second.add(unichr(3206)+word[i+2:])
            elif ord(word[i+2]) == 3265 or ord(word[i+2]) == 3266:
                possible_second.add(unichr(3209)+word[i+3:])
                possible_second.add(unichr(3210)+word[i+3:])
            else:
                possible_second.add(unichr(3205) + word[i + 3:])
                possible_second.add(unichr(3206) + word[i + 3:])

            for first in possible_first:
                for second in possible_second:
                    if wordset.is_present(first) and wordset.is_present(second):
                        splits.append((first, second))

        if ord(word[i]) == 3277 and ord(word[i+1]) == 3253:
            possible_first = set()
            possible_second = set()
            possible_first.add(word[:i]+unichr(3265))
            possible_first.add(word[:i]+unichr(3266))

            if 3211 <= ord(word[i+2]) <= 3253:
                possible_second.add(unichr(3205)+word[i+2:])
                possible_second.add(unichr(3206)+word[i+2:])
            elif ord(word[i+2]) == 3265 or ord(word[i+2]) == 3266:
                possible_second.add(unichr(3209)+word[i+3:])
                possible_second.add(unichr(3210)+word[i+3:])
            else:
                possible_second.add(unichr(3205) + word[i + 3:])
                possible_second.add(unichr(3206) + word[i + 3:])

            for first in possible_first:
                for second in possible_second:
                    if wordset.is_present(first) and wordset.is_present(second):
                        splits.append((first, second))

        if ord(word[i]) == 3277 and ord(word[i+1]) == 3248:
            possible_first = set()
            possible_second = set()
            possible_first.add(word[:i]+unichr(3265))
            possible_first.add(word[:i]+unichr(3266))

            if 3211 <= ord(word[i+2]) <= 3253:
                possible_second.add(unichr(3205)+word[i+2:])
                possible_second.add(unichr(3206)+word[i+2:])
            elif ord(word[i+2]) == 3265 or ord(word[i+2]) == 3266:
                possible_second.add(unichr(3209)+word[i+3:])
                possible_second.add(unichr(3210)+word[i+3:])
            else:
                possible_second.add(unichr(3205) + word[i + 3:])
                possible_second.add(unichr(3206) + word[i + 3:])

            for first in possible_first:
                for second in possible_second:
                    if wordset.is_present(first) and wordset.is_present(second):
                        splits.append((first, second))



    return splits















