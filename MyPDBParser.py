# lag et program som henter informasjon fra en PDB fil, output skal skal presenteres osm under
# PDB_ID:1E3L
#Number of a-helices:33
#Number of b-strands:36
#Number of b-sheets:12
#Helix1:8
#Helix2:6
#..
#Helix33:11
#Strands_Sheet1:2
#Strands_Sheet2:3
#..
#Strands_Sheet12:6

import sys

filename = "6cq6.pdb"
#filename = "1uok.pdb"
#file = open(filename, 'r')

def helix_sheet(filename):
    helix_length = []
    sheet_strands = []
    n = 0
    m = 0
    j = 0
    k = 0
    s = 0
    file = open(filename, 'r')
    #helixdict = {} #dictionary for helix number and length
    
   
    for line in file:
        
        
        if "HEADER" in line:
            header_info = line.split()
            print("PDB_ID:", header_info[-1])
            
            
        
    file.seek(0)
    previous = [] 
    for line in file:
        if "HELIX" in line:
            j += 1
        if "SHEET" in line:
            k += 1
            
            sheetinfo = line.split()
            if sheetinfo[3] not in previous:
                s += 1
            previous.clear()
            previous.append(sheetinfo[3])


        
        
    print("Number of a-helices:", j)
    print("Number of b-strands:", k)
    print("Number of b-sheets:", s)

    file.seek(0)
    for line in file:   
        if "HELIX" in line:
            helix_info = line.split()
            keys = "Helix" + str(n+1)+":"
            values = helix_info[-1]
            n+=1
            #helixdict[keys] = values
            helix_length.append((keys,values))
            print(keys, values)
    
    file.seek(0)
    duplicate_values = set()
    duplicate_statement = set()
    sheets = [] 
    x = 0
    for line in file:
        if "SHEET" in line:
            sheet_info = line.split()
            keys_2 = "Strands_Sheet" + str(m+1) + ":"
            values_2 = sheet_info[3]
            n += 1
            #m += 1
            x = 1
            sheets.append("SHEET")
            sheet_strands.append((keys_2,values_2))
            if values_2 not in duplicate_values:
                print(keys_2, values_2)
                duplicate_values.add(values_2)
                m += 1
   
    for i in sheets:
        if i == "SHEET":
           x = 1
           break
    if x == 0:
        print("No sheets or strands found in this PDB file")
      
    #print(helix_length)
    #print(sheet_strands)
    return helix_length, sheet_strands  
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,6))

x = [i[0] for i in helix_sheet(filename)[0]]
y = [int(i[1]) for i in helix_sheet(filename)[0]]

x2 = [i[0] for i in helix_sheet(filename)[1]]
y2 = [int(i[1]) for i in helix_sheet(filename)[1]]

ax1.hist(y, bins=range(min(y), max(y)+2), rwidth=0.8, color = "#6C4B9B")
ax1.yaxis.set_major_locator(MaxNLocator(integer=True))
ax1.set_xticks(range(min(y), max(y) + 1))
ax1.set_title('Distribution of Helix Lengths')
ax1.set_xlabel('Helix lenght:')
ax1.set_ylabel('Frequency')
if len(ax1.get_xticklabels()) > 15:
    plt.setp(ax1.get_xticklabels(), rotation=45,fontsize = 6, ha="right")


ax2.bar(x2, y2, width=0.8, color = "#2C5D8C")
ax2.yaxis.set_major_locator(MaxNLocator(integer=True))
ax2.set_title('Strands per Sheet')
ax2.set_ylabel('Number of Strands')
ax2.set_xticklabels(x2, rotation=45, ha="right")  # Rotate the x-ticks for better readability


plt.tight_layout()
plt.show()




if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 MyPDBParser.py <name of PDB file>")
    else:
        pdb_filename = sys.argv[1]
        helix_sheet(pdb_filename)