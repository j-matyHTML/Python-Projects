import pywhatkit

#Print instructions and line
print("Please enter the numbers without spaces and with phone prefix")
print("-------------------------------------------------------------")
#Define variables as user input
number = input("Enter number to send message to")
message = input("Enter the message")
time = input("Enter the time you want the message to be delivered")
#Use imported module to send the message to desired number
pywhatkit.sendwhatmsg(''+number, ' '+message, 18, 49)
