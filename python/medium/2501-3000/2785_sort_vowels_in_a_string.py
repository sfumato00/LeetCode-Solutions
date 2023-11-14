class Solution:
    def sortVowels(self, s: str) -> str:
        
        VOWEL = set("aeiouAEIOU")
        vowels = sorted([c for c in s if c in VOWEL])
        output = [vowels.pop() if c in VOWEL else c for c in s[::-1]]
        return "".join(output[::-1])