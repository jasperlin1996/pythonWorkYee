triangle = [(a,b,c) for a in range(1,101) for b in range(a,101) for c in range (b,101) if a ** 2 + b ** 2 == c ** 2]
import itertools

dic = { frozenset(key):0 for i in range(1,len(['A','B','C','D','E','F'])+1) for key in itertools.combinations(['A','B','C','D','E','F'], i) }
print(dic)