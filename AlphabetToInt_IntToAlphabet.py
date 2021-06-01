import os
from platform import system

if system() == "Windows": # Checks if the system is Windows or not
    Windows = True
else:
    Windows = False

def clear(): # Clears the terminal
    if Windows:
        os.system("cls")
    else:
        os.system("clear")

clear()
Origin = input("\n Code to \"encrypt\": ")
Encrypted = Origin
Test = "a1 b2 c3 4d 5e 6f g7 h8 i9 j10 k11 l12 m13 n14 o15 p16 q17 r18 s19 t20 u21 v22 w23 x24 y25 z26" # Input for testing
InvertedTest = "1a 2b 3c 4d 5e 6f g7 8h 9i 10j 11k 12l 13m 14n 15o 16p 17q 18r 19s 20t 21u 22v 23w 24x 25y 26z" # Expected output from testing

TestCheck = Origin.replace(" ","") # Origin, but replace all spaces

if TestCheck == "":
    Origin = Test
    Encrypted = Test

"""
#------------------------------------------------#
# Replaces the letters with their corresponding  #
#     number in the alphabet and vice versa      #
                                                 #
Encrypted = Encrypted.replace("a","^") # a = 1   #
Encrypted = Encrypted.replace("1","a")           #
Encrypted = Encrypted.replace("^","1")           #
                                                 #
Encrypted = Encrypted.replace("b","^") # b = 2   #
Encrypted = Encrypted.replace("2","b")           #
Encrypted = Encrypted.replace("^","2")           #
                                                 #
Encrypted = Encrypted.replace("c","^") # c = 3   #
Encrypted = Encrypted.replace("3","c")           #
Encrypted = Encrypted.replace("^","3")           #
                                                 #
Encrypted = Encrypted.replace("d","^") # d = 4   #
Encrypted = Encrypted.replace("4","d")           #
Encrypted = Encrypted.replace("^","4")           #
                                                 #
Encrypted = Encrypted.replace("e","^") # e = 5   #
Encrypted = Encrypted.replace("5","e")           #
Encrypted = Encrypted.replace("^","5")           #
                                                 #
Encrypted = Encrypted.replace("f","^") # f = 6   #
Encrypted = Encrypted.replace("6","f")           #
Encrypted = Encrypted.replace("^","6")           #
                                                 #
Encrypted = Encrypted.replace("g","^") # g = 7   #
Encrypted = Encrypted.replace("7","g")           #
Encrypted = Encrypted.replace("^","7")           #
                                                 #
Encrypted = Encrypted.replace("h","^") # h = 8   #
Encrypted = Encrypted.replace("8","h")           #
Encrypted = Encrypted.replace("^","8")           #
                                                 #
Encrypted = Encrypted.replace("i","^") # i = 9   #
Encrypted = Encrypted.replace("9","i")           #
Encrypted = Encrypted.replace("^","9")           #
                                                 #
Encrypted = Encrypted.replace("j","^") # j = 10  #
Encrypted = Encrypted.replace("10","j")          #
Encrypted = Encrypted.replace("^","10")          #
                                                 #
Encrypted = Encrypted.replace("k","^") # k = 11  #
Encrypted = Encrypted.replace("11","k")          #
Encrypted = Encrypted.replace("^","11")          #
                                                 #
Encrypted = Encrypted.replace("l","^") # l = 12  #
Encrypted = Encrypted.replace("12","l")          #
Encrypted = Encrypted.replace("^","12")          #
                                                 #
Encrypted = Encrypted.replace("m","^") # m = 13  #
Encrypted = Encrypted.replace("13","m")          #
Encrypted = Encrypted.replace("^","13")          #
                                                 #
Encrypted = Encrypted.replace("n","^") # n = 14  #
Encrypted = Encrypted.replace("14","n")          #
Encrypted = Encrypted.replace("^","14")          #
                                                 #
Encrypted = Encrypted.replace("o","^") # o = 15  #
Encrypted = Encrypted.replace("15","o")          #
Encrypted = Encrypted.replace("^","15")          #
                                                 #
Encrypted = Encrypted.replace("p","^") # p = 16  #
Encrypted = Encrypted.replace("16","p")          #
Encrypted = Encrypted.replace("^","16")          #
                                                 #
Encrypted = Encrypted.replace("q","^") # q = 17  #
Encrypted = Encrypted.replace("17","q")          #
Encrypted = Encrypted.replace("^","17")          #
                                                 #
Encrypted = Encrypted.replace("r","^") # r = 18  #
Encrypted = Encrypted.replace("18","r")          #
Encrypted = Encrypted.replace("^","18")          #
                                                 #
Encrypted = Encrypted.replace("s","^") # s = 19  #
Encrypted = Encrypted.replace("19","s")          #
Encrypted = Encrypted.replace("^","19")          #
                                                 #
Encrypted = Encrypted.replace("t","^") # t = 20  #
Encrypted = Encrypted.replace("20","t")          #
Encrypted = Encrypted.replace("^","20")          #
                                                 #
Encrypted = Encrypted.replace("u","^") # u = 21  #
Encrypted = Encrypted.replace("21","u")          #
Encrypted = Encrypted.replace("^","21")          #
                                                 #
Encrypted = Encrypted.replace("v","^") # v = 22  #
Encrypted = Encrypted.replace("22","v")          #
Encrypted = Encrypted.replace("^","22")          #
                                                 #
Encrypted = Encrypted.replace("w","^") # w = 23  #
Encrypted = Encrypted.replace("23","w")          #
Encrypted = Encrypted.replace("^","23")          #
                                                 #
Encrypted = Encrypted.replace("x","^") # x = 24  #
Encrypted = Encrypted.replace("24","x")          #
Encrypted = Encrypted.replace("^","24")          #
                                                 #
Encrypted = Encrypted.replace("y","^") # y = 25  #
Encrypted = Encrypted.replace("25","y")          #
Encrypted = Encrypted.replace("^","25")          #
                                                 #
Encrypted = Encrypted.replace("z","^") # z = 26  #
Encrypted = Encrypted.replace("26","z")          #
Encrypted = Encrypted.replace("^","26")          #
                                                 #
#------------------------------------------------#
"""

