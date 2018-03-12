# -*- coding: utf-8 -*-
gear11 = ['Z', 'Y', 'S', 'M', 'J', 'U', 'V', 'E', 'L', 'A', 'G', 'Q', 'K', 'X', 'H', 'F', 'D', 'T', 'I', 'C', 'N', 'B', 'W', 'R', 'O', 'P']
gear12 = ['D', 'R', 'H', 'F', 'U', 'W', 'O', 'E', 'S', 'T', 'X', 'L', 'K', 'G', 'J', 'B', 'C', 'V', 'I', 'Z', 'Y', 'N', 'A', 'P', 'M', 'Q']
gear13 = ['Z', 'U', 'R', 'G', 'M', 'Y', 'B', 'F', 'N', 'A', 'P', 'T', 'D', 'S', 'J', 'L', 'H', 'X', 'V', 'C', 'I', 'W', 'O', 'E', 'Q', 'K']
gear14 = ['T', 'R', 'C', 'S', 'U', 'X', 'Z', 'W', 'V', 'F', 'H', 'J', 'N', 'Y', 'L', 'B', 'P', 'O', 'D', 'K', 'A', 'G', 'E', 'I', 'Q', 'M']
gear15 = ['E', 'H', 'T', 'G', 'S', 'A', 'Q', 'U', 'F', 'D', 'K', 'Y', 'L', 'X', 'P', 'M', 'V', 'I', 'O', 'J', 'C', 'B', 'N', 'W', 'R', 'Z']
gear21 = ['U', 'S', 'Q', 'W', 'D', 'O', 'Z', 'N', 'K', 'H', 'R', 'V', 'P', 'J', 'E', 'L', 'X', 'T', 'I', 'A', 'F', 'Y', 'B', 'C', 'M', 'G']
gear22 = ['U', 'V', 'Y', 'F', 'H', 'Q', 'R', 'G', 'O', 'S', 'A', 'K', 'N', 'P', 'J', 'E', 'L', 'X', 'Z', 'B', 'C', 'W', 'T', 'M', 'I', 'D']
gear23 = ['I', 'S', 'Q', 'K', 'M', 'U', 'F', 'O', 'X', 'Y', 'L', 'H', 'J', 'B', 'A', 'C', 'D', 'G', 'T', 'N', 'V', 'P', 'Z', 'W', 'R', 'E']
gear24 = ['E', 'S', 'V', 'Y', 'A', 'J', 'L', 'X', 'R', 'K', 'T', 'I', 'W', 'D', 'U', 'G', 'C', 'B', 'N', 'O', 'F', 'Q', 'H', 'M', 'Z', 'P']
gear25 = ['S', 'O', 'T', 'E', 'R', 'D', 'V', 'J', 'W', 'K', 'G', 'Z', 'U', 'I', 'Q', 'A', 'C', 'P', 'L', 'N', 'F', 'H', 'M', 'B', 'X', 'Y']
gear31 = ['Z', 'C', 'T', 'Q', 'R', 'E', 'H', 'O', 'J', 'W', 'N', 'K', 'V', 'U', 'M', 'P', 'D', 'F', 'G', 'B', 'X', 'L', 'S', 'A', 'Y', 'I']
gear32 = ['Y', 'M', 'C', 'E', 'G', 'L', 'Z', 'S', 'N', 'D', 'B', 'K', 'A', 'T', 'R', 'O', 'H', 'V', 'W', 'I', 'P', 'X', 'Q', 'J', 'F', 'U']
gear33 = ['L', 'D', 'Q', 'R', 'M', 'E', 'X', 'J', 'T', 'C', 'F', 'W', 'H', 'N', 'U', 'S', 'A', 'O', 'G', 'Y', 'I', 'P', 'B', 'K', 'V', 'Z']
gear34 = ['T', 'K', 'C', 'N', 'F', 'Z', 'W', 'X', 'I', 'Q', 'P', 'L', 'S', 'J', 'O', 'R', 'A', 'H', 'G', 'V', 'E', 'U', 'D', 'B', 'Y', 'M']
gear35 = ['S', 'D', 'O', 'U', 'F', 'Q', 'L', 'R', 'Y', 'N', 'J', 'H', 'X', 'Z', 'K', 'C', 'T', 'M', 'G', 'B', 'I', 'P', 'A', 'W', 'V', 'E']

