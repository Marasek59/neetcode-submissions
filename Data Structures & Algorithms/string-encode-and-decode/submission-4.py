class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = []
        for w in strs:
            encoded_string.append(f'{len(w)}#{w}')
        return "".join(encoded_string)

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            start = j + 1
            end = start + length
            decoded_strs.append(s[start:end])
            i = end
        return decoded_strs