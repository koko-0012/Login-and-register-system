print("Please Lgoin")

#Login Username & Password
username = input("Please Type your Username: ")

password = input("Please Type your Password: ")

for line in open("Reg/users.txt","r").readlines(): #reads the line

    login_01 = line.split()#splits the 2 strings
    
    if username == login_01[0] and password == login_01[1]:
        print("Logined in")
    else:
        print("Wrong Password or login")

