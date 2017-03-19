from multiprocessing.dummy import dict
import readfromfile
import lab12
import re


def string_split(string):
    string = string.replace(',', ' ')
    string = string.replace('.', ' ')
    string = string.split()
    return string


def word_in_string(splitedString):
    dictionary = dict()
    for item in splitedString:
        if item in dictionary.keys():
            dictionary[item] += 1
        else:
            dictionary[item] = 1
    return dictionary


def density(string, splitedString):
    counter = 0
    for i in string:
        if i == '.':
            counter += 1
    den = float(counter) / len(splitedString)
    return den


def medium(medium_string):
    medium_string = lab12.qsort(medium_string)
    print medium_string
    return medium_string[int((len(medium_string))/2)]


def grammas(splitedString, n, k):
    gramsDict = dict()#dict for all n-gramms
    for j in range(len(splitedString)):#check all words
        if len(splitedString[j]) >= n:#if word > n-gramm
            for x in range(len(splitedString[j]) - n):#find n-gramm in word
                sr = splitedString[j][x: x + n]#cut n-gramm from word
                if gramsDict.get(sr, 'n') == 'n':
                    gramsDict[sr] = 1
                else:
                    a = gramsDict[sr]#if n-gramm already exist, a++
                    a += 1
                    gramsDict[sr] = a
        else:
            continue
    sortedGramsDict = sorted(gramsDict.items(), key=lambda y: y[1], reverse=True)#sort of dict
    list1 = [sortedGramsDict[i][1] for i in range(len(sortedGramsDict))]
    print('Top {} {}-gramm:'.format(k, n))
    for i in range(k):
        o = list1[0]
        p = list1.count(o)
        print(i + 1, ':')
        for j in range(p):
            list1.remove(o)
            print(sortedGramsDict[0])
            del sortedGramsDict[0]
        if len(sortedGramsDict) == 0:
            break


def start():
    string = readfromfile.read_from_file('text.txt')
    n = input('Enter n:')
    k = input('Enter k:')
    medium_string = readfromfile.read_from_file('sort.txt').split()
    for item in medium_string:
        medium_string[medium_string.index(item)] = int(item)
    splitedString = string_split(string)
    dictionary = word_in_string(splitedString)
    print('Repeating words in text:')
    for i in dictionary:
        print('{}:{}'.format(i, dictionary[i]))
    print('Density:', density(string, splitedString))
    print('Medium:', medium(medium_string))
    grammas(splitedString, n, k)


start()