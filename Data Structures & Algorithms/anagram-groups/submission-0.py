class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = {}
        sorted_strs = []
        for str in strs:
            str = sorted(str)
            str = "".join(str)
            sorted_strs.append(str)

        grouped = {}
        for i, str in enumerate(sorted_strs):
            hashmap[i] = str
        for key, value in hashmap.items():
            grouped.setdefault(value, []).append(key)
        outputs = []    
        for key, value in grouped.items():
            output = []
            for num in value:
                output.append(strs[num])
            outputs.append(output)

        return outputs


