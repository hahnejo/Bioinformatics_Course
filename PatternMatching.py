def PatternMatching(Pattern, Genome):
    k = len(Pattern)
    pos = []
    for i in range(len(Genome)):
        if Genome[i:i+k] == Pattern:
            pos.append(i)
    return pos

def PatternMatching2(Pattern, Genome):
    pos = [i for i in range(len(Genome)) if Genome[i:i+len(Pattern)] == Pattern]
    return pos

print(PatternMatching("CT", "ATATCTCTATAT"))
print(PatternMatching2("CT", "ATATCTCTATAT"))