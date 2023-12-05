class Solution:
    def largestGoodInteger(self, num: str) -> str:
        good = ""
        if "999" in num:
            return "999"
        elif "888" in num:
            return "888"
        elif "777" in num:
            return "777"
        elif "666" in num:
            return "666"

        elif "555" in num:
            return "555"
        elif "444" in num:
            return "444"
        elif "333" in num:
            return "333"
        elif "222" in num:
            return "222"
        elif "111" in num:
            return "111"
        elif "000" in num:
            return "000"
        else:
            return ""


