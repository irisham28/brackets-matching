#each time, when an open paranthesis is encountered push it into the stack (add it into the stack)
#and when closed paranthesis is encountered, match it with an open one and delete it (pop it)
# if the stack is empty at the end, return balanced otherwise unbalanced. 

open_list = ["(","[","{"]

close_list = [")","]","}"]

def check(mystring):
    stack = []
    for i in mystring:
        if i in open_list: #if we encountered an opening bracket 
            stack.append(i) #pushing into the stack
        elif i in close_list: #if we encountered a closed bracket 
            pos = close_list.index(i) #this will give us the index number of i 
            if (len(stack) > 0 and open_list[pos]==stack[len(stack)-1]):
                stack.pop()
            else:
                print("brackets are not balanced.")

    if len(stack) == 0:
        print("expression is balanced ")
    else:
        print("expression is not balanced")


sentance = "{hello} I am Irisha and I love (volleyball)"
check(sentance)





