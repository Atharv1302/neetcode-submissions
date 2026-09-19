class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        AnagramKeeper = {}


        for word in strs: 

            sortedVersion = "".join(sorted(word))

            if sortedVersion in AnagramKeeper:
                AnagramKeeper[sortedVersion].append(word)
            else:
                AnagramKeeper[sortedVersion] = [word]


        return list(AnagramKeeper.values())

        






    