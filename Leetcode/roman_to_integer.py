def romanToInt(s: str) -> int:
    roman_dict={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    number = 0
    for i in range(len(s)):
        if i>0 and roman_dict[s[i]]>roman_dict[s[i-1]]:
            number = number + roman_dict[s[i]] - 2*roman_dict[s[i-1]]
        else:
            number += roman_dict[s[i]]
    return number

print(romanToInt("MMXXVIII"))
            
