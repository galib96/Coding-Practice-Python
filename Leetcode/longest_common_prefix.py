def longestCommonPrefix(strs):
        """
        Takes in a list of strings and returns the longest common prefix among those strings.
        inputs: 
        strs: list of strings
        output:
        a string containing longest common prefix
        """
        # if strs contains no value, it should return "" directly.
        if len(strs) == 0:
            return ""
        
        # element with minimum length. Common Prefix will never be bigger than this.
        com = min(strs, key=len)

        # start with biggest substring of shortest string.
        # if it is found in all strings as prefix, then return it.
        # otherwise check for shorter substrings.
        for i in range(len(com),0,-1):
            if all(s[:i] == com[:i] for s in strs):
                return com[:i]
        
        return ""
        
#checking for different lists
print(longestCommonPrefix([]))
print(longestCommonPrefix(['b','a']))
print(longestCommonPrefix(['abc']))
print(longestCommonPrefix(['ab','a']))
print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["dog","racecar","car"]))