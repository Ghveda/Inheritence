class People:
    def __init__(self,firstname,lastname) -> None:
        self.firstname = firstname
        self.lastname = lastname

    def get_email(self):
        return f'{self.firstname}'+f'.{self.lastname}'
    

class Lecturer(People):
    def __init__(self, salary,firstname, lastname) -> None:
        super().__init__(firstname,lastname)
        self.salary = salary

    def __str__(self) -> str:
        return 'Your Email is: '+  super().get_email()+'@btu.edu.ge'


class Students(People):
    def __init__(self, courses,firstname, lastname) -> None:
        super().__init__(firstname,lastname)
        self.courses = courses

    def __str__(self) -> str:
        return 'Your Email is: '+  super().get_email()+'.1@btu.edu.ge'

