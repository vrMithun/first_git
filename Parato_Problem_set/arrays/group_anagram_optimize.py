def groupAnagrams(strs):
    anagrams = {}
    for s in strs:
        # Sort the string to create a key
        key = ''.join(sorted(s))
        if key in anagrams:
            anagrams[key].append(s)
        else:
            anagrams[key] = [s]
    # Return the values of the dictionary, which are the grouped anagrams
    return list(anagrams.values())

# Test cases
print("Test case 1 (Basic anagrams):", groupAnagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']))
# Expected: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

print("Test case 2 (No anagrams):", groupAnagrams(['dog', 'cat', 'bird']))
# Expected: [['dog'], ['cat'], ['bird']]

print("Test case 3 (Empty input):", groupAnagrams([]))
# Expected: []

print("Test case 4 (Single string):", groupAnagrams(['abc']))
# Expected: [['abc']]

print("Test case 5 (Duplicate strings):", groupAnagrams(['aaa', 'aaa', 'aaa']))
# Expected: [['aaa', 'aaa', 'aaa']]

print("Test case 6 (Mixed lengths):", groupAnagrams(['a', 'ab', 'ba', 'abc', 'cba', 'cab']))
# Expected: [['a'], ['ab', 'ba'], ['abc', 'cba', 'cab']]

print("Test case 7 (Strings with spaces):", groupAnagrams(['a b', 'b a', 'ab', ' ba']))
# Expected: [['a b', 'b a'], ['ab'], [' ba']]

print("Test case 8 (Special characters):", groupAnagrams(['@#!', '!#@', '#@!', 'abc']))
# Expected: [['@#!', '!#@', '#@!'], ['abc']]

print("Test case 9 (Case sensitivity):", groupAnagrams(['a', 'A', 'aa', 'AA']))
# Expected: [['a'], ['A'], ['aa'], ['AA']]

print("Test case 10 (Numbers in strings):", groupAnagrams(['123', '231', '312', '456']))
# Expected: [['123', '231', '312'], ['456']])
