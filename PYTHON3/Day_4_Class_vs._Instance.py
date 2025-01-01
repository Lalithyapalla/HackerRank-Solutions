class Person:
    def __init__(self,initialAge):
        self.initialAge=initialAge
        if self.initialAge<0:
            self.initialAge=0
            print(f'Age is not valid, setting age to {0}.')
        else:
            self.initialAge=initialAge
    def amIOld(self):
        if self.initialAge<13:
            print('You are young.')
        elif 13<=self.initialAge<18:
            print('You are a teenager.')
        else:
            print('You are old.')
    def yearPasses(self):
        self.initialAge+=1
