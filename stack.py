def Brackets(statement, index, stack):
    if index == len(statement):
        if stack:
            return "Wrong bracket opened but never closed"
        else:
            return "Correct, Nice!"
    else:
        x = statement[index]
        if x in ['(', '[', '{']:
            stack.append(x)
        elif x in [')', ']', '}']:
            if not stack:
                return "Wrong bracket closed but never opened"
            else:
                last_open_bracket = stack.pop()
                if (x == ')' and last_open_bracket != '(') or \
                   (x == ']' and last_open_bracket != '[') or \
                   (x == '}' and last_open_bracket != '{'):
                    return "Wrong Mismatched Brackets"
        return Brackets(statement, index + 1, stack)

while True:
    statement = input("\nEnter a string with parentheses or 'exit' to exit: ")
    if statement.lower() == 'exit':
        print("\nYou have exited the program, Bye!")
        break
    else:
        answer = Brackets(statement, 0, [])
        print("\n",answer)
