def word_break(s, dictionary):    
    def _word_break(offset):
        if offset == len(s):
            return []

        breaks_from_offset = []
        if s[offset:] in dictionary:
            breaks_from_offset.append([s[offset:]])

        for i in range(offset+1, len(s)):
            if s[offset:i] in dictionary:
                for break_from_i in _word_break(i):
                    breaks_from_offset.append([s[offset:i]] + break_from_i)

        return breaks_from_offset

    return [' '.join(words) for words in _word_break(0)]

print word_break('programmerit',{'pro', 'gram', 'merit', 'program', 'it', 'programmer'})
