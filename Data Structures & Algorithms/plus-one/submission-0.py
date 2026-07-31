class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if i == len(digits) - 1:
                total = digits[i] + 1
                if total >= 10:
                    carry = 1
                    digits[i] = total % 10
                else:
                    carry = 0
                    digits[i] = total
            else:
                if carry == 0:
                    break
                else:
                    total = digits[i] + 1
                    if total >= 10:
                        carry = 1
                        digits[i] = total % 10
                    else:
                        carry = 0
                        digits[i] = total
        if carry == 1:
            digits.insert(0, 1)
        return digits
        