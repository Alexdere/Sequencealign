filepath = r"C:\Users\vetle\OneDrive - University of Bergen\mol103,204,210\Rapport\CLUSTAL _multiple sequence_blast1.txt"
import re
pattern = re.compile(r'^[A-Z0-9]{4}_[A-Z0-9]')
row = 0
raw = []

with open(filepath, "r", encoding="utf-8") as f:
    for line in f:
        if pattern.match(line):
            row +=1
            raw.append(line.strip())
            print(line.strip())

n = 0
block = []
columns = []
# now u have isolated the rows, now u need to prune the rows to get onlu seq align
for i in raw:
    i = i.split()
    block.append(i[1])
    n = n+1
    if n == 10:
        columns.append(block)
        n = 0
        block = []
    
c = 0
for i in columns: 
    transposed = zip(*i)
    for j in transposed:
        if len(set(j)) == 1:
            c += 1

print(c)        
    
