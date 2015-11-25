import os,glob 

Tophat="/storage/home/mglee/source/THF/tophat-2.0.14.Linux_x86_64/tophat"
maindir="/storage/home/mglee/Tophat_TCGA/14.CHOL/"
shdir=maindir+"/11.sh_CHOL/"
logdir=maindir+"/log/"
outdir=maindir+"/13.result/"
os.system("mkdir %s"%maindir); os.system("mkdir %s %s %s"%(shdir, logdir, outdir))
option="--fusion-search --keep-fasta-order --bowtie1 --no-coverage-search -r 0 --mate-std-dev 80 --max-intron-length 100000 --fusion-min-dist 20000 --fusion-anchor-length 20 --fusion-ignore-chromosomes chrM"
refdir="/storage/home/mglee/source/THF/tophat_ref"
ncore=8
inputdir="/storage/home/mglee/Raw_TCGA/CHOL/ln_CHOL/"
#Your job 10795 ("TCGA-W5-AA2G-01A") has been submitted
inf=glob.glob("%sTCGA*_1.fastq"%inputdir)
l=0 ; wwn=60 ;stop=80
for line in inf: 
	l+=1
	if l <=wwn : continue
	if l > stop  : continue 
	sampleid= line.split("/")[7].split("_1.fastq")[0]	
	print sampleid
	out="%s/T_%s.sh"%(shdir,"".join(sampleid.split("-")[1:3]))
	os.system("echo \#! \/bin\/bash  > %s"%(out))
	os.system("echo \#$ -q anode64.q@anode64-0-4 >> %s"%(out))
	#os.system("echo \#$ -q inode24.q@inode24-0-1>> %s"%(out))
	os.system("echo \#$ -S \/bin\/bash  >> %s"%(out))
	os.system("echo \#$ -j y  >> %s"%(out))
	os.system("echo \#$ -N %s >> %s"%(sampleid,out))
	os.system("echo \#$ -e %s >> %s"%(logdir,out))
	os.system("echo \#$ -o %s >> %s"%(logdir,out))
	os.system('''echo %s -o %s/tophat_%s -p %s %s %s/hg19 %s/%s_1.fastq %s/%s_2.fastq >> %s'''%(Tophat,outdir,sampleid,ncore,option,refdir,inputdir,sampleid,inputdir,sampleid,out))
	os.system("chmod 755 %s"%out)
	os.system("cd %s"%shdir)
	os.system("qsub -pe mpich %s %s"%(ncore,out)) 
