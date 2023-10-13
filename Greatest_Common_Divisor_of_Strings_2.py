# For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

# Example 1:

# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
# Example 2:

# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
# Example 3:

# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
 

# Constraints:

# 1 <= str1.length, str2.length <= 1000
# str1 and str2 consist of English uppercase letters.



def gcdOfStrings(str1: str, str2: str) -> str:

    if str1+str2 != str2+str1:
        return ""
    else:
        l1 = len(str1)
        l2 = len(str2)
        gdiv = 0
        for i in range(1,min(l1,l2)+1):
            if l1%i == 0 and l2%i == 0:
                gdiv = i
        print(l1,l2)
        return str2[:gdiv]

        
print(gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX","TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"))
print("="*30)
print(gcdOfStrings("ABABABAB","ABAB"))
print("="*30)
print(gcdOfStrings("ABABAB","ABAB"))
print("="*30)
print(gcdOfStrings("LEET","CODE"))
print("="*30)
print(gcdOfStrings("NLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGM","NLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGM"))
print("="*30)


#learnings :

# Understand the question clearly