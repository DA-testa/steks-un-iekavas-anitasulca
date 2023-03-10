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
   
    letter = input("Choose (F) to input file path or (I) to input text: ")
    if letter.strip().lower() == "f":
        path = input("Enter file path: ")
        if os.path.exists(path):
            with open(path, "r") as f:
                text = f.read()
                mismatch = find_mismatch(text)
                print(mismatch)
        else:
           print("Invalid file path!")
    elif letter.strip().lower() == "i":
        text = input("Enter text: ")
        mismatch = find_mismatch(text)
        # Printing answer, write your code here
        print(mismatch)
    else:
        print("Invalid input")


  


if __name__ == "__main__":
    main()
