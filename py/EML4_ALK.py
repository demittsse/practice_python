import os, glob, pysam

gtfPath="/storage/home/mglee/LAML_fish/map_fusion/hg19.gtf" ## 1. write gtf path
nibPath="/storage/home/mglee/LAML_fish/map_fusion/" ## 2. write nibfrag path
chrFaPath="/storage/home/mglee/LAML_fish/map_fusion/" ## 2. put chr.fa path
HNMID="NM_001145076" ## 3. put Head NMID
TNMID="NM_004304" ## 4. put Tail NMID
HGname="EML4" ## 5. put Head Gene name
TGname="ALK" ## 6. put Tail Gene name
FGname=HGname+"_"+TGname
H1exonNum=13 ; T1exonNum=20 ## 7. put Exon start Number
H2exonNum=H1exonNum+1; T2exonNum=T1exonNum+1 
genedir="/storage/home/mglee/LAML_fish/map_fusion/3.%s/"%(FGname)
Fadir="/storage/home/mglee/LAML_fish/map_fusion/3.%s/Fa/"%(FGname)
fusout="%s/%s_%s_merge.fa"%(Fadir,HGname,TGname)
#os.system("mkdir %s"%genedir)
#os.system("mkdir %s"%Fadir)
Hgtf=[];Tgtf=[]
gtf=open(gtfPath)
Hstart_codon="";Hstop_codon="";Tstart_codon="";Tstop_codon="";
Hchr="";Tchr=""
for line in gtf:
	if HNMID in line:
		if "exon" in line:
			llsp1=line.split("\t")[3]; rlsp1=line.split("\t")[4] ; joinlsp1=str(int(llsp1)+1)+" "+str(int(rlsp1)+1)
			Hgtf.append(joinlsp1)
			Hchr=line.split("\t")[0] ;
		if "start_codon" in line: Hstart_codon=line.split("\t")[3]
		if "stop_codon" in line: Hstop_codon=line.split("\t")[3]
	
	if TNMID in line:
		if "exon" in line:
			llsp2=line.split("\t")[3]; rlsp2=line.split("\t")[4] ;  joinlsp2=str(int(llsp2)+1)+" "+str(int(rlsp2)+1)
			Tgtf.append(joinlsp2)
			Tchr=line.split("\t")[0]
		if "start_codon" in line: Tstart_codon=line.split("\t")[3]
		if "stop_codon" in line: Tstop_codon=line.split("\t")[3]
	

if int(Hstart_codon)> int(Hstop_codon):
	Hgtf=sorted(Hgtf, reverse=True)
	print "Head reverse"
else : Hgtf=sorted(Hgtf)

if int(Tstart_codon)> int(Tstop_codon):
	Tgtf=sorted(Tgtf, reverse=True)
	print "Tail reverse"
else : Tgtf=sorted(Tgtf)



head1fa="%s/%s_exon%s.fa"%(Fadir,HGname,str(H1exonNum))
head2fa="%s/%s_exon%s.fa"%(Fadir,HGname,str(H2exonNum))
tail1fa="%s/%s_exon%s.fa"%(Fadir,TGname,str(T1exonNum))
tail2fa="%s/%s_exon%s.fa"%(Fadir,TGname,str(T2exonNum))

os.system("%s./nibFrag -upper -name=%s_exon%s %s/%s.fa.nib %s + %s" %(nibPath, HGname, str(H1exonNum), chrFaPath, Hchr, Hgtf[H1exonNum-1],head1fa))
os.system("%s./nibFrag -upper -name=%s_exon%s %s/%s.fa.nib %s + %s" %(nibPath, HGname, str(H2exonNum), chrFaPath,Hchr, Hgtf[H2exonNum-1],head2fa))



os.system("%s./nibFrag -upper -name=%s_exon%s %s/%s.fa.nib %s + %s" %(nibPath, TGname, str(T1exonNum), chrFaPath, Tchr,Tgtf[T1exonNum-1],tail1fa))
os.system("%s./nibFrag -upper -name=%s_exon%s %s/%s.fa.nib %s + %s" %(nibPath, TGname, str(T2exonNum), chrFaPath, Tchr, Tgtf[T2exonNum-1],tail2fa))




## input ##
head1=open(head1fa); head2=open(head2fa); tail1=open(tail1fa); tail2=open(tail2fa)

## output ##




totalfa=[]
#headfa1=[]; headfa2=[]; tailfa1=[]; tailfa2=[]
#headfa1=""; headfa2=""; tailfa1=""; tailfa2=""
#out=open("ctla4_cd28.fa","w");tailout=open("CD28_merge.fa","w")
#out.write(">CTLA4_CD28\n");tailout.write(">CD28exon4\n");


def extractFA(inf):
	out=[]
	for line in inf:
		if ">" in line:continue
		out.append(line.split("\n")[0])
	outfa="".join(out)
	return outfa


headfa1=extractFA(head1); headfa2=extractFA(head2)
tailfa1=extractFA(tail1); tailfa2=extractFA(tail2)



if len(headfa1+headfa2)>500:
	headfa1=headfa1[len(headfa1)-200:len(headfa1)]
	headfa2=headfa2[0:200]

if len(tailfa1+tailfa2)>500:
	tailfa1=tailfa1[len(tailfa1)-200:len(tailfa1)]
	tailfa2=tailfa2[0:200]

totalfa=headfa1+tailfa2; headfa=headfa1+headfa2; tailfa=tailfa1+tailfa2
print totalfa
def JoinWrite(fastr,ouf,Gene):
	ouf.write(">"+Gene+"\n")
	ouf.write(fastr)
	ouf.write("\n")


