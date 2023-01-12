# balanced parentheses in an expression
open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]


# Function to check parentheses
def is_balanced(myStr):
    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                    (open_list[pos] == stack[len(stack) - 1])):
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"


# Driver code
string = "{[()]}"
print(is_balanced(string))

string = "{[(]}"
print(is_balanced(string))

string = "{{[[(())]]}}"
print(is_balanced(string))
