class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = list(magazine)
        ransomNote = list(ransomNote)
        if not ransomNote:
            return False
        for ch in ransomNote:
            try:
                if magazine:
                    magazine.remove(ch)
                    pass
                else:
                    return False
            except ValueError as e:
                return False
        else:
            return True

ransomNote = 'bbbb'
magazine = 'b'

obj = Solution()
print(obj.canConstruct(ransomNote, magazine))
