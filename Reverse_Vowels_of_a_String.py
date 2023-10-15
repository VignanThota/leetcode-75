# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

# Example 1:

# Input: s = "hello"
# Output: "holle"
# Example 2:

# Input: s = "leetcode"
# Output: "leotcede"
 

# Constraints:

# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.


def reverseVowels(s: str) -> str:
    vowles = 'aeiouAEIOU'
    stri = ''

    for i in s:
        if i in vowles:
            stri+=i

    ptr = 0
    newstr = ''

    for i in range(len(s)-1,-1,-1):
        if s[i] in vowles:
            newstr += stri[ptr]
            ptr +=1
        else:
            newstr += s[i]

    newstr = newstr[::-1]


reverseVowels('hello')
reverseVowels('leetcode')
