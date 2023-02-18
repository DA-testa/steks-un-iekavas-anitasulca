# python3

from collections import namedtuple
import os 
Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next,i+1))
            #pass

        if next in ")]}":
            # Process closing bracket, write your code here
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, next):
                return i+1
            opening_brackets_stack.pop()
    if opening_brackets_stack:
        return opening_brackets_stack[0].position
    return" Success"


def main():
    letter = input("Choose input type- F for file OR I for user input:")
    if letter == "F":
        filename = input(" Enter the name of file :")
        if os.path.exists(filename):
            with open (filename, 'r') as f:
                text = f.read()
        else:
            print ("File doesn't exist")
            return
    elif letter == "I":
        text = input("Enter the text with brackets:")
    else:
        print("Invalid")
        return 
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()
