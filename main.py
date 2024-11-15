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
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"


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


def get_x_y_oper():
    global memory
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
                if len(check_result) != 0:
                    print(check_result)
                print(msg_2)
            elif oper == '/' and y == 0:
                if len(check_result) != 0:
                    print(check_result)
                print(msg_3)
            else:
                if len(check_result) != 0:
                    print(check_result)
                return calculate_result(x, oper, y)
        except:
            print(msg_1)


def messages_creator(msg_index):
    message = "msg_{}".format(msg_index)
    if message == 'msg_10':
        return msg_10
    elif message == 'msg_11':
        return msg_11
    elif message == 'msg_12':
        return msg_12


def is_one_digit(result):
    global memory
    msg_index = 10
    if -10 < result < 10 and result.is_integer():
        while msg_index <= 12:
            m = messages_creator(msg_index)
            print(m)
            ans = input()
            if ans == 'y':
                msg_index += 1
                if msg_index == 13:
                    memory = result
            if ans == 'n':
                break
    else:
        memory = result
    return memory


def message_four(result):
    global memory
    #"Do you want to store the result? (y / n):"
    print(msg_4)
    answer = input()
    if answer == 'y':
        memory = is_one_digit(result)
        message_five()
    if answer == 'n':
        memory = 0
        message_five()


def message_five():
    global memory
    print(msg_5)
    # "Do you want to continue calculations? (y / n):"
    answer = input()
    if answer == 'y':
        result = get_x_y_oper()
        print(result)
        message_four(result)
    if answer == 'n':
        return 'n'


memory = 0
while True:
    result = get_x_y_oper()
    print(result)
    print(msg_4)
    answer = input()
    if answer == 'y':
        memory = is_one_digit(result)
        five = message_five()
        if five is None or five == 'n':
            break
    if answer == 'n':
        memory = 0
        five = message_five()
        if five is None or five == 'n':
            break