#------------------- Inverted -------------------#
# Replaces the letters with their corresponding  #
#     number in the alphabet and vice versa      #
                                                 #
Encrypted = Encrypted.replace("z","^") # z = 26  #
Encrypted = Encrypted.replace("26","z")          #
Encrypted = Encrypted.replace("^","26")          #
                                                 #
Encrypted = Encrypted.replace("y","^") # y = 25  #
Encrypted = Encrypted.replace("25","y")          #
Encrypted = Encrypted.replace("^","25")          #
                                                 #
Encrypted = Encrypted.replace("x","^") # x = 24  #
Encrypted = Encrypted.replace("24","x")          #
Encrypted = Encrypted.replace("^","24")          #
                                                 #
Encrypted = Encrypted.replace("w","^") # w = 23  #
Encrypted = Encrypted.replace("23","w")          #
Encrypted = Encrypted.replace("^","23")          #
                                                 #
Encrypted = Encrypted.replace("v","^") # v = 22  #
Encrypted = Encrypted.replace("22","v")          #
Encrypted = Encrypted.replace("^","22")          #
                                                 #
Encrypted = Encrypted.replace("u","^") # u = 21  #
Encrypted = Encrypted.replace("21","u")          #
Encrypted = Encrypted.replace("^","21")          #
                                                 #
Encrypted = Encrypted.replace("t","^") # t = 20  #
Encrypted = Encrypted.replace("20","t")          #
Encrypted = Encrypted.replace("^","20")          #
                                                 #
