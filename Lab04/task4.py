import platform #import the platform module
import os #import the operating system module


x = platform.system() #get the platform - linux or windows
print('The operating system is:',x) #print the platform

if x == 'Darwin': #if the operating system is Darwin
    print(os.fork()) #fork
elif x == 'Linux': #if the operating system is Linux
    print(os.fork())
elif x == 'Windows': #if the operating system is Windows
    print(os._spawn())

