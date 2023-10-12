class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        def is_vowel(ch):
            return ch.lower() in ["a", "e", "i", "o", "u"]

        def to_goat_latin_word(word, pos):
            if not word:
                return ""

            word = word + "ma" if is_vowel(word[0]) else word[1:] + word[0] + "ma"
            return word + "a" * pos

        words = sentence.split(" ")
        return " ".join([to_goat_latin_word(ch, i + 1) for i, ch in enumerate(words)])
