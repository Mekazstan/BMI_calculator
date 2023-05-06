# Defining a function that prints out a formatted table displaying the BMI classifications and their corresponding health risks.
def printOut():
    print("""
        BMI         |    Classification    |     Health Risk
    <---------------|----------------------|----------------------->
        Under 18.5  |   Underweight        |    Minimal
        18.5 - 24.9 |   Normal Weight      |    Minimal
        25 - 29.9   |   Overweight         |    Increased
        30 - 34.9   |   Obese              |    High
        35 - 39.9   |   Severely Obese     |    Very High
        40 & Over   |   Morbidly Obese     |    Extremely High   
        
    """)

# Defining a function that calculates the BMI (Body Mass Index) based on the user's weight and height inputs    
def weightCalculator():
    BMI = (weight * 703) / (height * height)
    print(BMI)
    if BMI>0:
        if(BMI<18.5):
            return name +", you are underwight."
        elif (BMI<=24.9):
            return name +", you are normal weight."
        elif (BMI<=29.9):
            return name +", you are overweight. You need to exercise more and stop sitting and writing so many python tutorials."
        elif (BMI<=34.9):
            return name +", you are obese. Stop eating too much food."
        elif (BMI<=39.9):
            return name +", you are severely obese. Only God can help you."
        else:
            return name +", you are morbidly obese."
    else:
        return "Enter valid input"
    
    
printOut()

# Collecting user's inputs
name = input("Enter you name: ")

weight = int(input("Enter your weight in pounds: "))

height = int(input("Enter your height in inches: "))

# Printing the result (return value) of the weightCalculator() function
print(weightCalculator())
