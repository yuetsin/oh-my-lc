class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        st = str(x)
        s = st.replace('-', '')
      #  if len(s) > 10:
      #     return 0
      #  elif len(s) == 10:
      #      if int(s[0]) > 2:
      #          return 0
      #      if int(s[-1]) > 2:
      #          return 0
        if s != st:
            s += '-'
        r = int(s[::-1])

        if r > 2147483647:
            return 0
        if r < -2147483648:
            return 0
        return r
