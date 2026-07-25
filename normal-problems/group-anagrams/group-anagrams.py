import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grupos = {}

        for s in strs:
            chave = ''.join(sorted(s))

            if chave not in grupos:
                grupos[chave] = []

            grupos[chave].append(s)

        return list(grupos.values())