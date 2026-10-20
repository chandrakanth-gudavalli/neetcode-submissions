class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map_dict = dict()
        for item in nums:
            map_dict[item] = map_dict.get(item, 0) + 1
        freq_list = [[item, map_dict[item]] for item in map_dict]
        freq_list = sorted(freq_list, key=lambda x:-x[1])
        return [item[0] for item in freq_list[:k]]
        