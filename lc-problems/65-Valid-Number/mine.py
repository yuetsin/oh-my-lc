class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            float(s.strip())
            return True
        except:
            return False
#         s = s.strip()
#         for i in s:
#             if not i in '0123456789-e.':
#                 return False

#         if ' ' in s:
#             return False
#         if 'e' in s:
#             try:
#                 s1, s2 = s.split('e')[0], s.split('e')[1]
#             except:
#                 return False
#             if '.' in s2:
#                 return False
#             if '-' in s2 and s2[0] != '-':
#                 return False
#             if '.' in s1:
#                 if s1.count('.') > 1:
#                     return False
#                 try:
#                     p1, p2 = s1.split('.')[0], s1.split('.')[1]
#                 except:
#                     return False
#                 if p1.
