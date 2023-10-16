def reverseWords(s: str) -> str:
        s = s.strip()
        s = s.split(' ')
        newstr = ''
        for i in range(len(s)-1,0,-1):
            if len(s[i]) >0:
                newstr+= s[i]+" "
        newstr+= s[0]
        return newstr

print(reverseWords("  hello world  "))