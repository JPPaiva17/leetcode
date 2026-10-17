class Solution:
    def intToRoman(self, num: int) -> str:
        roman_map = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        result = []
        for t in roman_map:
            if num >= t[0]:
                result.append(num//t[0] * t[1])
                num %= t[0]

        return "".join(result)
