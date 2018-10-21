"""
Labour work #2
 Check spelling of words in the given  text
"""

from lab_1.main import calculate_frequences

LETTERS = 'abcdefghijklmnopqrstuvwxyz'
REFERENCE_TEXT = ''

if __name__ == '__main__':
    with open('very_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()
        freq_dict = calculate_frequences(REFERENCE_TEXT)


def propose_candidates(word, max_depth_permutations: int=1):

    if (word != '' and word is not None and max_depth_permutations is not None
            and type(max_depth_permutations) == int and max_depth_permutations > 0):
        l_word = word.lower()
        splits = []
        for i in range(len(l_word)+1):
            splits.append([l_word[:i], l_word[i:]])

        deletes = []
        for left, right in splits:
            if right != '':
                deletes.append(left + right[1:])

        interchange = []
        for i in range(len(l_word)-1):
            interchange.append(l_word[:i] + l_word[i + 1] + l_word[i] + l_word[i + 2:])

        inserted = []
        for letter in LETTERS:
            for i in range(len(l_word) + 1):
                inserted.append(l_word[:i] + letter + l_word[i:])

        changed_to_new = []
        for letter in LETTERS:
            for i in range(len(l_word)):
                changed_to_new.append(l_word[:i] + letter + l_word[i+1:])

        all_changes = changed_to_new + inserted + interchange + deletes
        #permutations = len(changed_to_new) + len(inserted) + len(interchange) + len(deletes)
        all_changes_set = set(all_changes)
        clear_changes = list(all_changes_set)
        return clear_changes

    else:
        return []


pass


def keep_known(candidates, as_is_words):
    #filtered_d = []
    filtered_w = []
    if (as_is_words != [] and as_is_words is not None and candidates != []
            and candidates is not None and type(candidates) != tuple):
        """for candidate_key in frequencies.keys:
            if candidate_key in candidates:
                filtered_d.appened(candidate_key)"""
        for candidate in as_is_words:
            if candidate in candidates:
                filtered_w.append(candidate)


pass


def choose_best(frequencies: dict, candidates: tuple) -> str:
    if frequencies != None:
        sort_l = sorted(frequencies.items())
        most_frequent = []

        for pair in sort_l:
            if pair[1] == sort_l[0][1]:
                most_frequent.append(pair)

        most_freq_list = []
        for pair in most_frequent:
            most_freq_list.append(pair[0])
        if candidates != []:
            for candidate in candidates:
                if candidate in most_freq_list:
                    return candidate
        else:
            return 'UNK'
    else:
        return 'UNK'


pass


def spell_check_word(frequencies: dict, as_is_words: tuple, word: str) -> str:
    if word in frequencies or word in as_is_words:
        return word
    else:
        modifications = propose_candidates(word)
        clean = keep_known(modifications, frequencies)
        winner = choose_best(frequencies, clean)
        return winner


pass


def spell_check_text(frequencies: dict, as_is_words: tuple, text: str) -> str:
    for old_word in text:
        if old_word.isalpha():
            word = old_word.lower()
            if word in frequencies or word in as_is_words:
                return word
            else:
                modifications = propose_candidates(word)
                clean = keep_known(modifications, frequencies)
                winner = choose_best(frequencies, clean)
                return winner

    

pass