def gearselection1(selected):
	global valid
	global gear1
	if int(selected) == 1:
		gear1 = gear11
		valid = True
	elif int(selected) == 2:
		gear1 = gear12
		valid = True
	elif int(selected) == 3:
		gear1 = gear13
		valid = True
	elif int(selected) == 4:
		gear1 = gear14
		valid = True
	elif int(selected) == 5:
		gear1 = gear15
		valid = True
	else: print("Invalid input.")

def gearselection2(selected):
	global valid
	global gear2
	if int(selected) == 1:
		gear2 = gear21
		valid = True
	elif int(selected) == 2:
		gear2 = gear22
		valid = True
	elif int(selected) == 3:
		gear2 = gear23
		valid = True
	elif int(selected) == 4:
		gear2 = gear24
		valid = True
	elif int(selected) == 5:
		gear2 = gear25
		valid = True
	else: print("Invalid input.")

def gearselection3(selected):
	global valid 
	global gear3
	if int(selected) == 1:
		gear3 = gear31
		valid = True
	elif int(selected) == 2:
		gear3 = gear32
		valid = True
	elif int(selected) == 3:
		gear3 = gear33
		valid = True
	elif int(selected) == 4:
		gear3 = gear34
		valid = True
	elif int(selected) == 5:
		gear3 = gear35
		valid = True
	else: print("Invalid input.")

def incrementGear1(gear1or):
	gear1or += 1
	if gear1or > 24:
		gear1or -= 25
	return gear1or

def incrementGear2(gear1or, gear2or):
	if gear1or == 0:
		gear2or += 1
		if gear2or > 24:
			gear2or -= 25
	return gear2or

def incrementGear3(gear1or, gear2or, gear3or):
	if gear2or == 0 and gear1or == 0:
		gear3or += 1
		if gear3or > 24:
			gear3or -= 25
	return gear3or

def encrypt(plaintext, gear1or, gear2or, gear3or):
	print("Input: "+plaintext)
	print("gear1or: "+str(gear1or))
	print("gear2or: "+str(gear2or))
	print("gear3or: "+str(gear3or))
	cipher1 = gear1or + ord(plaintext) - 65
	if cipher1 > 25:
		cipher1 -= 26
	cipher1 = gear1[cipher1]
	print("After Gear 1: "+cipher1)

	cipher2 = gear2or + ord(cipher1) - 65
	if cipher2 > 25:
		cipher2 -= 26
	cipher2 = gear2[cipher2]
	print("After Gear 2: "+cipher2)

	cipher3 = gear3or + ord(cipher2) - 65
	if cipher3 > 25:
		cipher3 -= 26
	cipher3 = gear3[cipher3]
	print("After Gear 3: "+cipher3)

	cipher3 = chr(90 - ord(cipher3) + 65)
	print("After the reflector: "+cipher3)

	cipher3 = chr(gear3.index(cipher3) + 65 - gear3or)
	if ord(cipher3) < 65:
		cipher3 = chr(ord(cipher3) + 26)
	print("After Gear 3 again: "+cipher3)

	cipher2 = chr(gear2.index(cipher3) + 65 - gear2or)
	if ord(cipher2) < 65:
		cipher2 = chr(ord(cipher2) + 26)
	print("After Gear 2 again: "+cipher2)

	cipher1 = chr(gear1.index(cipher2) + 65 - gear1or)
	if ord(cipher1) < 65:
		cipher1 = chr(ord(cipher1) + 26)
	print("After Gear 1 again: "+cipher1)
	return cipher1
