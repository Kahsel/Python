class students:
    
    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        
    def fullName(self):
        return f'\nFirstName: {self.firstName}\nSecondName: {self.lastName}\nAge: {self.age}\nRank: {self.rank}'
    
class teachers(students):
    pass
    def __init__(self, firstName, lastName, age,rank):
        super().__init__(firstName, lastName, age)
        self.rank = rank
        
tchr1 = teachers('Collins', 'Dalung', 36, 12)
tchr2 = teachers('Sekyen', 'Leshak', 40, 9)

print(teachers.fullName(tchr1),'\n', teachers.fullName(tchr2))