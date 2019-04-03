class Solution:
    length = 0
    def plusOne(self, digits: List[int], at = 1) -> List[int]:
        if self.length == 0:
            self.length = len(digits)
        if at != self.length:
            # Not the highest bit
            digits[self.length - at] += 1
            if digits[self.length - at] == 10:
                digits[self.length - at] = 0
                self.plusOne(digits, at + 1)
        else:
            digits[self.length - at] += 1
            if digits[self.length - at] == 10:
                digits[self.length - at] = 0
                digits.insert(0, 1)
        if at == 1:
            return digits