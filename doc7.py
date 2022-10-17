# Write function bmi that calculates body mass index (bmi = weight / height2).
# if bmi <= 18.5 return "Underweight"
# if bmi <= 25.0 return "Normal"
# if bmi <= 30.0 return "Overweight"
# if bmi > 30 return "Obese"

def BMI(height, weight): 
  bmi = weight/(height**2) 
  return bmi 

height = float(input('enter the height'))
weight = float(input('enter the weight'))

bmi = BMI(height, weight) 
print("The BMI is", format(bmi))

print("Health status = ",end="")
if (bmi < 18.5): 
  print("Your weight is Underweight") 

elif ( bmi >= 18.5 and bmi < 24.9): 
  print("You are Healthy") 

elif ( bmi >= 24.9 and bmi < 30): 
  print("Your weight is Overweight") 

elif ( bmi >=30): 
  print("Suffering from Obesity")