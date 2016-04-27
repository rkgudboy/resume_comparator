import sys

def get_chunk(f, size):
    chunk = set()
    buf = f.read()
    for i in range(0, len(buf)-size+1):
        yield buf[i:i+size]

def jaccard(set1, set2):
    x = len(set1.intersection(set2))
    y = len(set1.union(set2))
    return x / float(y)

cur_jaccard_val = 0
input_1 = sys.argv[1]
input_2 = sys.argv[2]
with open(input_1) as f1, open(input_2) as f2:
    chunk1 = set(get_chunk(f1, size=5))
    chunk2 = set(get_chunk(f2, size=5))
print(jaccard(chunk1, chunk2), input_1, input_2)
