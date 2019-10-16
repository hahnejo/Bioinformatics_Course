import operator

def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n - k + 1):
        Pattern = Text[i:i+k]
        if Pattern in freq:
            freq[Pattern] += 1
        else:
            freq[Pattern] = 1
    return (freq)
    # return (max(freq.iteritems(), key=operator.itemgetter(1))[0])

print(FrequencyMap("CGATATATCCATAG", 3))
print(FrequencyMap("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4))