class Solution:
    def isValid(self, s: str) -> bool:
        final_string = []
        for each in s:
            if each == ']' or each == '}' or each == ')':
                if not final_string:
                    return False
            if each == '}' :
                if final_string[-1] == '{':
                    final_string.pop()
                else:
                    return False
            if each == ']' :
                if final_string[-1] == '[':
                    final_string.pop()
                else:
                    return False
            if each == ')' :
                if final_string[-1] == '(':
                    final_string.pop()
                else:
                    return False
            if each=='(' or each=='[' or each=='{':
                final_string.append(each)
        if not(final_string):
            return True
        else:
            return False



        