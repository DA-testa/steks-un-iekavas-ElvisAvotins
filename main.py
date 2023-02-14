#Elvis Avotiņš 7.grupa 220RX0898

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    bracket_count = 0
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            bracket_count = bracket_count + 1
            opening_brackets_stack.append(Bracket(next, bracket_count))
        
        if next in ")]}":
            bracket_count = bracket_count + 1
            if not opening_brackets_stack:
                return bracket_count
            elif not are_matching(opening_brackets_stack[-1].char, next):
                return bracket_count
            else:
                opening_brackets_stack.pop()
    if opening_brackets_stack:
        return opening_brackets_stack[0].position
    return "Success"

def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)
if __name__ == "__main__":
    main()
