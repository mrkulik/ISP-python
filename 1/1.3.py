import readfromfile
import savetofile


def storage():
    fullset = set()
    while True:
        string = raw_input('>>> ')
        splitedString = string.split()
        #if splitedString[0] == 'load':
        if splitedString[0] == 'add':
            for i in splitedString[1:]:
                fullset.add(i)
            print('Element added.')
        elif splitedString[0] == 'remove':
            for i in splitedString[1:]:
                fullset.remove(i)
            print('Element removed.')
        elif splitedString[0] == 'find':
            for i in splitedString[1:]:
                if i in fullset:
                    print (i)
                else:
                    print('There is no such element.')
        elif splitedString[0] == 'list':
            for i in fullset:
                print(i)
        #elif splitedString[0] == 'save':
        elif splitedString[0] == 'exit':
            break
        else:
            print ("Incorrect string.")


storage()