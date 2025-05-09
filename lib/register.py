# Pseudocode

# this is a simple program that takes a list of members 
# member enter the name he wants to check 
# check the name entered whether it exist in the list 
# if the name is available return the member is a registered member 
# if name not found return no a registered member

registered_members = ["David", "Goggins", "Mary", "Kim"]

Name = input("Enter your name: ")
if Name in registered_members:
    print(f"{Name} is a registered member")

    delete = input("Are you enjoying your membership with us? ")
    if delete.lower() == "yes":
        print(f"We are glad to hear that you are enjoying your membership")
    else:
        feedback = input("we would like to help, let us know how we can make it better? ")
        if "delete" and "remove" in feedback.lower():
            registered_members.remove(Name)
            print(f"{Name} we are sorry to see you go, your details has been removed successfully")
        else:
            print("Thank you for your feedback, we value you as our member")
else:
    print(f"{Name} is not a registered member")

    register = input("Would you like to become a member? ")
    if register.lower() == "yes":
        registered_members.append(Name)
        print(f"Dear {Name} you are successfully registered as a member!")

print(registered_members)