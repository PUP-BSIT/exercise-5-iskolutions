
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
print("3. (Fernette Pearl Franco) Who wrote the play of Romeo and Juliet?")
print("a) Jane Austen        \tb) J.K. Rowling")
print("c) George R.R. Martin \td) William Shakespeare")
answer = input("Enter your answer: ").upper()
if answer == "D":
    print(f"{answer} is correct!")
    score += 1
else:
    print(f"{answer} is incorrect. The correct answer is D")

# Question 4
print("")
print("4. (Fernette Pearl Franco) The largest planet in the solar system?")
print("a) Earth \tb) Jupiter")
print("c) Mars \td) Saturn")
answer = input("Enter your answer: ").upper()
if answer == "B":
    print(f"{answer} is correct!")
    score += 1
else:
    print(f"{answer} is incorrect. The correct answer is B")

# ToDO(Lopez, Jakim): Do question 5 and 6

# ToDO(Gagtan, Hanz Matthew): Do question 7 and 8

# ToDO(Causon, Miko Lorenz): Do question 9 and 10

print(f"Congratulations! You got {score} out of 10 items!")

