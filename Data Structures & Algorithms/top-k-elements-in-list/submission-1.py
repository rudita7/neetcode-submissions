class Solution:
    def topKFrequent(self, nums, k):
        res = {}
        for num in nums:
            if num in res:
                res[num] += 1
            else:
                res[num] = 1

        sorted_dict = dict(sorted(res.items(), key = lambda item : item[1], reverse=True))
        dict_keys = list(sorted_dict.keys())
        output = []
        for i in range(k):
            output.append(dict_keys[i])
        return sorted(output)