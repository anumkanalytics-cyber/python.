#Student marks calculator
Marks_Eng = int(input("Enter your English marks: "))
Marks_urdu = int(input("Enter your Urdu marks: "))
Marks_maths = int(input("Enter your maths marks: "))
Marks_Chem = int(input("Enter your chemistry marks: "))
Marks_phy = int(input("Enter your physics marks: "))
if Marks_Eng >= 40 and Marks_urdu >= 40 and Marks_maths>= 40 and Marks_Chem >=40 and  Marks_phy >=40:
    print("You passed!")
else:
    print("you failed.")

print("your Marks in English is ", Marks_Eng)
print("your Marks in urdu is", Marks_urdu)
print("your Marks in maths is", Marks_maths)
print("your Marks in Chemistry is ", Marks_Chem)
print("your Marks in physics is " , Marks_phy)
Over_allmarks = Marks_Eng + Marks_Chem + Marks_maths + Marks_phy + Marks_urdu
print("your total marks are", Over_allmarks, "/500")