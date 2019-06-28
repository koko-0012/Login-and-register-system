
#Username & Password
username = input("Please Type your Username: ")

password = input("Please Type your Password: ")

writefile = open("Reg/users.txt","a")


#Format User:Password
writefile.write(username)

writefile.write(" ")

writefile.write(password)

writefile.write("\n")

writefile.close()

