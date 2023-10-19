# %% Func
def first_non_repeating_char(string):
    hash = {}
    
    for char in string:
        if char in hash.keys() and hash[char] == False:
            hash[char] = True
                
        else:
            hash[char] = False
    
    for char in string:
        if hash[char] == False:
            return char
    
    return None

# %% Test
print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbcc') )



"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""
# %%
