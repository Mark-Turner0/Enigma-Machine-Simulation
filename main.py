import wx
import inputValidation as iv 
import enigma as en
import mainPyGame as mpg 
mode = 1
plugSets = []

class questions(wx.Frame):    
    def __init__(self, *args, **kwargs):
        super(questions, self).__init__(*args, **kwargs) 
            
        self.drawWindow()
        self.initUI()
        
    def drawWindow(self):
        self.window = wx.Frame(None) 
        self.panel= wx.Panel(self)

    def initUI(self):
        self.SetTitle("Enigma Setup")
        self.SetSize((370,150))
        self.Show(True)
        questionLabel = "Please select the first gear you would like to use (1-5):"
        self.question = wx.StaticText(self.panel, label=questionLabel,pos=(0,0))
        self.answerBox = wx.TextCtrl(self.panel, size=(340,22.5), pos=(15,50))
        self.submitButton = wx.Button(self.panel, -1, "Submit", pos=(40,100))
        self.Bind(wx.EVT_BUTTON, self.onSubmit, id=self.submitButton.GetId())
        self.quitButton = wx.Button(self.panel, -1, "Quit", pos=(240,100))
        self.Bind(wx.EVT_BUTTON, self.onQuit, id=self.quitButton.GetId())

    def onSubmit(self, e):
        global mode
        global plugSets
        global i
        global numOfSets
        global gear1or
        global gear2or
        global gear3or
        selected = self.answerBox.GetValue()

        if mode < 4:
            if iv.validGearSelection(selected) != True:
                self.answerBox.SetValue("")
                self.question.SetLabel("Please enter a valid input (1-5)")

                mode -= 1

        if mode == 1:
            self.answerBox.SetValue("")
            en.gearselection1(selected)
            self.question.SetLabel("Please select the second gear you would like to use (1-5):")

        if mode == 2:
            self.answerBox.SetValue("")
            en.gearselection2(selected)
            self.question.SetLabel("Please select the third gear you would like to use (1-5):")

        if mode == 3:
            self.answerBox.SetValue("")
            en.gearselection3(selected)
            self.question.SetLabel("How would you like the first gear to be orientated (1-26)?")

        if mode > 3 and mode < 7:
            if iv.validOrientationInput(selected) != True:
                self.answerBox.SetValue("")
                self.question.SetLabel("Please enter a valid input (1-26):")
                mode -= 1

        if mode == 4:
            self.answerBox.SetValue("")
            gear1or = int(selected) - 1
            self.question.SetLabel("How would you like the second gear to be orientated (1-26)?")

        if mode == 5:
            self.answerBox.SetValue("")
            gear2or = int(selected) - 1
            self.question.SetLabel("How would you like the third gear to be orientated (1-26)?")

        if mode == 6:
            self.answerBox.SetValue("")
            gear3or = int(selected) - 1
            global plugSets
            plugSets = []
            self.question.SetLabel("How many plugboard settings wouild you like to set (0-13)?")

        if mode == 7:
            if iv.plugboardnumberValidation(selected) != True:
                self.answerBox.SetValue("")
                self.question.SetLabel("Please enter a valid input (0-13):")
                mode -= 1

        if mode == 7 and int(selected) > 0:
            numOfSets = int(selected)*2
            self.answerBox.SetValue("")
            self.question.SetLabel("What letter of the alphabet would you like to swap?")

        if mode == 7 and int(selected) == 0:
            mode = 33

        if mode > 7 and mode < 33:
            selected = selected[:1].upper()
            if iv.plugboardValidation(plugSets, selected) != True:
                self.answerBox.SetValue("")
                self.question.SetLabel("This letter is invalid or has already been used.")
                mode -= 1
            else: 
                plugSets.append(selected)

                print(len(plugSets))
                if len(plugSets) > numOfSets-1:
                    mode = 33
            
            if mode > 7 and mode < 33:
                if mode % 2 == 0:
                    self.answerBox.SetValue("")
                    self.question.SetLabel("What letter of the alphabet would you like to swap it with?")
                else:
                    self.answerBox.SetValue("") 
                    self.question.SetLabel("What character would you like to swap?")

        if mode == 33:
            self.Close()
            mpg.main(gear1or, gear2or, gear3or, plugSets)

        mode += 1

    def onQuit(self, e):
        import sys
        self.Close()
        sys.exit(1)

def main():
    app = wx.App()
    questions(None)
    app.MainLoop()   

if __name__ == '__main__':
    main()
