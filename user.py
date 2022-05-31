class User():
    def __init__(self, first_name, last_name, age, 
            sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
    
    def describe_user(self):
        print("The users name is " + self.first_name 
        + " " + self.last_name + ". Their age is " + self.age +
        " and their sex is " + self.sex + ".")
    
    def greet_user(self):
        print("Hello, " + self.first_name + " " +
        self.last_name + "!")