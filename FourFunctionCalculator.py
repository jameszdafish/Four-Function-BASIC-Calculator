Expression = input("This is a four-function calculator. Please type the expression here: ")
# Expression = "4+1/5"

print("The original expression is: " + str(Expression))

steps = 0

text = ""
numbers = ""
res = []
for i in Expression:
    if steps == 0:
        if i.isdigit():
            numbers += i
            steps += 1
        else:
            print("Please rerun the code with your expression starting with an integer.")
            exit()
    else:
        if i.isdigit():
            numbers += i
        else:
            res.append(numbers)
            numbers = ""
            text += i
            res.append(text)
            text = ""
res.append(numbers)

print(res)
print("^Final Result. Time to turn these into integers and operate!")


def add(num1, num2):
    print("We are adding now!")
    temp_answer = int(num1) + int(num2)
    return temp_answer


def subtract(num1, num2):
    print("We are subtracting now!")
    temp_answer = int(num1) - int(num2)
    return temp_answer


def divide(num1, num2):
    print("We are dividing now!")
    temp_answer = int(int(num1) / int(num2))
    return temp_answer


def multiply(num1, num2):
    print("We are multiplying now!")
    temp_answer = int(num1) * int(num2)
    return temp_answer


while len(res) > 1:
    stop_timer = 0

    if res[1] == "+":
        stored = add(res[0], res[2])
        res = res[3:]
        res.insert(0, str(stored))
        print(res)  # check
    elif res[1] == "-":
        stored = subtract(res[0], res[2])
        res = res[3:]
        res.insert(0, str(stored))
        print(res)  # check
    elif res[1] == "/":
        stored = divide(res[0], res[2])
        res = res[3:]
        res.insert(0, str(stored))
        print(res)  # check
    elif res[1] == "*":
        stored = multiply(res[0], res[2])
        res = res[3:]
        res.insert(0, str(stored))
        print(res)  # check
    else:
        stop_timer += 1

    if stop_timer == 1:
        break

print("Your answer is " + res[0])
