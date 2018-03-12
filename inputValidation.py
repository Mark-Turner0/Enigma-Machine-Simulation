def validGearSelection(selected):
	if int(selected) > 0 and int(selected) < 6:
		return True
	else: return False

def validOrientationInput(selected):
	if int(selected) > 0 and int(selected) < 27:
		return True
	else: return False

def plugboardnumberValidation(selected):
	if int(selected) > -1 and int(selected) < 14:
		return True
	else: return False

def plugboardValidation(settings, selected):
	if selected in settings:
		return False
	else: return True 
