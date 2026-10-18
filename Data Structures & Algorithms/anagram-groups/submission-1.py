class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = dict()
        for item in strs:
            item_sorted = "".join(sorted([c for c in item]))
            map[item_sorted] = map.get(item_sorted, []) + [item]
        return [map[item] for item in map]
