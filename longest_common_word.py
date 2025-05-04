from trie import Trie

class LongestCommonWord(Trie):
    def find_longest_common_word(self, strings) -> str:
        # Check for invalid input: not a list/tuple, empty, or contains non-strings
        if not isinstance(strings, (list, tuple)) or not strings:
            return ""
        if not all(isinstance(s, str) for s in strings):
            return ""

        # Handle single string case
        if len(strings) == 1:
            return strings[0]

        # Find the shortest string to limit prefix length
        min_length = min(len(s) for s in strings)

        # Compare characters across all strings
        common_prefix = ""
        for i in range(min_length):
            char = strings[0][i]
            if all(s[i] == char for s in strings[1:]):
                common_prefix += char
            else:
                break
        return common_prefix

if __name__ == "__main__":
    # Test 1: Common prefix exists
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl", "Test 1 failed: Expected 'fl'"

    # Test 2: Common prefix exists (longer prefix)
    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters", "Test 2 failed: Expected 'inters'"

    # Test 3: No common prefix
    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == "", "Test 3 failed: Expected ''"

    # Test 4: Empty array
    trie = LongestCommonWord()
    strings = []
    assert trie.find_longest_common_word(strings) == "", "Test 4 failed: Expected ''"

    # Test 5: Single string
    trie = LongestCommonWord()
    strings = ["hello"]
    assert trie.find_longest_common_word(strings) == "hello", "Test 5 failed: Expected 'hello'"

    # Test 6: Invalid input (non-list)
    trie = LongestCommonWord()
    strings = "not a list"
    assert trie.find_longest_common_word(strings) == "", "Test 6 failed: Expected ''"

    # Test 7: Invalid input (contains non-strings)
    trie = LongestCommonWord()
    strings = ["hello", 123, "world"]
    assert trie.find_longest_common_word(strings) == "", "Test 7 failed: Expected ''"

    print("All tests passed successfully!")