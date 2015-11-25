#/storage3/Project/mglee/TCGA_SOAP/10.LUAD/13.result_LUAD/UNCID_2176630/junction_seq/LUAD/junction/LUAD.D1.junction.fa

#ercsb@ercsb-B85M-D3H:/storage3/Project/mglee/TCGA_SOAP/10.LUAD/13.result_LUAD/UNCID_2176630/junction_seq/LUAD/junction$ grep EML4 LUAD.D1.junction.fa.info.case.num
# 11550 EML4/ALK  6478030>EML4_ALK 6489581
#GACTGGTCCCCAGACAAGTATATAATGTCTAACTCGGGAGACTATGAAATATTGTACTGTAAGTATGAATGATTAT GATCCTCTCTGTGGTGACCTCTGCCCTCGTGGCCGCCCTGGTCCTGGCTTTCTCCGGCATCATGATTGTGTACCGCCGGAAGCACCAGGAGCTGCAAGCCATGCAGATGGAGCTGCAGAGCCCTGAGTACAAGCTGAGCAAGCTCCGCACCTCGACCATCATGACCGACTACAACCCCAACTACTGCTTTGCTGGCATTCGTGGAGACCAGGAGCTGCAAGCCATGCAGA
inf=open("/home/ercsb/work/transcript/EML4_ALK/pos.fa")
#ouf=open("/home/ercsb/work/transcript/EML4_ALK/EML4_ALK.fa","w")
ouf2=open("/home/ercsb/work/transcript/EML4_ALK/tail.fa","w")
linenum=0
x=[];Head=[];Tail=[];SpTail=[]
for line in inf:
	linenum+=1
	#if linenum == 6489581 : print line
	if linenum == 6478031 : 
		Head.append(line[0:47])
		tailsp=line[48:].split("\n")[0]
		Tail.append(tailsp)

	if linenum > 6478031 and linenum <6489581:
		splitRH=line[0:47]
		splitRT=line[48:].split("\n")[0]
		if splitRH not in Head:
			Head.append(splitRH)
		if splitRT not in Tail:
			Tail.append(splitRT)
		#Tail.append(line.split("\n")[0][-1:])
	if ">EML6/ECE1" in line: break

#ConTail= "".join(Tail)
#for HH in Head:
#	print HH
for TT in Tail:
	SpTail.append(TT[-1:])
print "".join(SpTail)
#ouf.write(">EML4_ALK\n")

#ouf.write("".join(x))
#for item in x:
#	print item
"""
def solution(x):
    from itertools import permutations
    for perm in permutations(x):
        linked = [perm[i][:-5] for i in range(len(perm)-1) 
                               if perm[i][-5:]==perm[i+1][:5]]
        if len(perm)-1==len(linked):
            return "".join(linked)+perm[-1]
    return None


print solution(x)
"""
