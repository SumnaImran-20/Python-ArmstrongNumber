#Program to check 3 digit Armstrong Number

def numbercheck():
  num = int(input("Enter any 3 digit number between 100-999: "))

  #Checking if the number 3 digit
  if num >= 100 and num <= 999:
    print("You entered the number within the range: "+str(num))
    sum = 0

    #find the sum of cube of of each digit
    temp = num
    while temp>0:
       digit = temp % 10
       sum += digit**3
       temp//= 10
 
    #display the result
    if sum ==num:
     print("This is an armstrong number: "+str(sum))
    else:
     print("This is not an armstrong number: "+str(num))

  else:
    print("You did not entered the number within the range: "+str(num))
    print("Try Again!")
    numbercheck()
    

print("-----------------------------------------------")
print("Program to check 3 digit Armstrong Number")
print("-----------------------------------------------")
#print("Enter any 3 digit number between 100-999:")
number = int(input("Enter any 3 digit number between 100-999: "))

#Checking if the number 3 digit
if number >= 100 and number <= 999:
 print("You entered the number within the range: "+str(number))
 sum = 0

 #find the sum of cube of of each digit
 temp = number
 while temp>0:
  digit = temp % 10
  sum += digit**3
  temp//= 10
 
 #display the result
 if sum ==number:
    print("This is an armstrong number: "+str(sum))
 else:
    print("This is not an armstrong number: "+str(number))

else:
    print("You did not entered the number with in range: "+str(number))
    print("Try Again!")
    numbercheck()

print("-------------------THE END-------------------------")
