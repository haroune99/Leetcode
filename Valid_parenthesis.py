class Solution:
    def isValid(self, s: str) -> bool:
        #open_par = ['(','{','[']
        #close_par = [')','}',']']
        open_par = 0
        closed_par = 0
        open_bra = 0
        closed_bra = 0
        open_dic = 0
        closed_dic = 0
        if len(s)%2 !=0:
            return False
        else:
            while len(s)>0:
                match s[-1]:
                    case ')':
                       closed_par +=1
                       s = s[:-1] 
                    case ']':
                       closed_bra +=1
                       s = s[:-1]  
                    case '}':
                       closed_dic +=1
                       s = s[:-1]  
                    case '(':
                       open_par +=1
                       s = s[:-1]  
                    case '[':
                       open_bra +=1
                       s = s[:-1]  
                    case '{':
                       open_dic +=1
                       s = s[:-1] 

            if (open_par == closed_par) and (open_bra == closed_bra) and (open_dic == closed_dic):
                return True
            else:
                return False



            

