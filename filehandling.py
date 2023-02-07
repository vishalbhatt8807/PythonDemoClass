f = open("test","r")

#print(f.read())

#write value in new abc if not present than it create new file but overwrite existing value
#f1 = open("abc","w")
#print(f1.write("anv"))


#for data in f:
 #   f1.write(data)

# a- append value
#f2 = open("abc","a")
#f2.write("This is file abc")

#read binary
f3 = open("IMG_9475.JPG","rb")
#print(f3.read())

#write binary
f4 = open("newImage.JPG",'wb')
for data in f3:
    f4.write(data)