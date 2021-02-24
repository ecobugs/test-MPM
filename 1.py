import difflib

def closeMatches(patterns, words):
    values = []
    for pattern in patterns:
        value = ''
        value = difflib.get_close_matches(pattern,words)
        print value
        if value[len(value)-1] == pattern:
            values.insert(len(values),value[len(value)-1])
        else:
            values.insert(len(values),pattern)
            values.insert(len(values),value[len(value)-1])
            
    return values

patterns = ['hit', 'dog']
words = ["hot", "dot", "dog", "lot", "log"]
print closeMatches(patterns, words)

