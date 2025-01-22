class Solution:
    def isValid(self, s: str) -> bool:
        opened = ['(', '[', '{']
        closed = [')', ']', '}']
        open_par, closed_par = 0, 0
        open_bra, closed_bra = 0, 0
        open_dic, closed_dic = 0, 0
        
        # Check if the input length is odd or ends with an opening bracket
        if len(s) % 2 != 0 or s[-1] in opened:
            return False
        
        # Check for invalid adjacent pairs
        for i in range(len(s) - 1):
            if s[i] in opened and s[i + 1] in closed:
                if opened.index(s[i]) != closed.index(s[i + 1]):
                    return False
        
        # Process the string
        while len(s) > 0:
            match s[-1]:
                case ')':
                    closed_par += 1
                    s = s[:-1]
                case ']':
                    closed_bra += 1
                    s = s[:-1]
                case '}':
                    closed_dic += 1
                    s = s[:-1]
                case '(':
                    open_par += 1
                    s = s[:-1]
                    if open_par > closed_par:  # Ensure proper closing order
                        return False
                case '[':
                    open_bra += 1
                    s = s[:-1]
                    if open_bra > closed_bra:  # Ensure proper closing order
                        return False
                case '{':
                    open_dic += 1
                    s = s[:-1]
                    if open_dic > closed_dic:  # Ensure proper closing order
                        return False
        
        # Final check to ensure all open and close counts match
        if open_par == closed_par and open_bra == closed_bra and open_dic == closed_dic:
            return True
        else:
            return False
