class Solution:

    def encode(self, strs):
        encoded = []
        for s in strs:
            s = str(len(s)) + "#" + s
            encoded.append(s)
        encoded_string = "".join(encoded)
        return encoded_string


    def decode(self, s):
        remaining = s
        result = []
        while remaining:
            position = remaining.index("#")
            length = remaining[:position]
            word = remaining[(position + 1):(int(length) + (position + 1))]
            result.append(word)
            remaining = remaining[int(length) + (position + 1): ]

        return result
