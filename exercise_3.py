import datetime

class Contact:
    def __init__(self,name, phone) -> None:
        self.name = name
        self.phone = phone


class MailSender:
    def send_mail(self,email):
        return f'Your email sent to the direction {email}'


class Friend(Contact, MailSender):
    def __init__(self, name, phone, email) -> None:
        super().__init__(name, phone)
        self.email = email
    
    def __str__(self) -> str:
        return super().send_mail(self.email)
    

class Family(Contact,MailSender):
    def __init__(self, name, phone,email) -> None:
        super().__init__(name, phone)
        self.email = email
        self.birthdate = datetime.datetime.now()

    def __str__(self) -> str:
        return super().send_mail(self.email)


    
