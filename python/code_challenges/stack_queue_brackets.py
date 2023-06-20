from data_structures.stack import Stack


def multi_bracket_validation(string):
    stack = Stack()
    for bracket in string:
        if bracket in "({[":
            stack.push(bracket)
        elif bracket in ")}]":
            if stack.is_empty():
                return False
            if bracket == ")" and stack.peek() == "(":
                stack.pop()
            elif bracket == "}" and stack.peek() == "{":
                stack.pop()
            elif bracket == "]" and stack.peek() == "[":
                stack.pop()
            else:
                return False
    return stack.is_empty()
