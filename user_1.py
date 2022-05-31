import user as u

class Admin(u.User):
    def __init__(self, first_name, last_name, age, 
            sex):
        super().__init__(first_name, last_name, age,
                        sex)

        self.admin_privileges = Privileges()


class Privileges():
    def __init__(self):
         self.privileges = ['can add post', 
                        'can delete post',
                        'can ban user']
    
    def show_privileges(self):
        print("An admins privileges are:")
        for privilege in self.privileges:
            print(privilege)