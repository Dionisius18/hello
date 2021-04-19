#doc = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
#for a in doc :
#    tokens = a.split()
#    normalized = [token.rstrip('.,').lower() for token in tokens]
#    print(normalized)

#doc = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
#for a in doc :
#    words = a.split()
#    for word in words :
#        word.strip('.,')
#        word.lower()
#    print(words)

def word_search(doc_list, keyword):
    """
    Takes a list of doc_list (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all doc_list 
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    pass
    list_1 = []
    for i, doc in enumerate(doc_list) :
        words = doc.split()
        for word in words :
            word.strip('.,')
            word.lower()
        if keyword.lower() in words :
            list_1.append(i)
    return list_1

doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
word_search(doc_list, 'casino')

def word_research(doc_list, keyword):
    # list to hold the indices of matching doc_list
    indices = [] 
    # Iterate through the indices (i) and elements (doc) of doc_list
    for i, doc in enumerate(doc_list):
        # Split the string doc into a list of words (according to whitespace)
        tokens = doc.split()
        
        # Make a transformed list where we 'normalize' each word to facilitate matching.
        # Periods and commas are removed from the end of each word, and it's set to all lowercase.
        normalized = [token.rstrip('.,').lower() for token in tokens]
        # Is there a match? If so, update the list of matching indices.
        if keyword.lower() in normalized:
            indices.append(i)
    return indices

doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
word_research(doc_list, 'casino')