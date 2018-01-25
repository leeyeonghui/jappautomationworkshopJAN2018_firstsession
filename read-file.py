file = open("testfile.txt","r")

#Exercise 1
#file.write("Hello BIG World\n")
#file.write("This is our new text file\n")
#file.write("and this is another line.\n")
#file.write("Why? Because we can.\n")

#Exercise 2
#dataline =["Hello BIG World","This is our new text file","and this is another line.","Why? Because we can."]
#file.write(dataline[3] + "\n")
#file.write(dataline[2] + "\n")
#file.write(dataline[1] + "\n")
#file.write(dataline[0] + "\n")

#Exercise 3
#dataline =["Hello BIG World","This is our new text file","and this is another line","Why? Because we can"]
count=0
for x in file:
	count=count+1
	print x
print("Count is: " + str(count))
file.close()
