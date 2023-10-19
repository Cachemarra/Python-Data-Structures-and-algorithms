# %% WRITE GROUP_ANAGRAMS FUNCTION HERE #
def group_anagrams(strings):
    list_of_lists = []
    sub_list = []
    new_hash = False
    
    
    def create_hash(word):
        # First word
        hash = {}
        
        for char in word:
            hash[char] = True
        return hash
    
    hash = create_hash(strings[0])
    
    for word in strings:
        for char in strings:
            
            if char not in hash.keys():
                new_hash = True
                
        if new_hash:
            list_of_lists.append(sub_list)
            sub_list = [word]
            hash = create_hash(word)
        else:
            sub_list.append(word)
            
    return list_of_lists
            

# %% Tests
print("1st set:")
print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )

print("\n2nd set:")
print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]) )

print("\n3rd set:")
print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )



"""
    EXPECTED OUTPUT:
    ----------------
    1st set:
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    2nd set:
    [['abc', 'cba', 'bac'], ['foo'], ['bar']]

    3rd set:
    [['listen', 'silent'], ['triangle', 'integral'], ['garden', 'ranged']]

"""