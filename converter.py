height_cm = input('What is your height? (cm)')
weight_kg = input('How much do you weigh? (kg)')

height = float(height_cm)
weight = float(weight_kg)

height_inch = height / 2.54

#There are 12 inches in a foot
height_feet = int(height_inch // 12)
height_inch = round(height_inch % 12)


#1 kg = 2.2046226218 lbs
weight_lb = weight * 2.2046226218 

print(f"You are {height_cm} cm tall, and weigh is {weight_kg} kg.")

print(f"I stand at {height_feet} feet {height_inch} inches and weigh {weight_lb:.2f} pounds.")


