#task 1: user input(3 numbers)
#task 2: 3 frnds and find lowest cgpa and avg cgpa

x=float(input("Put the value for x :"))
y=float(input("Put the value for y :"))
z=float(input("Put the value for z :"))
print("x= ",x, "y= ",y,"z= ",z )

if x>y and x>z:
    print("x is largest and the value is :",x)
elif y>x and y>z:
    print("y is largest and the value is :",y)
else:
    print("z is largest and the value is :",z)
    
print("\n------------------- cgpa------------------------\n")

# 3 friends cgpa
Na=float(input("Naruto's cgpa :"))
Sa=float(input("Sasuke's cgpa :"))
Sak=float(input("Sakura's cgpa :"))
print ("Naruto's cgpa : ",Na, "Sasuke's cgpa : ",Sa,"Sakura's cgpa : ",Sak)

if Na<Sa and Na<Sak:
    print("Naruto has lowest Cgpa :",Na)
elif Sa<Na and Sa<Sak:
    print("Sasuke has lowest cgpa :",Sa)
else:
    print("Sakura has lowest cgpa :",Sak)

avg=(Na+Sa+Sak )/ 3

txt=f"The average cgpa is : {avg}"
print (txt)
