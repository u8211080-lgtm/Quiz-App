
score = 0


print("What is the capital of France")
print("A) Paris")
print("B) London")
print("C) Berlin")
print("D) Rome")
answer = input("What is your answer?")

if answer.strip().upper() == "A":
    print("Correct!")
    score+= 1 
else:
    print("Incorrect.")

print("What is the highest selling series of all time?")
print("A) Percy Jackson")
print("B) The Magic Treehouse")
print("C) Harry Potter")
print("D) Goosebumps")
answer = input("What is your answer?")

if answer.strip().upper() == "C":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

print("Who made the equation E=mc^2")
print("A) Issac Newton")
print("B) Albert Einstien")
print("C) Ada Lovelace")
print("D) Stephen Hawking")
answer = input("What is your answer?")

if answer.strip().upper() == "B":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

print("What is the largest ocean on Earth?")
print("A) Atlantic Ocean")
print("B) Indian Ocean")
print("C) Arctice Ocean")
print("D) Pacific Ocean")
answer = input("What is your answer?")

if answer.strip().upper() == "D":
    print ("Correct!")
    score += 1
else:
    print ("Incorrect")

print("What gas do plants use for photosynthesis?")
print("A) Oxygen")
print("B) Hydrogen")
print("C) Carbon Dioxide")
print("D) Nitrogen")
answer = input("What is your answer?")

if answer.strip().upper() == "C":
    print("Correct!")
    score+= 1 
else:
    print("Incorrect")

print("Which country is known as The Land of the Rising Sun?")
print("A) China")
print("B) Japan")
print("C) Australia")
print("D) South Korea")
answer = input("What is your answer?")

if answer.strip().upper() == "B":
    print("Correct!")
    score+= 1
else:
    print("Incorrect")

print("Your final score is,", score)
            
    
    






