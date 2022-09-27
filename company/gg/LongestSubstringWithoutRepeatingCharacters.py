# LC 3. Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        res = start = 0
        for i, c in enumerate(s):
            if c in map and start <= map[c]:
                start = map[c] + 1
            else:
                res = max(res, i - start + 1)
            map[c] = i
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))