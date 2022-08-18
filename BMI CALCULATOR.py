

#BMI CALCULATOR
# designed by jimmy


def bmi_index():

    while True:

        try:
            weight = eval(input("Enter your weight value in kg : "))
            height = eval(input("Enter your height value in cm :"))

            bmi = weight / (height/100) **2

            if (weight < 0 or height < 0):
                myerror =ValueError
                raise myerror

            return bmi

        except ValueError as error:
            print("weight or height cannot be less than zero")

        except ZeroDivisionError:
            print(f" you cant divide number {weight}  by Zero")

        except Exception as error:
            print("Not a number")

result = bmi_index()

print (f"your body mass index is {result:.2f} ")

if result <= 18.5:
    print("The bmi status is underweight")

elif result >=18.5 and result <= 24.9:
    print("Your bmi status is Healthy")

elif result >=25 and result <=29.9:
    print("your bmi status is overweight")

else:
    print("Your bmi status is obese")
print()


def bmi_index_2():

    while True:
        repeat = input("do you wish to continue? (y/n): ")
        if repeat.upper() == 'Y':
            result = bmi_index()
            print(f"your body mass index is {result:.2f} ")
        else:
            print("Bye!")
            break

        if result <= 18.5:
            print("The bmi status is underweight")

        elif result >= 18.5 and result <= 24.9:
            print("Your bmi status is Healthy")

        elif result >= 25 and result <= 29.9:
            print("your bmi status is overweight")

        else:
            print("You bmi status is obese")
        print()


print(bmi_index_2())




























