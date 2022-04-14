class Toggleable():
    def __init__(self, value=False):
        if(type(value) == bool):
            self.value = value
        else:
            self.value = False
    def t(self):
        if(self.value == True):
            self.value = False
        elif(self.value == False):
            self.value = True
        else:
            self.value = False
    def toggle(self):
        if(self.value == True):
            self.value = False
        elif(self.value == False):
            self.value = True
        else:
            self.value = False
    def setVal(self, nv):
        if(type(nv) == bool):
            self.value = nv
        elif(type(self.value) != bool):
            self.value = False