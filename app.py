gamer = [

]

register_data = ""
register_data = register_data + input("Enter your login : ")
register_data = register_data + " | " + input("Enter your password : ")

gamer = register_data.split( " | ")

if len(gamer[0]) < 5 :
    print("Error ")  

if len(gamer[1]) > 10 :
    print("Error")  





