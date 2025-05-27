# Imagine you're building a prototype of a social media app called InstaClone. Users can create profiles, upload profile pictures, write bios, and follow other users.


# Defin class (template for instagram user)
import json

class User:
    # This is special method in python called constructor (call automatically when new object is creatae)
    def __init__(self, user_name, bio, profile_picture):
        # Attributes : These are properties every user will have. These decribe the object.
        self.user_name = user_name
        self.bio = bio
        self.profile_picture = profile_picture
    
    # Methods : Actions
    def follow_user(self, another_user):
        return f"{self.user_name} followed {another_user.user_name}"
    
    def to_dictionary(self):
        return{
            "user_name" : self.user_name,
            "bio" : self.bio,
            "profile_picture" : self.profile_picture
        }
    
# create users / objects
user1 = User("Joshi", "Love reading book", "joshi.png")
user2 = User("Kulkarni", "Love travelling..!", "kulkarni.png") 

# access properties and print user1 and user2
print(user1) #<__main__.User object at 0x00000000010F1A50> : python Json can not directly serialize custom class objects. We need to convert it to dictionary first.
print(user2)

# convert to JSON
json_data = json.dumps(user1.to_dictionary())
print(json_data) #{"user_name": "Joshi", "bio": "Love reading book", "profile_picturfe": "joshi.png"}

#call method
result = user1.follow_user(user2)
print(result)

        
        