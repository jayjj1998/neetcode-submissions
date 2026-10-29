class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

            # loop through each char of the string. if char not in dic then add it with a count of 1. else if it is, add to its count. 

            # do the same for the second string. and the moment the dictionary wants to add a new letter it breaks because we know the words are not the same

        # for char in s:
        #     print(f"{char}")
        #     if char not in anagramCount.keys():
        #         anagramCount[char] = 1

        #     else:
        #         anagramCount[char] +=1

        s_dict = self.createDict(s)
        t_dict = self.createDict(t)

        if s_dict == t_dict:
            return True
        else:
            return False

            
    def createDict(self, word: str) -> dict:
        anagramCount = {}

        for char in word:
            if char not in anagramCount.keys():
                anagramCount[char] = 1
            else:
                anagramCount[char] +=1
        return anagramCount



