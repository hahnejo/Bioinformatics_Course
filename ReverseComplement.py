def ReverseComplement(Pattern):
    rev_pattern = Pattern[::-1]
    comp = ''
    for letter in rev_pattern:
        if letter == 'C':
            comp += 'G'
        elif letter == 'G':
            comp += 'C'
        elif letter == 'A':
            comp += 'T'
        else:
            comp += 'A'
    return comp

print(ReverseComplement("ATTTTAC"))