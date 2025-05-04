from trie import Trie

class Homework(Trie):
    def count_words_with_suffix(self, pattern) -> int:
        # Check if pattern is None or not a string
        if not isinstance(pattern, str) or pattern is None:
            raise ValueError("Pattern must be a non-empty string")
        if not pattern:
            raise ValueError("Pattern cannot be empty")

        count = 0
        # Iterate over all words in the trie
        for word in self.words():
            if word.endswith(pattern):
                count += 1
        return count

    def has_prefix(self, prefix) -> bool:
        # Check if prefix is None or not a string
        if not isinstance(prefix, str) or prefix is None:
            raise ValueError("Prefix must be a non-empty string")
        if not prefix:
            raise ValueError("Prefix cannot be empty")

        # Check if any word starts with the given prefix
        for word in self.words():
            if word.startswith(prefix):
                return True
        return False

if __name__ == "__main__":
    # Initialize trie and add test words
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    # Test 1: count_words_with_suffix - words ending with pattern
    assert trie.count_words_with_suffix("e") == 1, "Test 1 failed: Expected 1 word ending with 'e'"  # apple
    assert trie.count_words_with_suffix("ion") == 1, "Test 2 failed: Expected 1 word ending with 'ion'"  # application
    assert trie.count_words_with_suffix("a") == 1, "Test 3 failed: Expected 1 word ending with 'a'"  # banana
    assert trie.count_words_with_suffix("at") == 1, "Test 4 failed: Expected 1 word ending with 'at'"  # cat

    # Test 2: count_words_with_suffix - no words with pattern, returns 0
    assert trie.count_words_with_suffix("xyz") == 0, "Test 5 failed: Expected 0 words ending with 'xyz'"
    assert trie.count_words_with_suffix("z") == 0, "Test 6 failed: Expected 0 words ending with 'z'"

    # Test 3: count_words_with_suffix - case sensitivity
    assert trie.count_words_with_suffix("E") == 0, "Test 7 failed: Expected 0 words ending with 'E' (case-sensitive)"

    # Test 4: has_prefix - prefix exists
    assert trie.has_prefix("app") == True, "Test 8 failed: Expected True for prefix 'app'"  # apple, application
    assert trie.has_prefix("ban") == True, "Test 9 failed: Expected True for prefix 'ban'"  # banana
    assert trie.has_prefix("ca") == True, "Test 10 failed: Expected True for prefix 'ca'"  # cat

    # Test 5: has_prefix - prefix does not exist
    assert trie.has_prefix("bat") == False, "Test 11 failed: Expected False for prefix 'bat'"
    assert trie.has_prefix("xyz") == False, "Test 12 failed: Expected False for prefix 'xyz'"

    # Test 6: has_prefix - case sensitivity
    assert trie.has_prefix("APP") == False, "Test 13 failed: Expected False for prefix 'APP' (case-sensitive)"

    # Test 7: Invalid input handling
    try:
        trie.count_words_with_suffix(None)
        assert False, "Test 14 failed: Expected ValueError for None input in count_words_with_suffix"
    except ValueError:
        pass

    try:
        trie.count_words_with_suffix("")
        assert False, "Test 15 failed: Expected ValueError for empty input in count_words_with_suffix"
    except ValueError:
        pass

    try:
        trie.has_prefix(None)
        assert False, "Test 16 failed: Expected ValueError for None input in has_prefix"
    except ValueError:
        pass

    try:
        trie.has_prefix("")
        assert False, "Test 17 failed: Expected ValueError for empty input in has_prefix"
    except ValueError:
        pass

    try:
        trie.count_words_with_suffix(123)
        assert False, "Test 18 failed: Expected ValueError for non-string input in count_words_with_suffix"
    except ValueError:
        pass

    try:
        trie.has_prefix(123)
        assert False, "Test 19 failed: Expected ValueError for non-string input in has_prefix"
    except ValueError:
        pass

    # Test 8: Efficiency test with large dataset
    large_trie = Homework()
    for i in range(10000):
        large_trie.put(f"word{i}", i)
    large_trie.put("testword", 10000)

    # Check performance for suffix
    import time
    start_time = time.time()
    assert large_trie.count_words_with_suffix("word") == 1, "Test 20 failed: Expected 1 word ending with 'word'"
    assert large_trie.count_words_with_suffix("xyz") == 0, "Test 21 failed: Expected 0 words ending with 'xyz'"
    suffix_time = time.time() - start_time

    # Check performance for prefix
    start_time = time.time()
    assert large_trie.has_prefix("test") == True, "Test 22 failed: Expected True for prefix 'test'"
    assert large_trie.has_prefix("xyz") == False, "Test 23 failed: Expected False for prefix 'xyz'"
    prefix_time = time.time() - start_time

    print(f"All tests passed successfully!")
    print(f"Time for suffix search on large dataset: {suffix_time:.4f} seconds")
    print(f"Time for prefix search on large dataset: {prefix_time:.4f} seconds")