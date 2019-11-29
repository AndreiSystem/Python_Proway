class Person:
    def setPersonAddress(self, personAddress):
        self.personAddress = personAddress
    
    def getPersonAddress(self):
        return self.personAddress    

    def setNome(self, nome):
        self.nome = nome
    
    def getNome(self):
        return self.nome
    
    def setTelefone(self, telefone):
        self.telefone = telefone
    
    def getTelefone(self):
        return self.telefone
    
    def setEmail(self, email):
        self.email = email
    
    def getEmail(self):
        return self.email
    
    def purchaseParkingPass(self):
        pass

class Student(Person):
    def setStudentNumber(self, studentNumber):
        self.studentNumber = studentNumber
    
    def getStudentNumber(self):
        return self.studentNumber

    
    def setAverageMark(self, averageMark):
        self.averageMark = averageMark
    
    def getAverageMark(self):
        return self.averageMark
    
    def ValidateAverage(self):
        if self.getAverageMark() < 70:
            return 'REPROVADO'
        else:
            return 'APROVADO'

class Professor(Person):
    def setSalary(self, salary):
        self.salary = salary
    
    def getSalary(self):
        return self.salary

    
class Address():
    def __str__(self):
        return self.street + "\n" + self.city + "\n" + self.state + "\n" + self.postalCode + "\n" + self.country + "\n"
    
    def setStreet(self, street):
        self.street = street
    
    def getStreet(self):
        return self.street
    
    def setCity(self, city):
        self.city = city
    
    def getCity(self):
        return self.city
    
    def setState(self, state):
        self.state = state
    
    def getState(self):
        return self.state
    
    def setPostalCode(self, postalCode):
        self.postalCode = postalCode
    
    def getPostalCode(self):
        return self.postalCode
    

    def setCountry(self, country):
        self.country = country
    
    def getCountry(self):
        return self.country
    
    def validate(self):
        pass

    def OutputAsLabel(self):
        pass



professor = Professor()

professor.setNome('José')
professor.setSalary(324234)
print(professor.getNome())
print(professor.getSalary())
"""
#Instanciando
pessoa = Student()
address = Address()

#Setando Parametros SUDENT
pessoa.setNome('Juka')
pessoa.setEmail('Juka@hotmail.com')
pessoa.setTelefone('(47) 991-81')
pessoa.setStudentNumber(1254)
pessoa.setAverageMark(60)

#Setando parametros ADDRESS
address.setStreet('Rua 7 de Setembro')
address.setCity('Blumenau')
address.setState('SC')
address.setPostalCode('89070-258')
address.setCountry('Brazil')

#Setando um ADDRESS para um STUDENT
pessoa.setPersonAddress(address)

print(pessoa.getNome())
print(pessoa.getEmail())
print(pessoa.getTelefone())
print(pessoa.getStudentNumber())
print(pessoa.getAverageMark())
print(pessoa.getPersonAddress())
print(pessoa.ValidateAverage())



"""