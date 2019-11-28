class Address:
    def __init__(self, street, city, state, code, country):
        self.street = street
        self.city = city
        self.state = state
        self.code = code
        self.country = country

class Person(Address):
    def __init__(self, name, phone, email):
        self.name = name.title().strip()
        self.phone = phone
        self.email = email
        
    
    def say_registers (self):
        print(f'Nome: {self.name}, telefone: {self.phone}, email: {self.email}')
        
    
class Student(Person):
    def __init__(self, number, media):
        self.number = number
        self.media = media

        if self.media > 7:
            print('\033[32mStudent is alleged!\033[0;0m')
        else:
            print('\033[31mStudent not is alleged!\033[0;0m')

    def registers_student(self):
        print(f'Average Mark: \033[32m{self.number}\033[0;0m')
        print(f'Student average: \033[32m{self.media:.2f}\033[0;0m')
    

class Professor(Person):
    def __init__ (self, salary):
        self.salary = salary
    
    def say_salary(self):
        print(f'Salary: R${self.salary:.2f}')



def calcula_media(message = 'How many notes do you want to register? '):
    n_notas = int(input(message))
    notas = []
    for i in range(1,n_notas+1):
        n = float(input(f'{i}º grade: '))
        notas.append(n)
    media_aluno = sum(notas) / len(notas)
    return media_aluno



name = input('Register your name: ')
phone = int(input('Register your phone: '))
email = input('Digite um email: ')


#pessoa1 = Person(name, phone, email)
#pessoa1.say_registers()

#media_final = calcula_media()
#aluno = Student(888, media_final)
#aluno.registers_student()

professor = Professor(1234)
professor.say_salary()





