with open ('./rosalind_dna.txt', 'r') as file:
    data = file.read()

def count_function(data):
    nu_a = 0
    nu_c = 0
    nu_g = 0
    nu_t = 0
    for element in data:
        if element == 'A':
            nu_a += 1
        if element == 'C':
            nu_c += 1
        if element == 'G':
            nu_g += 1
        if element == 'T':
            nu_t += 1
    print(nu_a, nu_c, nu_g, nu_t)

count_function(data)

# import fileinput

# for sequence in fileinput.input('./rosalind_dna.txt'):
# 	a_count = 0
# 	c_count = 0
# 	g_count = 0
# 	t_count = 0
# 	for base in sequence:
# 		if base == 'A':
# 			a_count += 1
# 		elif base == 'C':
# 			c_count += 1
# 		elif base == 'G':
# 			g_count += 1
# 		elif base == 'T':
# 			t_count += 1

# print (str(a_count) + ' ' + str(c_count) + ' ' + str(g_count) + ' ' + str(t_count))