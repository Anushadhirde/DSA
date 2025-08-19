class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        Bracket={'(':')','{':'}','[':']'}
        for i in s:
            if i in Bracket:
                stack.append(i)
            elif i in Bracket.values():
                if not stack:
                    return False
                top_bracket=stack.pop()
                if Bracket[top_bracket] != i:
                    return False
        return not stack

            

        
        
