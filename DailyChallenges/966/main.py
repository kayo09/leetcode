from typing import List
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def devowel(word):
            return ''.join('_' if c.lower() in 'aeiou' else c for c in word.lower())
        exact_words = set(wordlist)
        case_insenitive_map = {}
        vowel_error_map = {}
        for word in wordlist:
            lower_word = word.lower()
            if lower_word not in case_insenitive_map:
                case_insenitive_map[lower_word] = word
            devoweled_word = devowel(word)
            if devoweled_word not in vowel_error_map:
                vowel_error_map[devoweled_word] = word
        result = []
        for query in queries:
            if query in exact_words:
                result.append(query)
            elif query.lower() in case_insenitive_map:
                result.append(case_insenitive_map[query.lower()])
            else:
                devow_query = devowel(query.lower())
                if devow_query in vowel_error_map:
                    result.append(vowel_error_map[devow_query])
                else:
                    result.append("")

        return result

solution = Solution()
wordlist = ["KiTe","kite","hare","Hare"]
queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
print(solution.spellchecker(wordlist, queries))
