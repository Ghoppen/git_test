def is_possible_to_construct(target_word: str, word_bank: list) -> bool:
    table = [False for i in range(len(target_word) + 1)]
    table[0] = True

    for position in range(len(target_word)):
        if table[position] is True:
            for word in word_bank:
                sliced_target = target_word[position : position + len(word)]
                if sliced_target == word:
                    table[position + len(word)] = True
    return table[len(target_word)]


print(is_possible_to_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))


def get_amount_of_constructs(target_word: str, word_bank: list) -> int:
    table = [0 for i in range(len(target_word) + 1)]
    table[0] = 1
    for position in range(len(target_word)):
        for word in word_bank:
            new_position = position + len(word)
            sliced_target = target_word[position:new_position]
            if sliced_target == word:
                table[new_position] = table[position] + table[new_position]
    return table[len(target_word)]


print(get_amount_of_constructs("purple", ["purp", "p", "ur", "le", "purpl"]))


def get_all_possible_constructs(target_word: str, word_bank: list) -> list:
    table = [[] for i in range(len(target_word) + 1)]
    table[0] = [[]]
    for position in range(len(target_word)):
        for word in word_bank:
            new_position = position + len(word)
            if target_word[position:new_position] == word:
                combination = table[position]
                for x in combination:
                    x.append(word)
                    table[new_position].append(x)
    for i in table:
        print(i)

    return table[len(target_word)]


print(get_all_possible_constructs("purple", ["purp", "p", "ur", "le", "purpl"]))
