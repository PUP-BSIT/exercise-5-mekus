
user_score = 0  # Variable to store the user's score

# Question 1
print("\n(Jermaine) Question 1: What is the derivative of "
        + "f(x) = 3x^2 + 2x + 1?")
print(" a. 3x + 2                c. 6x + 2")
print(" b. 6x + 1                d. 3x^2 + 2")

user_answer = input("Enter your answer: ").upper()

if user_answer == 'C':
    print("You got the correct answer!")
    user_score += 1
else:
    print(f"{user_answer} is incorrect. The correct answer is C.")


# Question 2
print("\n(Jermaine) Question 2: What is the value of the limit "
        + "as x approaches 2 of (x^2 - 4)/(x - 2)?")
print(" a. 2                     c. 4")
print(" b. 0                     d. 3")

user_answer = input("Enter your answer: ").upper()

if user_answer == 'C':
    print("You got the correct answer!")
    user_score += 1
else:
    print(f"{user_answer} is incorrect. The correct answer is C.")


# Question 3
print("\n(Rollan) Question 3: What is the SI unit of force?")
print("a. Joule             c. Newton")
print("b. Watt              d. Pascal")

user_answer = input("Enter your answer: ").upper()

if user_answer == "C":
    print("You got the correct answer!")
    user_score += 1
else:
    print(f"{user_answer} is incorrect. The correct answer is C.")


# Question 4
print("\n(Rollan) Question 4: Which of the following laws states that an object" 
        + " in motion stays in motion unless acted upon by an external force?")
print("a. Newton's First Law                c. Newton's Third Law")
print("b. Newton's Second Law               d. Law of Universal Gravitation")

user_answer = input("Enter your answer: ").upper()

if user_answer == "A":
    print("You got the correct answer!")
    user_score += 1
else:
    print(f"{user_answer} is incorrect. The correct answer is A.")
    
    
# Question 5
print("\n(DannKyle) Question 5: What is the formula for speed?")
print("a) speed = distance/time                 c) speed = distance * time")
print("b) speed = distance + time               d) speed = distance - time")

user_answer = input("Enter your answer: ").upper()

if user_answer == "A":
    print("You got the correct answer!")
    user_score += 1
else:
    print(f"{user_answer} is incorrect. The correct answer is A.")


# Question 6
print("\n(DannKyle) Question 6: A car travels 150 km in 3 hours. "
        + "What is its average speed?")
print("a) 50 km/h               c) 45 km/h")
print("b) 55 km/h               d) 60 km/h")

user_answer = input("Enter your answer: ").upper()

if user_answer == "A":
    print("You got the correct answer!")
    user_score += 1
else:
    print(f"{user_answer} is incorrect. The correct answer is A.")


# Question 7
print("\n(John Albert) Question 7: A 2 kg object is moving at 4 m/s. " 
        + "What is the kinetic energy of the object?")
print("a) 8 J               c) 32 J")
print("b) 16 J              d) 4 J")

user_answer = input("Enter your answer: ").upper()

if user_answer == "B":
    print("You got the correct answer!")
    user_score += 1
else:
    print(f"{user_answer} is incorrect. The correct answer is B.")
    
    
# Question 8
print("\n(John Albert) Question 8: A 100 N force is applied to a 5 kg object. " 
        + "What is the acceleration produced? (Ignore friction)")
print("a) 20 m/s^2              c) 5 m/s^2")
print("b) 25 m/s^2              d) 50 m/s^2")

user_answer = input("Enter your answer: ").upper()

if user_answer == "A":
    print("You got the correct answer!")
    user_score += 1
else:
    print(f"{user_answer} is incorrect. The correct answer is A.")
 
 
# Question 9 
print("\n(Joshua) Question 9: What type of energy is stored " 
        + " in a stretched rubber band?")
print("a) Kinetic energy             c) Thermal energy")
print("b) Potential energy           d) Electrical energy")

user_answer = input("Enter your answer: ").upper()

if user_answer == "B" :
    print("You got the correct answer!")
    user_score += 1
else:
    print(f"{user_answer} is incorrect. The correct answer is B.")
    
    
# Question 10
print("\n(Joshua) Question 10: Which law explains action " 
        + "and reaction forces?")
print(" a) First Law                c) Third Law")
print(" b) Second Law               d) Fourth Law")

user_answer = input("Enter your answer: ").upper()

if user_answer == "C" :
    print("You got the correct answer!")
    user_score += 1
else:
    print(f"{user_answer} is incorrect. The correct answer is C.")
 
 
# Display the user's score
print(f"\nCongratulations! You got {user_score} out of 10 items")