class CountConstructor(object):
    merged_words = {}

    def can_construct(self, target_word: str, word_bank: list) -> bool:
        if target_word == "":
            return 1
        if target_word in self.merged_words:
            return self.merged_words[target_word]
        total_posibilities = 0
        for word in word_bank:
            if target_word.startswith(word):
                suffix = target_word[len(word) :]
                posibility = self.can_construct(suffix, word_bank)
                total_posibilities = total_posibilities + posibility
        self.merged_words[target_word] = total_posibilities
        return total_posibilities


construct = CountConstructor()
answer = construct.can_construct("purple", ["purp", "p", "ur", "le", "purpl"])
print(answer)
