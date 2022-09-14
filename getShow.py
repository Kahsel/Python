class stringUpper:
    def set(self):
        self.str1 = ''
        self.str1 = str(input('Enter String: '))
        
    def get(self):
        print(self.str1.upper())
    
str1 = stringUpper() 
str1.set()
str1.get()
