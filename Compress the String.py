from itertools import groupby
S = input()
compressed = [(len(list(g)), int(k)) for k, g in groupby(S)]
print(' '.join(str(item) for item in compressed))