Encrypted = Encrypted.replace("s","^") # s = 19  #
Encrypted = Encrypted.replace("19","s")          #
Encrypted = Encrypted.replace("^","19")          #
                                                 #
Encrypted = Encrypted.replace("r","^") # r = 18  #
Encrypted = Encrypted.replace("18","r")          #
Encrypted = Encrypted.replace("^","18")          #
                                                 #
Encrypted = Encrypted.replace("q","^") # q = 17  #
Encrypted = Encrypted.replace("17","q")          #
Encrypted = Encrypted.replace("^","17")          #
                                                 #
Encrypted = Encrypted.replace("p","^") # p = 16  #
Encrypted = Encrypted.replace("16","p")          #
Encrypted = Encrypted.replace("^","16")          #
                                                 #
Encrypted = Encrypted.replace("o","^") # o = 15  #
Encrypted = Encrypted.replace("15","o")          #
Encrypted = Encrypted.replace("^","15")          #
                                                 #
Encrypted = Encrypted.replace("n","^") # n = 14  #
Encrypted = Encrypted.replace("14","n")          #
Encrypted = Encrypted.replace("^","14")          #
                                                 #
Encrypted = Encrypted.replace("m","^") # m = 13  #
Encrypted = Encrypted.replace("13","m")          #
Encrypted = Encrypted.replace("^","13")          #
                                                 #
Encrypted = Encrypted.replace("l","^") # l = 12  #
Encrypted = Encrypted.replace("12","l")          #
Encrypted = Encrypted.replace("^","12")          #
                                                 #
Encrypted = Encrypted.replace("k","^") # k = 11  #
Encrypted = Encrypted.replace("11","k")          #
Encrypted = Encrypted.replace("^","11")          #
                                                 #
Encrypted = Encrypted.replace("j","^") # j = 10  #
Encrypted = Encrypted.replace("10","j")          #
Encrypted = Encrypted.replace("^","10")          #
                                                 #
Encrypted = Encrypted.replace("i","^") # i = 9   #
Encrypted = Encrypted.replace("9","i")           #
Encrypted = Encrypted.replace("^","9")           #
                                                 #
Encrypted = Encrypted.replace("h","^") # h = 8   #
Encrypted = Encrypted.replace("8","h")           #
Encrypted = Encrypted.replace("^","8")           #
                                                 #
Encrypted = Encrypted.replace("g","^") # g = 7   #
Encrypted = Encrypted.replace("7","g")           #
Encrypted = Encrypted.replace("^","7")           #
                                                 #
Encrypted = Encrypted.replace("f","^") # f = 6   #
Encrypted = Encrypted.replace("6","f")           #
Encrypted = Encrypted.replace("^","6")           #
                                                 #
Encrypted = Encrypted.replace("e","^") # e = 5   #
Encrypted = Encrypted.replace("5","e")           #
Encrypted = Encrypted.replace("^","5")           #
                                                 #
Encrypted = Encrypted.replace("d","^") # d = 4   #
Encrypted = Encrypted.replace("4","d")           #
Encrypted = Encrypted.replace("^","4")           #
                                                 #
Encrypted = Encrypted.replace("c","^") # c = 3   #
Encrypted = Encrypted.replace("3","c")           #
Encrypted = Encrypted.replace("^","3")           #
                                                 #
Encrypted = Encrypted.replace("b","^") # b = 2   #
Encrypted = Encrypted.replace("2","b")           #
Encrypted = Encrypted.replace("^","2")           #
                                                 #
Encrypted = Encrypted.replace("a","^") # a = 1   #
Encrypted = Encrypted.replace("1","a")           #
Encrypted = Encrypted.replace("^","1")           #
                                                 #
#------------------------------------------------#


print(f"\n Given Code: {Origin}\n\n Encrypted Code: {Encrypted}\n")
if Origin == Test:
    if Encrypted == InvertedTest:
        print("Success")
    else:
        print("\n Something went wrong\n")