class stringUpper:
    def get(self):
        self.str1 = ''
        self.str1 = str(input('Enter String: '))
        
    def push(self):
        print(self.str1.upper())
    
str1 = stringUpper() 
str1.get()
str1.push()
