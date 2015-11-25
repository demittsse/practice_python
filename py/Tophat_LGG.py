import os,glob,time

Tophat="/storage/home/mglee/source/THF/tophat-2.0.14.Linux_x86_64/tophat"
maindir="/storage/home/mglee/Tophat_TCGA/15.LGG/"
shdir=maindir+"/11.sh_LGG/"
logdir=maindir+"/log/"
outdir=maindir+"/13.result/"
#os.system("mkdir %s"%maindir); os.system("mkdir %s %s %s"%(shdir, logdir, outdir))
option="--fusion-search --keep-fasta-order --bowtie1 --no-coverage-search -r 0 --mate-std-dev 80 --max-intron-length 50000 --fusion-min-dist 100000 --fusion-anchor-length 20 --fusion-ignore-chromosomes chrM"
refdir="/storage/home/mglee/source/THF/tophat_ref"
ncore=8
inputdir="/storage/home/mglee/Raw_TCGA/LGG/ln_LGG/"
#Your job 10795 ("TCGA-W5-AA2G-01A") has been submitted
inf=glob.glob("%sTCGA*_1.fastq"%inputdir)

l=0 ; wwn=409 ;stop=415
for line in inf: 
	l+=1
	if l <=wwn : continue
	if l > stop  : continue 
	sampleid= line.split("/")[7].split("_1.fastq")[0]	
	print sampleid
	print "%s -o %s/tophat_%s -p %s %s %s/hg19 %s/%s_1.fastq %s/%s_2.fastq"%(Tophat,outdir,sampleid,ncore,option,refdir,inputdir,sampleid,inputdir,sampleid)
	inputfile1="%s/%s_1.fastq"%(inputdir, sampleid); inputfile2="%s/%s_2.fastq"%(inputdir, sampleid)
	EXfile1=os.path.isfile(inputfile1); EXfile2=os.path.isfile(inputfile2)
	if EXfile1 == True and EXfile2 ==True:
		out="%s/T_%s.sh"%(shdir,"".join(sampleid.split("-")[1:3]))
		os.system("echo \#! \/bin\/bash  > %s"%(out))
		os.system("echo \#$ -q anode64.q@anode64-0-1 >> %s"%(out))
		#os.system("echo \#$ -q inode24.q@inode24-0-3>> %s"%(out))
		os.system("echo \#$ -S \/bin\/bash  >> %s"%(out))
		os.system("echo \#$ -j y  >> %s"%(out))
		os.system("echo \#$ -N %s >> %s"%(sampleid,out))
		os.system("echo \#$ -e %s >> %s"%(logdir,out))
		os.system("echo \#$ -o %s >> %s"%(logdir,out))
		#os.system("echo sleep 3600 >> %s"%(out))
		os.system('''echo %s -o %s/tophat_%s -p %s %s %s/hg19 %s %s >> %s'''%(Tophat,outdir,sampleid,ncore,option,refdir,inputfile1,inputfile2,out))
		os.system("chmod 755 %s"%out)
		os.system("cd %s"%shdir)
		os.system("qsub -pe mpich %s %s"%(ncore,out)) 
		time.sleep(3)
