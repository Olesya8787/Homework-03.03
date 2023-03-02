gamer = [

]
has_error = False

register_data = ""
register_data = register_data + input("Enter your login : ")
register_data = register_data + " | " + input("Enter your password : ")

gamer = register_data.split( " | ")

if len(gamer[0]) < 5 :
    has_error = True
    print("Login is to short ")    
if len(gamer[1]) > 10 :
    has_error = True
    print("Password is to long ")  
if has_error == False :
    print("The register data is correct")





