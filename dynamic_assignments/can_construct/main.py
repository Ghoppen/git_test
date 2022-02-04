class WordConstructor(object):

    merged_words = {}

    def can_construct(self, target_word: str, word_bank: list) -> bool:
        if target_word == "":
            return True
        if target_word in self.merged_words:
            return self.merged_words[target_word]
        for word in word_bank:
            if target_word.startswith(word):
                suffix = target_word[len(word) :]
                if self.can_construct(suffix, word_bank) is True:
                    self.merged_words[target_word] = True
                    return True
        self.merged_words[target_word] = False
        return False


construct = WordConstructor()
answer = construct.can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"])
print(answer)
