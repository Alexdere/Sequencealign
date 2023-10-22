#import blosum as bl
import random
import blosum
import matplotlib.pyplot as plt


aalist=['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S',
'T', 'W', 'Y', 'V']
time = []
n=0
def flatten(blosum_dict):

    nested_dict =  blosum_dict
    flat_dict = {}

    for aa1, inner_dict in nested_dict.items():
        for aa2, score in inner_dict.items():
            flat_dict[(aa1, aa2)] = score
    return flat_dict

    #print(flat_dict)
generator = [random.choice(aalist) for i in range(50)]
seq1 = generator.copy()
seq2 = generator.copy()
end1 = ''.join(seq1)
end2 = ''.join(seq2)

blosum45 = flatten(blosum.BLOSUM(45))
blosum62 = flatten(blosum.BLOSUM(62))
blosum90 = flatten(blosum.BLOSUM(90))
#print(blosum)
#print(blosum90["A"],["A"])
scores45 = []
scores62 = []
scores90 = []
#calculate blosum scores:

def scores(seq1,seq2,blosum_matrix):
    score = 0
    scorelist=[]
    
    for i in range(0,len(seq1)):
         score +=blosum_matrix[(seq1[i],seq2[i])]
         scorelist.append(score)
    return scorelist



for t in range(100):
    time.append(t)
    seq1[random.randint(0,len(seq1)-1)] = aalist[random.randint(0,len(aalist)-1)]
    seq2[random.randint(0,len(seq1)-1)] = aalist[random.randint(0,len(aalist)-1)]

    scores45.append(scores(seq1,seq2,blosum45)[-1])
    scores62.append(scores(seq1,seq2,blosum62)[-1])
    scores90.append(scores(seq1,seq2,blosum90)[-1])

    #print(seq1,seq2)
end1_1 = ''.join(seq1)
end2_2 = ''.join(seq2)


#plt.plot(time,scores45,"g", time, scores62, 'b', time, scores90, 'r' )
#plt.show()
import matplotlib.pyplot as plt

def annotate_colored(ax, text, comparison_text, y, x_start=0):
    x_offset = x_start
    for char1, char2 in zip(text, comparison_text):
        color = 'g' if char1 == char2 else 'r'
        ax.annotate(char1, xy=(x_offset, y), xycoords='figure fraction', xytext=(5, -5), textcoords='offset points', ha='left', va='top', color=color, fontsize = 7)
        x_offset += 0.015  # adjust this value depending on your specific requirements



#plt.figure()
# Your existing plot code here...

# Annotate the starting sequences
plt.annotate(f'Starting sequence1: ', xy=(0, 1), xycoords='figure fraction', xytext=(5, -4), textcoords='offset points', ha='left', va='top', fontsize=9)
annotate_colored(plt.gca(), end1, end1, 1, x_start=0.2)

plt.annotate(f'Starting sequence2: ', xy=(0, 0.975), xycoords='figure fraction', xytext=(5, -5), textcoords='offset points', ha='left', va='top', fontsize=9)
annotate_colored(plt.gca(), end2, end2, 0.975, x_start=0.2)

# Annotate the ending sequences
plt.annotate(f'Ending sequence1:   ', xy=(0, 0.95), xycoords='figure fraction', xytext=(5, -5), textcoords='offset points', ha='left', va='top', fontsize=9)
annotate_colored(plt.gca(), end1_1, end2_2, 0.95, x_start=0.2)

plt.annotate(f'Ending sequence2:   ', xy=(0, 0.925), xycoords='figure fraction', xytext=(5, -5), textcoords='offset points', ha='left', va='top', fontsize=9)
annotate_colored(plt.gca(), end2_2, end1_1, 0.925, x_start=0.2)





plt.plot(time, scores45, label='BLOSUM45')
plt.plot(time, scores62, label='BLOSUM62')
plt.plot(time, scores90, label='BLOSUM90')
plt.xlabel('Time Steps')
plt.ylabel('Alignment Score')
# Annotate starting and ending sequences
plt.legend()
plt.show()
#plt.savefig("allignment3.png")
#plt.close()



