# 20CE029 Misari Gami
# GitHub repository link : https://github.com/MisariGami/Programming-Assignment-Python

# You are given a string.Your task is to count the frequency of letters of the string and print the letters in descending order of frequency.
# If the following string is given as input to the program:
# aabbbccde
# Then, the output of the program should be:
# b 3
# a 2
# c 2
# d 1
# e 1


def freq(s1):
    dict = {}
    for n in s1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
str = input()
print(freq(str))
