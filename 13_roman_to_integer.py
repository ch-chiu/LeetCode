class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        syms_dict = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90,
                     "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1}
        s = s.strip()
        i = 0
        num = 0
        while i < len(s):
            if i+1 < len(s):
                if s[i] == "I":
                    if s[i + 1] == "X":
                        num += 9
                        i += 2
                    elif s[i + 1] == "V":
                        num += 4
                        i += 2
                    else:
                        num += syms_dict["I"]
                        i += 1
                elif s[i] == "X":
                    if s[i + 1] == "C":
                        num += 90
                        i += 2
                    elif s[i + 1] == "L":
                        num += 40
                        i += 2
                    else:
                        num += syms_dict["X"]
                        i += 1
                elif s[i] == "C":
                    if s[i + 1] == "M":
                        num += 900
                        i += 2
                    elif s[i + 1] == "D":
                        num += 400
                        i += 2
                    else:
                        num += syms_dict["C"]
                        i += 1
                else:
                    num += syms_dict[s[i]]
                    i += 1
            else:
                num += syms_dict[s[i]]
                i += 1

        return num
