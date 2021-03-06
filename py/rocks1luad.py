
import os,glob 
inf1=glob.glob("/storage3/Project/mglee/2.TCGA_THF/10.LUAD/13.result/tophat_*")
inf2=glob.glob("/storage/home/mglee/Tophat/02.LUAD/result_LUAD/tophat_*")
inf3=glob.glob("/storage/Project/dbGap/TCGA/LUAD/ln_fasta_real/*_1.fastq")
total=[];st1=[];st3=[]

for a in range(0,len(inf1)):
	rowa=inf1[a].split("tophat_")[1]
	st3.append(rowa)

for b in range(0,len(inf2)):
	rowb=inf2[b].split("tophat_")[1]+"_1"
	st1.append(rowb)

for c in range(0,len(inf3)):
	rowc=inf3[c].split("ln_fasta_real/")[1].split("_1.fastq")[0]
	total.append(rowc)


Dlist=[]
Tophat="/storage3/Project/mglee/programs/tophat-2.0.14.Linux_x86_64/tophat"
maindir="/storage3/Project/mglee/2.TCGA_THF/10.LUAD"
shdir=maindir+"/11.sh_LUAD/"
logdir=maindir+"/log"
outdir=maindir+"/13.result"
option="--fusion-search --keep-fasta-order --bowtie1 --no-coverage-search -r 0 --mate-std-dev 80 --max-intron-length 100000 --fusion-min-dist 100000 --fusion-anchor-length 20 --fusion-ignore-chromosomes chrM"
refdir="/storage3/Project/mglee/Bt1index"
ncore=10
inputdir="/storage/Project/dbGap/TCGA/LUAD/ln_fasta_real/"
inf=list(set(total)-set(st1)-set(st3))
result=glob.glob(outdir+"/tophat_*/fusions.out")


l=0 ; wwn=0 ;stop=10
for line in inf: 
	l+=1
	if l <=wwn : continue
	if l > stop  : continue 
	sampleid= line.replace("\n","")
	print sampleid
	out="%s/%s.sh"%(shdir,sampleid)
	os.system("echo \#! \/bin\/bash  > %s"%(out))
	os.system("echo \#$ -q dellr815.q@dellr815-0-2 >> %s"%(out))
	##dellr815.q@dellr815-0-0 multi.q@multi-0-3
	os.system("echo \#$ -S \/bin\/bash  >> %s"%(out))
	os.system("echo \#$ -j y  >> %s"%(out))
	os.system("echo \#$ -N %s >> %s"%(sampleid,out))
	os.system("echo \#$ -e %s >> %s"%(logdir,out))
	os.system("echo \#$ -o %s >> %s"%(logdir,out))
	os.system('''echo %s -o %s/tophat_%s -p %s %s %s/hg19 %s/%s_1.fastq %s/%s_2.fastq >> %s'''%(Tophat,outdir,sampleid,ncore,option,refdir,inputdir,sampleid,inputdir,sampleid,out))
	#os.system("echo cd %s"%outdir)
	#os.system("echo /storage3/Project/mglee/programs/tophat-2.0.14.Linux_x86_64/tophat-fusion-post -p 2 --num-fusion-reads 1 --num-fusion-pairs 2 --num-fusion-both 5 /storage3/Project/mglee/Bt1index/hg19")
	os.system("chmod 755 %s"%out)
	os.system("cd %s"%shdir)
	os.system("qsub -pe mpich %s %s"%(ncore,out)) 
