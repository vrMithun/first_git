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
print(groupAnagrams(['tttti', 'tttit', 'hhhuh', 'hhuhh', 'tittt']))