############################# Write Fusion seq to file   ####################################

#os.system("rm %s"%fusout)
#fusouf=open(fusout,"a");

#JoinWrite(headfa,fusouf,HGname)
#JoinWrite(tailfa,fusouf,TGname)
#JoinWrite(totalfa,fusouf,FGname)

############################   Make Possible fusion sequence   ###########################

import os, glob 	

#Tailfa2="TCACAGCCACTTGCAGGGGGCTTGGGTCGTTGGGCATTCCGGACACCTGGCCTTCATACACCTCCCCAAAGGCGCCATGGCCCAGACCCC"
#Headfa1="GTATATCAAATCAGCAAACAAATCAAAGCTCATGATGGCAGTGTGTTCACACTTTGTCAGATGAGAAATGGGATGTTATTAACTGGAGGAGGGAAAGACAGAAAAATAATTCTGTGGGATCATGATCTGAATCCTGAAAGAGAAATAGAGG"
#Tailfa2="AATGAGGGTGATGTTTTTCCGCGGCACCTCCTTCAGGTCACTGATGGAGGAGGTCTTGCCAGCAAAGCAGTAGTTGGGGTTGTAGTCGGTCATGATGGTCGAGGTGCGGAGCTTGCTCAGCTTGTACTCAGGGCTCTGCAGCTCCATCTGCATGGCTTGCAGCTCCTGGTGCTTCCGGCGGTACAC"

#Headfa1="AATCTCATATTTTCTTCTGGACCTGGAGCGGCAATTCACTAACAAGAAAACAGGGAATTTTTGGGAAATATGAAAAGCCAAAATTTGTGCAGTGTTTAGCATTCTTGGGGAATGGAGATGTTCTTACTGGAGACTCAGGTGGAGTCATGCTTATATGGAGCAAAACTACTGTAGAGCCCACACCTGGGAAAGGACCTAAAG"
#Tailfa2="TGTACCGCCGGAAGCACCAGGAGCTGCAAGCCATGCAGATGGAGCTGCAGAGCCCTGAGTACAAGCTGAGCAAGCTCCGCACCTCGACCATCATGACCGACTACAACCCCAACTACTGCTTTGCTGGCAAGACCTCCTCCATCAGTGACCTGAAGGAGGTGCCGCGGAAAAACATCACCCTCATTCGGGGTCTGGGCC"

#Headfa1="CACAGACAAACTCCAGAAAGCAAGAATGCTACTCCCACCAAAAGCATAAAACGACCATCACCAGCTGAAAAGTCACATAATTCTTGGGAAAATTCAGATGATAGCCGTAATAAATTGTCGAAAATACCTTCAACACCCAAATTAATACCAAAAGTTACCAAAACTGCAGACAAGCATAAAGATGTCATCATCAACCAAG"
#Tailfa2="TGTACCGCCGGAAGCACCAGGAGCTGCAAGCCATGCAGATGGAGCTGCAGAGCCCTGAGTACAAGCTGAGCAAGCTCCGCACCTCGACCATCATGACCGACTACAACCCCAACTACTGCTTTGCTGGCAAGACCTCCTCCATCAGTGACCTGAAGGAGGTGCCGCGGAAAAACATCACCCTCATTCGGGGTCTGGGCCA"

#Headfa1="GACTGGTCCCCAGACAAGTATATAATGTCTAACTCGGGAGACTATGAAATATTGTACTGTAAGTATGAATGATTAT"
#Tailfa2="GATCCTCTCTGTGGTGACCTCTGCCCTCGTGGCCGCCCTGGTCCTGGCTTTCTCCGGCATCATGATTGTGTACCGCCGGAAGCACCAGGAGCTGCAAGCCATGCAGATGGAGCTGCAGAGCCCTGAGTACAAGCTGAGCAAGCTCCGCACCTCGACCATCATGACCGACTACAACCCCAACTACTGCTTTGCTGGCATTCGTGGAGACCAGGAGCTGCAAGCCATGCAGA"
Headfa1="GTCTAACTCGGGAGACTATGAAATATTGTACTTGTACCGCCGGAAGCA"
Tailfa2="GAAATATTGTACTTGTACCGCCGGAAGCACCAGGAGCTGCAAGCCATG"
def seqseed(seed):
	SeqPo=[]
	for a in range(0,51-seed*2+1) :
		Head = 51-seed*2-a +seed
		Tail = seed +a 
		seq  = Headfa1[-(Head):] + Tailfa2[:(Tail) ]
		SeqPo.append(seq)
	return SeqPo


fileL=[]
Respath="/storage3/Project/mglee/LAML_fish/1.EML4_ALK/"
#Respath="/storage3/Project/mglee/LAML_fish/2.100LC/"
fileP=glob.glob("%s/fs/*.sorted.bam"%Respath)

for item in fileP:
	dd=item.split("/")[8].split(".sorted.bam")[0]
	fileL.append(dd)

#fileL.sort()

fw=open("EML4_Alk4fs1.txt","w")
fw.write("windowsize\t%s\n"%("\t".join(fileL)))
#(0,46)
for plus in range(0,26):
	seed = 5 + plus
	seq = Headfa1[-seed:] + Tailfa2[:seed]
	print seq
	
	SeqPo= seqseed(seed) 
	print SeqPo
	newline = [str(len(seq))]
	for file in fileP: 
		count= os.popen("samtools view %s | grep %s | cut -f 10 "  %(file, seq))
		reads = count.read().split("\n")
		readcount = 0 
		for read in reads:
			if read in SeqPo : 
				readcount+=1
		newline.append(str(readcount))
	print newline
	fw.write("\t".join(newline))
	fw.write("\n") 

