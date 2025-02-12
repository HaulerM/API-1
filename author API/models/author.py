

class Author:
    def __init__(self,name,age,location,contact,email):
        self.name= name
        self.age= age
        self.location=location
        self.email= email
        self.contact= contact

    def fetch_author(self):
        print(f"Author {self.name}. Published her first book at the age of {self.age},located at  {self.location}, {self.email}, {self.contact}")

author_one= Author("Haulah Musa",25,"London","haulermusa15@gmail.com",145678790)
author_one.fetch_author()