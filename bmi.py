def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight/(height*height)

    print("BMI = :", bmi)

    if bmi < 18.5:
        print("Under Weight")
    elif bmi >= 18.5 or bmi <= 25.0:
        print("Normal Weight")
    else:
        print("Overweight")


calculate_bmi(1.73, 57)
