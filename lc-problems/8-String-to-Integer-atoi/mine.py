class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        result = 0
        for i in str.split(' '):
            if i == "":
                continue
            if i.isdigit() or i[1:].isdigit() or i.replace('.', '').isdigit():
                try:
                    result = int(float(i))
                    break
                except ValueError:
                    return 0
            return 0

        if result > 2147483647:
            return 2147483647
        if result < -2147483648:
            return -2147483648

        return result
