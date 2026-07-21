# 271 Encode and Decode Strings

Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}
Machine 2 (receiver) has the function:
vector<string> decode(string s) {
  //... your code
  return strs;
}

# Thoughts and Approaches
Fixed Length Solution: 
If you pick a simple delimiter like , or # to join your strings, the decoding step will break if one of the original strings actually contains that delimiter 
(e.g.,  "hello#world#foo" becomes ambiguous). Therefore, I will create something like this '0005Hello0005World': connect length and string together. 

Regarding decoding process: set a pointer i to track the progress: we first extract the length of each string, then we move past the 4 digit header to the start of the string
and then we slice extract the string because we know the length already. At the end, the pointer is updated to be i+=length of this just completed string. In other words,
we are the at beginning of the next string. 

## Python Code
```Python
class Codec:
    def encode(self, strs: list[str]) -> str:
        res = []
        # Format length as a zero-padded 4-digit integer (e.g. 5 -> "0005")
        for s in strs:
            length = len(s)
            # 1. 把长度转化成固定的 4 位字符串
            length_str = str(length).zfill(4)
            # 2. 把 4 位长度头和原字符串拼接在一起
            chunk = length_str + s
            res.append(chunk)

        # 最后把数组里面的所有 chunk 连接在一起
        return "".join(res)

    def decode(self, s: str) -> list[str]:
        res = []  # 1. Stores the final decoded strings.
        i = 0  # 2. Pointer tracking where we are in s.

        while i < len(s):  # 3. Process s until reaching the end.
            # 4. Extract 4 digits for length (e.g., s[0:4] -> "0005" -> 5)
            length = int(s[i : i + 4])

            # 5. Move past the 4-digit header to the start of content
            i += 4

            # 6. Slice exact string length (s[4:9] -> "hello") & add to list
            res.append(s[i : i + length])

            # 7. Move pointer past content to start of next header
            i += length

        return res  # 8. Return list of original strings
```

## Time Complexity
O(n)

## Space Complexity
O(n) 
