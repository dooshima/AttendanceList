import time

start = time.time()
i = 0;
count = int(input("how many attendences do you want: "))
filename = input ("filename: ");
while i < count:
   
    with open (filename, mode = "a",encoding = 'utf-8') as f:
              f.write("\n")
              f.write("Name\tEmail\tGender\tLocation")
              f.write("\n")
              name = f.write(input("Enter Your Full Name: "));
              f.write("\t")
              email = f.write(input("Enter Your Email: "));
              f.write("\t")
              gender = f.write (input("Specify your gender e.g Male , Female: "));
              f.write("\t")
              loc = f.write(input("Enter Your Location: "));
              f=open(filename, mode = "rt")
              if email in f:
                  break
              i += 1;
              #loop that checks if user has already entered
              f.close()
              
else:
        print("you have logged in")
        end = time.time()
        print(end - start,"seconds")



    

      
