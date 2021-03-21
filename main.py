from VividHues import Clr
import random
#====================
first_val = random.choice([False,True])
second_val = random.choice([False,True])
operators = ["AND","OR","XOR","NOT"]
rand_operator = random.choice(operators)
all_not = random.choice([False,True])

if rand_operator == "AND":
  question = f"{first_val} {rand_operator} {second_val}"
  actual_result = first_val and second_val
elif rand_operator == "OR":
  question = f"{first_val} {rand_operator} {second_val}"
  actual_result = first_val or second_val
elif rand_operator == "XOR":
  question = f"{first_val}  {second_val}"
  actual_result = first_val ^ second_val
elif rand_operator == "NOT":
  question = f"{rand_operator} {first_val}"
  actual_result = not first_val

if all_not is True:
  actual_result = not actual_result
  question = f"NOT ({question})"

print(question)
user_answer = input("Enter your answer\n\t--> ").title()

if user_answer == str(actual_result):
  print("Correct!")
else:
  print("Incorrect")
  print(f"The answer was: {actual_result}")