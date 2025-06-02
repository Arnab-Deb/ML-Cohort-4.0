# funtion-->NID and Parameters---->Full name ,Father's name,Mother's name ,DOB ,Nid number,Gender,Address,Nationality


def NID(fullname, fathername, mothername, dob, nid_number, gender, address, nationality):
    print(f"--------NATIONAL ID CARD--------\n Full Name     : {fullname}\n Father's Name : {fathername}\n Mother's Name :{mothername}\n Death of Birth: {dob}\n NID Number    : {nid_number}\n Gender        : {gender}\n Address       : {address}\n Nationality   : {nationality}")


NID("Naruto Uzumaki","Minato Namikaze","Kushina Uzomaki","10-10-1986",1000000000,"male","Hidden Leaf Village","Japanese")   


# Or taking input from users
print("\n----------------------user's input-----------------------\n")

fl=input("Enter your full name: ")
fn=input("Enter your father name: ")
mn=input("Enter your mother name: ")
db=input("Enter your death of birth: ")
nn=input("Enter your nid number: ")
g=input("Type 'Male' or 'Female': ")
ad=input("Enter your address: ")
na=input("Enter you nationality: ")

NID(fl,fn,mn,db,mn,g,ad,na)   
