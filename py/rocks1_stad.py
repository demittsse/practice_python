import os,glob 
Dlist=[]
Tophat="/storage3/Project/mglee/programs/tophat-2.0.14.Linux_x86_64/tophat"
maindir="/storage3/Project/mglee/2.TCGA_THF/17.STAD/"
shdir=maindir+"/11.sh_LUAD/"
logdir=maindir+"/log"
outdir=maindir+"/13.result"
os.system("mkdir %s"%maindir); os.system("mkdir %s %s %s"%(shdir, logdir, outdir))
option="--fusion-search --keep-fasta-order --bowtie1 --no-coverage-search -r 0 --mate-std-dev 80 --max-intron-length 50000 --fusion-min-dist 100000 --fusion-anchor-length 20 --fusion-ignore-chromosomes chrM"
refdir="/storage3/Project/mglee/Bt1index"
ncore=10
inputdir="/storage3/Project/dbGap/TCGA/STAD/ln_fasta_1/"
inf=glob.glob("/storage3/Project/dbGap/TCGA/STAD/ln_fasta_1/*_1.fastq")
result=glob.glob(outdir+"/tophat_*/fusions.out")
for done in result:
	df=done.split("/")[7].split("tophat_")[1]
	Dlist.append(df)
	
# wwn=0;stop=3have to run

l=0 ; wwn=29 ;stop=32
for line in inf: 
	l+=1
	if l <=wwn : continue
	if l > stop  : continue 
	sampleid= line.split("/")[7].split("_1.fastq")[0]
	if sampleid in Dlist: continue
	print sampleid
	out="%s/%s.sh"%(shdir,sampleid)
	os.system("echo \#! \/bin\/bash  > %s"%(out))
	#os.system("echo \#$ -q dellr815.q@dellr815-0-2 >> %s"%(out))
	os.system("echo \#$ -q multi.q@multi-0-3 >> %s"%(out))
	##dellr815.q@dellr815-0-0 
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
