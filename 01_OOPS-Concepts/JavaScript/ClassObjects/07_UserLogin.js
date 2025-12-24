// Create a User class:

// Properties: username, password
// Methods: login(inputPassword) and changePassword(oldPass, newPass)

// Rules:
// Login only if password matches
// Password should not be directly accessible

class user{
    userName
    password

    constructor(userName, password){
        if (password.length < 5){
            throw new Error("password must contain more than 5 chars.")
        }

        this.userName = userName
        this.password = password
    }

    login(inputPassword){
        if(inputPassword == this.password){
            console.log("Logged-in successfuly.")
        }else{
            console.log("You have entered wrong password."); 
        }
    }

    changePassword(oldPass, newPass){
        if(oldPass === this.password){
            if(oldPass === newPass){
                console.log("New password should not be same as new password");  
            }else{
                this.password = newPass
            }
        }
        
    }
}

const usr1 = new user("Joshi", "1234")
usr1.login("1234")