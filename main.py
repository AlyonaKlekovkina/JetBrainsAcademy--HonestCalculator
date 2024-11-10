msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"


def calculate_result(x, op, y):
    result = 0
    if op == '+':
        result = x + y
    elif op == '-':
        result = x - y
    elif op == '*':
        result = x * y
    elif op == '/':
        result = x / y
    return result


def check(v1, v2, v3):
    msg = ''
    if -10 < v1 < 10 and v1.is_integer() and -10 < v2 < 10 and v2.is_integer():
        msg += msg_6
    if (v1 == 1 and v3 == '*') or (v2 == 1 and v3 == '*'):
        msg += msg_7
    if (v1 == 0 or v2 == 0 and v3 == '*') or (v1 == 0 or v2 == 0 and v3 == '+') or (v1 == 0 or v2 == 0 and v3 == '-'):
        msg += msg_8
    if msg != '':
        msg = msg_9 + msg
    return msg


def get_x_y_oper(memory):
    while True:
        print(msg_0)
        calc = input().split()
        x = calc[0]
        oper = calc[1]
        y = calc[2]

        if x == 'M':
            x = memory
        if y == 'M':
            y = memory
        operations = ['+', '-', '*', '/']
        try:
            x = float(x)
            y = float(y)
            check_result = check(x, y, oper)
            if oper not in operations:
                print(check_result)
                print(msg_2)
            elif oper == '/' and y == 0:
                print(check_result)
                print(msg_3)
            else:
                print(check_result)
                return x, oper, y
        except:
            print(check_result)
            print(msg_1)


def result_storage(details):
    print(msg_4)
    #"Do you want to store the result? (y / n):"
    answer = input()
    if answer == 'y':
        memory = calculate_result(details[0], details[1], details[2])
        print(msg_5)
        #"Do you want to continue calculations? (y / n):"
        second_answer = input()
        if second_answer == 'y':
            details = get_x_y_oper(memory)
            return calculate_result(details[0], details[1], details[2])
        if second_answer == 'n':
            return 'n'
    if answer == 'n':
        print(msg_5)
        memory = 0
        #"Do you want to continue calculations? (y / n):"
        second_answer = input()
        if second_answer == 'y':
            details = get_x_y_oper(memory)
            result = calculate_result(details[0], details[1], details[2])
            return result
        if second_answer == 'n':
                return 'n'


memory = 0
details = get_x_y_oper(memory)
if len(details) == 3:
    print(calculate_result(details[0], details[1], details[2]))
else:
    print(details)
while True:
    memory = result_storage(details)
    if memory == 'n':
        break
    else:
        print(memory)
