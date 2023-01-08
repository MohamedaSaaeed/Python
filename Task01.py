# creating a function called 'char_change' for replacing a character in a string
def char_change(string, index, character):
    #here we will convert string to list
    l = list(string)
    #choosing specified index to change 
    l[index] = character
    string = ''.join(l)
    #print the string again
    print(string)

char_change('abracadabra', 5, 'k')