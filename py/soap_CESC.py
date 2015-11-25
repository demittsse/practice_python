import os,glob 
cancertype="CESC"
maindir="/storage/home/mglee/Soap_TCGA/13.%s"%(cancertype)
shdir=maindir+"/11.sh_%s/"%(cancertype)
logdir=maindir+"/log"
outdir=maindir+"/13.result_%s/"%(cancertype)
listdir=maindir+"/01.list/"
ncore=8
config="/storage/home/mglee/Soap_TCGA/DLBCcon.txt"
data="/storage/home/mglee/Raw_TCGA/"
inputdir="/storage/home/mglee/Raw_TCGA/CESC/ln_CESC/"
step=1
##Snumber="s0%s"%step
os.system("mkdir %s")
os.system("mkdir %s %s %s"%(shdir, logdir, outdir))

inf=inf=glob.glob("%sTCGA*_1.fastq"%inputdir)
l=0 ; wwn=200 ;stop=210
for line in inf: 
	l+=1
	if l <=wwn : continue
	if l > stop  : continue 
	sampleid= line.split("/")[7].split("_")[0]
	print sampleid
	out="%s/%s.sh"%(shdir,sampleid)
	print "perl /storage3/Project/mglee/programs/SOAPfuse-v1.26/SOAPfuse-RUN.pl -c %s -fd %s -l %s%s.txt -o %s/%s -fs %s >> %s"%(config,data,listdir,sampleid,outdir,sampleid,step,out)
	os.system("echo \#! \/bin\/bash  > %s"%(out))
	os.system("echo \#$ -q anode64.q@anode64-0-3>> %s"%(out))
	#os.system("echo \#$ -q inode24.q@inode24-0-2 >> %s"%(out))
	os.system("echo \#$ -S \/bin\/bash  >> %s"%(out))
	os.system("echo \#$ -j y  >> %s"%(out))
	os.system("echo \#$ -N %s >> %s"%(sampleid,out))
	os.system("echo \#$ -e %s >> %s"%(logdir,out))
	os.system("echo \#$ -o %s >> %s"%(logdir,out))
	os.system('''echo perl /storage/home/mglee/source/SOAP/SOAPfuse-v1.26/SOAPfuse-RUN.pl -c %s -fd %s -l %s%s.txt -o %s%s  >> %s'''%(config,data,listdir,sampleid,outdir,sampleid,out))
	os.system("chmod 755 %s"%out)
	os.system("cd %s"%shdir)
	os.system("qsub -pe mpich %s %s"%(ncore,out))


#perl /storage3/Project/mglee/programs/SOAPfuse-v1.26/SOAPfuse-RUN.pl -c /storage/home/mglee/Soap_TCGA/DLBCcon.txt -fd /storage/home/mglee/Raw_TCGA/ -l /storage/home/mglee/Soap_TCGA/13.CESC/12.list_CESCTCGA-DR-A0ZM-01A.txt -o /storage/home/mglee/Soap_TCGA/13.CESC/13.result_CESCTCGA-DR-A0ZM-01A -fs 1 >> /storage/home/mglee/Soap_TCGA/13.CESC/11.sh_CESC/TCGA-DR-A0ZM-01A.sh
