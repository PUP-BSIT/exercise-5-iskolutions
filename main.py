
print("QUIZ")
score = 0

# Question 1
print("")
print("1. (Aaron Kyle D. Efondo) What is the primary function of a router?")
print("a) Connectivity \tb) Storage")
print("c) Processing \t\td) Output") 
answer = input("Enter your answer: ").upper()
if answer == "A":
    print(f"{answer} is correct!")
    score += 1
else:
    print(f"{answer} is incorrect. The correct answer is A")

# Question 2
print("")
print("2. (Aaron Kyle D. Efondo) What does 'HTTP' stand for?")
print("a) HyperText Transfer Protocol \t\tb) High Text Transfer Protocol")
print("c) Hyper Tech Transmission Protocol \td) High Transfer Text Protocol") 
answer = input("Enter your answer: ").upper()
if answer == "A":
    print(f"{answer} is correct!")
    score += 1
else:
    print(f"{answer} is incorrect. The correct answer is A")

# Question 3
print("")
print("3. (Fernette Pearl Franco) Who is the first programmer?")
print("a) Grace Hopper \tb) Charles Babbage")
print("c) Charles Darwin \td) Ada Lovelace")
answer = input("Enter your answer: ").upper()
if answer == "D":
    print(f"{answer} is correct!")
    score += 1
else:
    print(f"{answer} is incorrect. The correct answer is D")

# Question 4
print("")
print("4. (Fernette Pearl Franco) Which file format is used for web pages?")
print("a) .txt \tb) .html")
print("c) .csv \td) .docx")
answer = input("Enter your answer: ").upper()
if answer == "B":
    print(f"{answer} is correct!")
    score += 1
else:
    print(f"{answer} is incorrect. The correct answer is B")

# Question 5
print("\n5. (Jakim D. Lopez) Which of the following is a comparison operator in Python?")
print("a) =\t\tc) #")
print("b) ==\t\td) &&")

answer = input("Enter your answer: ").upper()

if answer == "B":
    print("B is correct!")
    score += 1
else:
    print(f"{answer} is incorrect. The correct answer is B.")

# Question 6
print("\n6. (Jakim D. Lopez) Which data type in Python is used to represent whole numbers?")
print("a) float\tc) decimal")
print("b) int\t\td) double")

answer = input("Enter your answer: ").upper()

if answer == "B":
    print("B is correct!")
    score += 1
else:
    print(f"{answer} is incorrect. The correct answer is B.")

# Question 7
print("\n7. (Hanz Matthew A. Gagtan) What does HTML stand for?")
print("a) HyperText Markup Language\t\tc) HyperText Markdown Language")
print("b) HyperText Markdown Language\t\td) HyperText Markup Leveler")

answer = input("Enter your answer: ").upper()

if answer == "A":
    print("A is correct!")
    score += 1
else:
    print(f"{answer} is incorrect. The correct answer is A.")

# Question 8
print("\n8. (Hanz Matthew A. Gagtan) Which of the following is an example of an operating system?")
print("a) Microsoft Word\tc) Google Chrome")
print("b) Windows 10\t\td) Microsoft Excel")

answer = input("Enter your answer: ").upper()

if answer == "B":
    print("B is correct!")
    score += 1
else:
    print(f"{answer} is incorrect. The correct answer is B.")

# ToDO(Causon, Miko Lorenz): Do question 9 and 10

print(f"Congratulations! You got {score} out of 10 items!")

