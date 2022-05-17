#Kilmeters Biked by Dominique Hill

#Get Text information from user
name=input("Enter yur name")

#Get numeric information from user
kilometers_biked = eval(input("Enter kilometers biked"))

#Calculate Miles
miles = kilometers_biked*0.62137

#Display Answer
print("Hello ", name, "Your kilometers biked is ",kilometers_biked, ",which is equal to ", miles, "miles")