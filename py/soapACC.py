import os,glob 
cancertype="ACC"
maindir="/storage/home/mglee/Soap_TCGA/14.%s"%(cancertype)
shdir=maindir+"/11.sh_%s/"%(cancertype)
logdir=maindir+"/log"
outdir=maindir+"/13.result_%s/"%(cancertype)
listdir=maindir+"/01.list/"
ncore=8
config="/storage/home/mglee/Soap_TCGA/DLBCcon.txt"
data="/storage/home/mglee/"
inputdir="/storage/home/mglee/Raw_TCGA/ACC/"
step=1
##Snumber="s0%s"%step
#os.system("mkdir %s")
#os.system("mkdir %s %s %s"%(shdir, logdir, outdir))

#inf=inf=glob.glob("%sTCGA*_1.fastq"%inputdir)
inf=open("/storage/home/mglee/Soap_TCGA/14.ACC/remains.txt")
l=0 ; wwn=0 ;stop=15
for line in inf: 
	l+=1
	if l <=wwn : continue
	if l > stop  : continue 
	#sampleid= line.split("/")[6].split("_1.fastq")[0]
	sampleid=line.split("\n")[0]
	print sampleid, "".join(sampleid.split("-")[1:4])
	out="%s/%s.sh"%(shdir,sampleid)
	print "perl /storage3/Project/mglee/programs/SOAPfuse-v1.26/SOAPfuse-RUN.pl -c %s -fd %s -l %s%s.txt -o %s/%s -fs %s >> %s"%(config,data,listdir,sampleid,outdir,sampleid,step,out)
	os.system("echo \#! \/bin\/bash  > %s"%(out))
	os.system("echo \#$ -q anode64.q@anode64-0-3>> %s"%(out))
	#os.system("echo \#$ -q inode24.q@inode24-0-2 >> %s"%(out))
	os.system("echo \#$ -S \/bin\/bash  >> %s"%(out))
	os.system("echo \#$ -j y  >> %s"%(out))
	os.system("echo \#$ -N T%s >> %s"%("".join(sampleid.split("-")[1:3]),out))
	os.system("echo \#$ -e %s >> %s"%(logdir,out))
	os.system("echo \#$ -o %s >> %s"%(logdir,out))
	os.system('''echo perl /storage/home/mglee/source/SOAP/SOAPfuse-v1.26/SOAPfuse-RUN.pl -c %s -fd %s -l %s%s.txt -o %s%s  >> %s'''%(config,data,listdir,sampleid,outdir,sampleid,out))
	os.system("chmod 755 %s"%out)
	os.system("cd %s"%shdir)
	os.system("qsub -pe mpich %s %s"%(ncore,out))

