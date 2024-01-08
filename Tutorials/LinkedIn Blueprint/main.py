# "Blueprint" => a model that is replicated for each users (e.g. Name, mail or password...)
# A blueprint respond to two questions :
# - What information the user has ?
# - What action the user can perform with these informations ?
# The user's data associed to the attributes of the blueprint are called an "object" 

from user import User
from post import Post

app_user_one = User("Julien", "He", "21", "France", "js@gmail.com", "jsm", "+33 0715362495", "Student" )
app_user_one.get_user_info()

app_user_two = User("Leti", "She", "21", "Spain", "lm@gmail.com", "lme", "+34 445215370", "Student" )
app_user_two.get_user_info()

new_post = Post(app_user_one.name, "Just started my internship !")
new_post.get_post_info()