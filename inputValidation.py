def validGearSelection(selected):
	if int(selected) > 0 and int(selected) < 6:
		return True
		selected = 99
	else:
		return False

def plugboardValidation(settings, selected):
	if selected in settings:
		return False
		print("You have already used this character.")
	else:
		return True 

