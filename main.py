#coding: utf-8
import enigma as en
import wx
import inputValidation as iv 

selected = 99
while iv.validGearSelection(selected) != True:
	print("Please select the first gear you would like to use (1-5):")
	selected = input()
	en.gearselection1(selected)
selected = 99
while iv.validGearSelection(selected) != True:
	print("Please select the second gear you would like to use (1-5):")
	selected = input()
	en.gearselection2(selected)

selected = 99
while iv.validGearSelection(selected) != True:
	print("Please select the third gear you would like to use (1-5):")
	selected = input()
	en.gearselection3(selected)

print("How would you like the first gear to be orientated (1-26)?")
gear1or = int(input()) - 1
print(gear1or)
print("How would you like the second gear to be orientated (1-26)?")
gear2or = int(input()) - 1
print("How would you like the third gear to be orientated (1-26)?")
gear3or = int(input()) - 1
print("How many plugboard settings would you like to set (maximum 13)")
numOfSets = int(input())
plugSets = []
#for i in range(0,numOfSets-1):
	#valid = False
	#while valid != True:
		#print("What character would you like to swap?")
		#swap1 = input()
		#if iv.plugboardValidation(plugSets, swap1) == True:
			#plugSets.append(swap1)
			#print("What character would you like to swap it with?")
			#swap2 = input()
			#valid = True
			#if iv.plugboardValidation(plugSets, swap2) == False: 
				#plugSets.append(swap2)
				#valid = True

while 1:
	print("Please enter the character which you wish to be encyphered.")
	plaintext = input().upper()
	if plaintext == "QUIT": quit()
	cipher = en.encrypt(plaintext, gear1or,gear2or,gear3or)
	gear1or += 1
	if gear1or > 25:
		gear1or -= 26
		gear2or += 1
		if gear2or > 25:
			gear2or -= 26
			gear3or += 1
			if gear3or > 25:
				gear3or -= 26
	print(cipher)
