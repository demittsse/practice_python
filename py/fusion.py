External Ids for RUNX1T1 Gene
HGNC: 1535 Entrez Gene: 862 Ensembl: ENSG00000079102 OMIM: 133435 UniProtKB: Q06455
External Ids for RUNX1 Gene
HGNC: 10471 Entrez Gene: 861 Ensembl: ENSG00000159216 OMIM: 151385 UniProtKB: Q01196

nibFrag -upper -name=exon1  chr21.nib 93088194	 	93088365  + RUNX1T1exon1.fa  
nibFrag -upper -name=exon2  chr21.nib 93029455		 93029592 + RUNX1T1exon2.fa  
nibFrag -upper -name=exon3  chr21.nib 93026808	 	93027049 + RUNX1T1exon3.fa  
nibFrag -upper -name=exon7  chr8.nib 36206708	 36206899 + RUNX1exon7.fa  
grep NM_001243077 hg19.gtf > CD28.gtf
grep ../NM_005214 hg19.gtf > ctla4_cd28/CTLA4.gtf
 2051  grep NM_006139 hg19.gtf > ctla4_cd28/CD28.gtf
 
ercsb@ercsb-B85M-D3H:~/Desktop/work/mapFusion/ctla4_cd28$ more CD28.gtf
chr2	hg19_refGene	start_codon	204571420	204571422	0.000000	+	.	gene_id "NM_001243077"; transcript_id "NM_001243077"; 
chr2	hg19_refGene	CDS	204571420	204571471	0.000000	+	0	gene_id "NM_001243077"; transcript_id "NM_001243077"; 
chr2	hg19_refGene	exon	204571198	204571471	0.000000	+	.	gene_id "NM_001243077"; transcript_id "NM_001243077"; 
chr2	hg19_refGene	CDS	204591356	204591421	0.000000	+	2	gene_id "NM_001243077"; transcript_id "NM_001243077"; 
chr2	hg19_refGene	exon	204591356	204591421	0.000000	+	.	gene_id "NM_001243077"; transcript_id "NM_001243077"; 
chr2	hg19_refGene	CDS	204594371	204594495	0.000000	+	2	gene_id "NM_001243077"; transcript_id "NM_001243077"; 
chr2	hg19_refGene	exon	204594371	204594495	0.000000	+	.	gene_id "NM_001243077"; transcript_id "NM_001243077"; 
chr2	hg19_refGene	CDS	204599507	204599632	0.000000	+	0	gene_id "NM_001243077"; transcript_id "NM_001243077"; 
chr2	hg19_refGene	stop_codon	204599633	204599635	0.000000	+	.	gene_id "NM_001243077"; transcript_id "NM_001243077"; 
chr2	hg19_refGene	exon	204599507	204603636	0.000000	+	.	gene_id "NM_001243077"; transcript_id "NM_001243077";

 2072  .././nibFrag -upper -name=CD28_exon4  ../chr2.nib 204599507 204603636 + CD28_exon4.fa
 2073  .././nibFrag -upper -name=CTLA4_exon3  ../chr2.nib 204736100 20473629 + CTLA4_exon3.fa
.././nibFrag -upper -name=CD28_exon1  ../chr2.nib 204571197	 204571470 + CD28_exon1.fa
.././nibFrag -upper -name=CD28_exon2  ../chr2.nib 204591355	 204591420 + CD28_exon2.fa
.././nibFrag -upper -name=CD28_exon3  ../chr2.nib 204599506  	204599631 + CD28_exon3.fa
.././nibFrag -upper -name=CD28_exon3  ../chr2.nib 204571419   	204571470 + CD28_exon.fa
.././nibFrag -upper -name=CD28_exon4  ../chr2.nib 204594370 204599634 + CD28_exon4.fa
.././nibFrag -upper -name=CD28_exon4  ../chr2.nib 204594370  204594494 + CD28_exon4.fa
.././nibFrag -upper -name=CD28_cds  ../chr2.nib 204599506  204599634 + CD28_cds.fa

 2050  grep NM_005214 hg19.gtf > ctla4_cd28/CTLA4.gtf
 2051  grep NM_006139 hg19.gtf > ctla4_cd28/CD28.gtf
 2052  faToNib chr2.fa chr2.nib
 2054  ./faToNib chr2.fa chr2.nib
 


"nibFrag -upper -name=exon%s  chr%s.nib %s %s  + %sexon%s.fa"%(Hexon1,Hchr,Hexon1Start,Hexon1End,Hgname,Hexon1)
"nibFrag -upper -name=exon%s  chr%s.nib %s %s  + %sexon%s.fa"%(Hexon2,Hchr,Hexon2Start,Hexon2End,Hgname,Hexon2)
"nibFrag -upper -name=exon%s  chr%s.nib %s %s  + %sexon%s.fa"%(Hexon3,Hchr,Hexon3Start,Hexon3End,Hgname,Hexon3)
"nibFrag -upper -name=exon%s  chr%s.nib %s %s  + %sexon%s.fa"%(Hexon4,Hchr,Hexon4Start,Hexon4End,Hgname,Hexon4)


