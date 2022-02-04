class AllConstructor(object):
    def all_construct_possibilities(self, target_word: str, word_bank: list) -> list:
        if target_word == "":
            return [[]]

        all_ways = []
        for word in word_bank:
            if target_word.startswith(word):
                suffix = target_word[len(word) :]
                suffix_ways = self.all_construct_possibilities(suffix, word_bank)
                target_ways = self.add_word_to_start(word, suffix_ways)
                all_ways = all_ways + target_ways
        return all_ways

    def add_word_to_start(self, word: str, words: list) -> list:
        wordies = words
        for wor in wordies:
            wor.insert(0, word)
        return wordies


construct = AllConstructor()
answer = construct.all_construct_possibilities(
    "purple", ["purp", "p", "ur", "le", "purpl"]
)
print(answer)
