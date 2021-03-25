class LibraryItem:
    def __init__(self, title, subject, status) -> None:
        self.title = title
        self.subject = subject
        self.status = status
        
    def booking(self,first_arg):
        if self.status == True:
            return f'You have booked {first_arg} '
        elif self.status ==False: 
            return f'Your order about {first_arg} is occupied'
        

class Book(LibraryItem):
    def __init__(self, title, subject, status,ISBN,author) -> None:
        super().__init__(title, subject, status)
        self.ISBN = ISBN
        self.author = author
    
    def __str__(self) -> str:
        return super().booking(self.title)


class Magazine(LibraryItem):
    def __init__(self, title, subject, status,volume) -> None:
        super().__init__(title, subject, status)
        self.journalName = title
        self.volume = volume

    def __str__(self) -> str:
        return super().booking(self.journalName)


class CD(LibraryItem):
    def __init__(self, title) -> None:
        super().__init__(title, subject='',status = False,)
    def __str__(self) -> str:
        return super().booking(self.title)