diff -u /storage/home/sangok/Lymphoma/FusionTranscript/CD28.fa /home/ercsb/Desktop/work/mapFusion/ctla4_cd28/CD28_exon4.fa
diff /storage/home/sangok/Lymphoma/FusionTranscript/CTLA4.fa /home/ercsb/Desktop/work/mapFusion/ctla4_cd28/CTLA4_exon3.fa
diff /storage/home/sangok/Lymphoma/FusionTranscript/CD28.fa /home/ercsb/Desktop/work/mapFusion/ctla4_cd28/ctla4_cd28.fa
diff -u /storage/home/sangok/Lymphoma/FusionTranscript/CD28.fa /home/ercsb/Desktop/work/mapFusion/ctla4_cd28/CD28_merge.fa


	
head=open("CTLA4_exon3.fa");tail=open("CD28_exon4.fa")
tail2=open("CD28_cds.fa")
totalfa=[];tailfa=[]
out=open("ctla4_cd28.fa","w");tailout=open("CD28_merge.fa","w")
out.write(">CTLA4_CD28\n");tailout.write(">CD28exon4\n");

for line in head:
	if ">" in line:continue
	totalfa.append(line.split("\n")[0])

for item in tail:
	if ">" in item : continue
	totalfa.append(item.split("\n")[0])
	tailfa.append(item.split("\n")[0])

for t2 in tail2:
	if ">" in t2:continue
	tailfa.append(t2.split("\n")[0])


onefa="".join(totalfa)
tailmerge="".join(tailfa)
def split_by_n( seq, n ):
	while seq:
		yield seq[:n]
		seq = seq[n:]

#list2write=list(split_by_n(onefa,50))
#WLine="\n".join(list2write)
out.write(onefa)
tailout.write(tailmerge)


#################################
import os
shdir="/storage/home/mglee/nib"
for a in range(1,22):
	out="%s/%s.sh"%("/storage/home/mglee/nib",str(a))
	os.system("echo \#! \/bin\/bash  > %s"%(out))
	os.system("echo \#$ -q inode24.q@inode24-0-1 >>%s"%out)
	os.system("echo \#$ -S \/bin\/bash  >> %s"%(out))
	os.system("echo \#$ -j y  >> %s"%(out))
	os.system("echo \#$ -N chr%s >> %s"%(str(a),out))
	os.system("echo \#$ -e %s >> %s"%("/storage/home/mglee/nib",out))
	os.system("echo \#$ -o %s >> %s"%("/storage/home/mglee/nib",out))
	os.system('''echo wget ftp://hgdownload.cse.ucsc.edu/goldenPath/hg19/chromosomes/chr%s.fa.gz >> %s''')%(str(a),out)
	os.system("chmod 755 %s"%out)
	os.system("cd %s"%shdir)
	os.system("qsub -pe mpich %s %s"%(ncore,out)) 


import pysam
tabixfile = pysam.TabixFile("example.gtf.gz")

for gtf in tabixfile.fetch("chr1", 1000, 2000):
    print (gtf.contig, gtf.start, gtf.end, gtf.gene_id)
    
    
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import os, glob

fileL=glob.glob("*.bam")
fileL.sort()

cd284='GTGAGGAGTAAGAGGAGCAGGCTCCTGCACAGTGACTACATGAACATGACTCCCCGCCGCCCCGGGCCCACCCGCAAGCATTACCAGCCCTATGCCCCACCACGCGACTTCGCAGCCTATCGCTCCTGA'
ctla3='ATCCAGAACCGTGCCCAGATTCTGACTTCCTCCTCTGGATCCTTGCAGCAGTTAGTTCGGGGTTGTTTTTTTATAGCTTTCTCCTCACAGCTGTTTCTTTGAGCAAAATG'
ctla4='CTAAAGAAAAGAAGCCCTCTTACAACAGGGGTCTATGTGAAAATGCCCCCAACAGAGCCAGAATGTGAAAAGCAATTTCAGCCTTATTTTATTCCCATCAATTGA'
cd283='GGAAACACCTTTGTCCAAGTCCCCTATTTCCCGGACCTTCTAAGCCCTTTTGGGTGCTGGTGGTGGTTGGTGGAGTCCTGGCTTGCTATAGCTTGCTAGTAACAGTGGCCTTTATTATTTTCTGG'
fw=open("fusion.txt","w")

fw.write("windowsize\t%s\n"%("\t".join(fileL).replace("_vf.bam","")))

def seqseed(seed):
 SeqPo=[]
 for a in range(0,101-seed*2+1) :
  Head = 101-seed*2-a +seed
  Tail = seed +a
  seq  = ctla3[-(Head):] + cd284[:(Tail) ]
  SeqPo.append(seq)
 return SeqPo


for plus in range(0,46):
 seed = 5 + plus
 seq = ctla3[-seed:] + cd284[:seed ]
 SeqPo= seqseed(seed)
 newline = [str(len(seq))]
 for file in fileL: 
   count= os.popen("samtools view %s | grep %s | grep 101M | cut -f 10 "  %(file, seq))
   reads = count.read().split("\n")
   readcount = 0
   for read in reads:
      if read in SeqPo : readcount+=1
   newline.append(str(readcount))
 print newline
 fw.write("\t".join(newline))
 fw.write("\n")

fw.close()
