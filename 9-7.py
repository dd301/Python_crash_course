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
    
class Admin(User):
    def __init__(self, first_name, last_name, age, 
            sex):
        super().__init__(first_name, last_name, age,
                        sex)
        self.privileges = ['can add post', 
                        'can delete post',
                        'can ban user']
    
    def show_privileges(self):
        print("An admins privileges are:")
        for privilege in self.privileges:
            print(privilege)

admin = Admin('Donato', 'Doley', '20', 'Male')
admin.show_privileges()