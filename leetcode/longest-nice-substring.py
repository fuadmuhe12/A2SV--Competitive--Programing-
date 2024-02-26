class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        import string

        lowercase_letters = string.ascii_lowercase
        uppercase_letters = string.ascii_uppercase

        dic = dict(zip(lowercase_letters, uppercase_letters))
        dic.update(dict(zip(uppercase_letters, lowercase_letters)))
        mx =  -1
        l = None
        r = None
        for start in range(len(s)):
            required = set()
            seen =  set()

            for end in range(start,len(s) ):

                if s[end] not in seen:
                    seen.add(s[end])
                    if s[end] in required:
                        required.remove(s[end])
                    else:
                        required.add(dic[s[end]])

 
                if len(required) == 0:
                    if end - start +1 > mx:
                        l = start
                        r = end
                        mx = end -start +1
        return s[l:r+1]  if l != None else "" 
                
                    
                









