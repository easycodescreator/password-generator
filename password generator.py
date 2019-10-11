import random
items = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S"
,"T","U","W","V","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m",
"n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]

items2 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S"
,"T","U","W","V","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m",
"n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"
,"~","!","@","#","$","%","^","&","*","(",")","_","+"]
def password():
    """ This function generate 2 kind of password;weak password and strong password and
    generate also superstrong password.
    you should follow instruction to generate your favorite password. """
    a = input("""Do you want a weak password or strong password??\npress weak for
     weak password and press strong for strong password...""")

    if a == "weak":
        weak_password = random.sample(items, 8)
        weak_password = "".join(weak_password)
        return weak_password

    elif a == "strong":
        b = input("""Do you want super strong password or just a strong password??\n
        prss sstong for super strong and strong for strong.... """)

        if b == "sstrong":
            superstrong_password = random.sample(items2, 20)
            superstrong_password = "".join(superstrong_password)
            return superstrong_password

        elif b == "strong":
            strong_password = random.sample(items2, 8)
            strong_password = "".join(strong_password)
            return strong_password

print(password())
