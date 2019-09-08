'''
Simran Soin
CS 1134
HW5 Q1
'''
def separate_tokens(s, variable_names):
    lst = s.split(" ")
    for token in range(len(lst)):
        if lst[token].isdigit():
            lst[token] = int(lst[token])
        if lst[token] in variable_names:
            lst[token] = variable_names[lst[token]]
    return lst

def assignment_expression(tokens):
    variable_name = tokens[0]
    expression = tokens[2:]
    return (variable_name, arithmetic_expression(expression))

def arithmetic_expression(tokens):
    operators = "*+-/"
    while len(tokens) > 1:
        for token in range(len(tokens)):
            if type(tokens[token]) is str and tokens[token] in operators:
                last_two_nums = tokens[token-2:token]
                if tokens[token] == "*":
                    result = last_two_nums[0] * last_two_nums[1]
                elif tokens[token] == "/":
                    result = last_two_nums[0] / last_two_nums[1]
                elif tokens[token] == "+":
                    result = last_two_nums[0] + last_two_nums[1]
                elif tokens[token] == "-":
                    result = last_two_nums[0] - last_two_nums[1]
                else:
                    raise Exception("unauthorized function")
                del tokens[token-2:token+1]
                tokens.insert(token-2, result)
                break
    return tokens[0]
    
def main():
    user_input = input("--> ")
    variable_names = {}
    while user_input != "done()":
        tokens = separate_tokens(user_input, variable_names)
        if "=" in user_input:
            variable_val = assignment_expression(tokens)
            name = variable_val[0]
            val = variable_val[1]
            variable_names[name] = val
            print(name)
        elif user_input in variable_names:
            print(variable_names[user_input])
        else:
            print(arithmetic_expression(tokens))
        user_input = input("--> ")

main()
