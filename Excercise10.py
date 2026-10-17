W = float(input("Enter your weight(kg): "))
H = float(input("Enter your height(m): "))
BMI = W / (H*H)
if  BMI <= 18.5 :
    print("Underweight.")
elif BMI >= 18.9 and BMI <= 24.9 :
    print("Normal range.")
elif BMI >= 30 :
    print("obesity range")
