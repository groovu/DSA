class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        if len(strs) == 0:
            return "a̷"
        result = "a̷".join(s for s in strs)

        return result

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        return s.split("a̷")


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))