import os,glob 

Tophat="/storage/home/mglee/source/THF/tophat-2.0.14.Linux_x86_64/tophat"
maindir="/storage/home/mglee/Tophat_TCGA/12.ACC"
shdir=maindir+"/11.sh_ACC/"
logdir=maindir+"/log"
outdir=maindir+"/13.result"
option=option="--fusion-search --keep-fasta-order --bowtie1 --no-coverage-search -r 0 --mate-std-dev 80 --max-intron-length 100000 --fusion-min-dist 10000 --fusion-anchor-length 20 --fusion-ignore-chromosomes chrM"
refdir="/storage/home/mglee/source/THF/tophat_ref"
ncore=8
inputdir="/storage/home/mglee/Raw_TCGA/ACC/"
# wwn=0;stop=3have to run
inf=glob.glob("/storage/home/mglee/Raw_TCGA/ACC/TCGA*_1.fastq")
l=0 ; wwn=80 ;stop=100
for line in inf: 
	l+=1
	if l <=wwn : continue
	if l > stop  : continue 
	sampleid= line.split("/")[6].split("_1.fastq")[0]	
	print sampleid
	out="%s/%s.sh"%(shdir,sampleid)
	os.system("echo \#! \/bin\/bash  > %s"%(out))
	os.system("echo \#$ -q anode64.q@anode64-0-1 >> %s"%(out))
	##dellr815.q@dellr815-0-0 multi.q@multi-0-3
	os.system("echo \#$ -S \/bin\/bash  >> %s"%(out))
	os.system("echo \#$ -j y  >> %s"%(out))
	os.system("echo \#$ -N %s >> %s"%(sampleid,out))
	os.system("echo \#$ -e %s >> %s"%(logdir,out))
	os.system("echo \#$ -o %s >> %s"%(logdir,out))
	os.system('''echo %s -o %s/tophat_%s -p %s %s %s/hg19 %s/%s_1.fastq %s/%s_2.fastq >> %s'''%(Tophat,outdir,sampleid,ncore,option,refdir,inputdir,sampleid,inputdir,sampleid,out))
	os.system("chmod 755 %s"%out)
	os.system("cd %s"%shdir)
	os.system("qsub -pe mpich %s %s"%(ncore,out)) 
