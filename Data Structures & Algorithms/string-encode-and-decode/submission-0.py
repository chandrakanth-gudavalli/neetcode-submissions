class Solution:

    def encode(self, strs: List[str]) -> str:
        lengths = [len(item) for item in strs]
        result = "".join([str(lengths[i]) + "#" + strs[i] for i in range(len(strs))])
        return result

    def get_next_hash(self, start_index, s):
        for i in range(start_index, len(s)):
            if s[i] == "#":
                return i


    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        
        res_list = []

        len_start_index = 0
        next_hash_index = self.get_next_hash(len_start_index, s)
        while next_hash_index and next_hash_index < len(s):
            curr_len = int(s[len_start_index:next_hash_index])
            
            if curr_len == 0:
                res_list.append("")
            else:
                curr_str = s[next_hash_index+1: next_hash_index+1+curr_len]
                res_list.append(curr_str)
            
            len_start_index = next_hash_index+1+curr_len
            next_hash_index = self.get_next_hash(len_start_index, s)
            

        return res_list

