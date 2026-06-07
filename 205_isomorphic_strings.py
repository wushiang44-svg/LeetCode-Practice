class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        table_s_to_t = {}
        tanle_t_to_s = {}
        for i in range(len(s)):
            if s[i] in table_s_to_t:
                if table_s_to_t[s[i]] != t[i]:
                    return False
            else:
                table_s_to_t[s[i]] = t[i]

            if t[i] in tanle_t_to_s:
                if tanle_t_to_s[t[i]] != s[i]:
                    return False
            else:
                tanle_t_to_s[t[i]] = s[i]
        
        return True