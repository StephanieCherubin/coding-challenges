class Solution:
    def countSegments(self, s: str) -> int:
        if len(s) == s.count(" "):
            return 0
        else: 
            s = s.strip()
            ssplit = s.split()

        return (len(ssplit))