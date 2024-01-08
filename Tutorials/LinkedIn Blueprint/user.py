# Create a class to put all the "user atributes" and "user behavior"
# User attributes => data and user informations
# User behavior => what the user can do in the application with his data/informations

#Create a class
class User :
    # Define the blueprint atributes
    def __init__(self, name, gender, age, nationality, email, password, phone_number, job):
        self.name = name
        self.gender = gender
        self.age = age
        self.nationality = nationality
        self.email = email
        self.password = password
        self.phone_number = phone_number
        self.job = job
        
    # Define the blueprint behaviors or the methods
    def change_email(self, new_email):
        self.email = new_email
    
    def change_password(self, new_password):
        self.password = new_password
    
    def change_phone_number(self, new_phone_number):
        self.phone_number = new_phone_number
    
    def change_job(self, new_job):
        self.job = new_job

    def get_user_info(self):
        print(f"\n{self.name} is {self.age} years old and comes from {self.nationality}.\n" 
              f"{self.gender} is currently working as a {self.job}.\n"
              f"You can contact {self.name} by mail at {self.email} or by phone at {self.phone_number}.\n")
        
app_user_one = User("Julien", "He", "21", "France", "js@gmail.com", "jsm", "+33 0715362495", "Student" )
app_user_one.get_user_info()

app_user_two = User("Leti", "She", "21", "Spain", "lm@gmail.com", "lme", "+34 445215370", "Student" )
app_user_two.get_user_info()