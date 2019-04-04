#! /usr/bin/env python

import os

print('Welcome to the file Control System')
print('\t1  >> Create a new file')
print('\t2  >> Get the current working directory')
print('\t3  >> Change directory')
print('\t4  >> List the contents of the current directory')
print('\t5  >> Read the contents of a file')
print('\t6  >> Copy an existing file into a new directory')
print('\t7  >> Exit system')
def inputcode():
    inp = input('Please enter an option: ')
    inp = int(inp)
    while inp:
        if inp == 1:
            dirname = input('Please enter name of directory you wish to create: ')
            if dirname:
                os.mkdir('./ %s' % dirname)
                print('Directory > %s < successfully created' % dirname)
                inputcode()
            else:
                print('Please try again')
                inputcode()
        elif inp == 2:
            print(' Your current working directory is:\n')
            print(os.getcwd(),'\n')
            inputcode()
        elif inp == 3:
            newpath = input('New path: ')
            os.chdir('%s' % newpath)
            print('Your location is now: ', os.getcwd())
            inputcode()
        elif inp == 4:
            print('Directory contents:\n')
            print(os.listdir('.'),'\n')
            inputcode()
        elif inp == 5:
            filename = input('Please enter the name of the file you wish to open, including the extension:')
            file = os.open("%s" % filename, os.O_RDWR)
            read = os.read(file,1024)
            print(read,'\n')
            os.close(file)
            inputcode()
        elif inp == 6:
            path1 = input('Enter path of file you wish to move:')
            path2 = input('Enter the path of the directory you wish to copy this file into:')
            os.rename(path1,path2)
            print('File now moved to: %s' % path2)
        elif inp == 7:
            os._exit(0)
        else:
            print('Please enter a valid option')


if __name__ == "__main__":
    inputcode()