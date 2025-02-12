class Company:
    def __init__(self, name,email,location):
        self.name= name
        self.email = email
        self.location =location
        
    #new instance
company_one = Company("Musa","haulermusa18@gmail.com","Wakiso")
print(company_one.name,company_one.email,company_one.location)