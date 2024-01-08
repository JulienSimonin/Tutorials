class Post :
    def __init__(self, author, message):
        self.author = author
        self.message = message
        
    def get_post_info(self):
        print(f"Post :\n"
              f"    {self.message} \n"
              f"  Written by {self.author}. \n")
