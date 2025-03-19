print("QUIZ")
score = 0

# Question 1
print("\n1. (Aaron Kyle D. Efondo) What is the primary function of a router?")
print("a) Connectivity \tc) Processing")
print("b) Storage \t\td) Output") 

answer = input("Enter your answer: ").upper()

if answer == "A":
    print(f"{answer} is correct!")
    score += 1
else:
    print(f"{answer} is incorrect. The correct answer is A")

# Question 2
print("\n2. (Aaron Kyle D. Efondo) What does 'HTTP' stand for?")
print("a) HyperText Transfer Protocol \tc) Hyper Tech Transmission Protocol")
print("b) High Text Transfer Protocol \td) High Transfer Text Protocol")

answer = input("Enter your answer: ").upper()

if answer == "A":
    print(f"{answer} is correct!")
    score += 1
else:
    print(f"{answer} is incorrect. The correct answer is A")

# Question 3
print("\n3. (Fernette Pearl Franco) Who is the first programmer?")
print("a) Grace Hopper \tc) Charles Darwin")
print("b) Charles Babbage \td) Ada Lovelace")

answer = input("Enter your answer: ").upper()

if answer == "D":
    print(f"{answer} is correct!")
    score += 1
else:
    print(f"{answer} is incorrect. The correct answer is D")

# Question 4
print("\n4. (Fernette Pearl Franco) Which file format is used for web pages?")
print("a) .txt \tc) .csv")
print("b) .html \td) .docx")

answer = input("Enter your answer: ").upper()

if answer == "B":
    print(f"{answer} is correct!")
    score += 1
else:
    print(f"{answer} is incorrect. The correct answer is B")

# Question 5
print("\n5. (Jakim D. Lopez) Which of the following is a "
        + "comparison operator in Python?")
print("a) = \t\tc) #")
print("b) == \t\td) &&")

answer = input("Enter your answer: ").upper()

if answer == "B":
    print(f"{answer} is correct!")
    score += 1
else:
    print(f"{answer} is incorrect. The correct answer is B.")

# Question 6
print("\n6. (Jakim D. Lopez) Which data type in Python to " 
        + "represent whole numbers?")
print("a) float \tc) decimal")
print("b) int \t\td) double")

answer = input("Enter your answer: ").upper()

if answer == "B":
    print(f"{answer} is correct!")
    score += 1
else:
    print(f"{answer} is incorrect. The correct answer is B.")

# Question 7
print("\n7. (Hanz Matthew A. Gagtan) What does HTML stand for?")
print("a) HyperText Markup Language \t\tc) HyperTest Markdown Language")
print("b) HyperText Markdown Language \t\td) HyperText Markup Leveler")

answer = input("Enter your answer: ").upper()

if answer == "A":
    print(f"{answer} is correct!")
    score += 1
else:
    print(f"{answer} is incorrect. The correct answer is A.")

# Question 8
print("\n8. (Hanz Matthew A. Gagtan) Which is an operating system?")
print("a) Microsoft Word \tc) Google Chrome")
print("b) Windows \t\td) Microsoft Excel")

answer = input("Enter your answer: ").upper()

if answer == "B":
    print(f"{answer} is correct!")
    score += 1
else:
    print(f"{answer} is incorrect. The correct answer is B.")

# Question 9
print("\n9. (Miko Lorenz O. Causon) Who created Git?")
print("a) Charles Babbage \t\tc) Guido van Rossum")
print("b) Bjarne Stroustrup \t\td) Linus Trovalds")

answer = input("Enter your answer: ").upper()

if answer == "D":
    print(f"{answer} is correct!")
    score += 1
else:
    print(f"{answer} is incorrect. The correct answer is D.")
    
# Question 10
print("\n10. (Miko Lorenz O. Causon) Which one does not belong to the group?")
print("a) C \t\tc) Python")
print("b) C++ \t\td) Go")

answer = input("Enter your answer: ").upper()

if answer == "C":
    print(f"{answer} is correct!")
    score += 1
else:
    print(f"{answer} is incorrect. The correct answer is C.")

# Result
print(f"\nCongratulations! You got {score} out of 10 items.")