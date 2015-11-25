import os,glob 

maindir="/storage/home/mglee/lymphoma/Soapfuse"
shdir=maindir+"/sh/"
logdir=maindir+"/log/"
outdir=maindir+"/result/"
listdir=maindir+"/list/"
ncore=8
config="/storage/home/mglee/lymphoma/Soapfuse/LUAD_cfg.txt"
data="/storage/home/mglee/lymphoma/"
inputdir="/storage/home/mglee/lymphoma/"
##step=1
##Snumber="s0%s"%step

inf=glob.glob("/storage/home/mglee/lymphoma/data/reserve/*_1.fastq")
#l=0 ; wwn=5 ;stop=11
for line in inf: 
#	l+=1
#	if l <=wwn : continue
#	if l > stop  : continue 
	#sampleid= line.split("/")[7].split("_")[0]
	sampleid="S1123664"
	print sampleid
	out="%s/%s.sh"%(shdir,sampleid)
	##print "perl /storage3/Project/mglee/programs/SOAPfuse-v1.26/SOAPfuse-RUN.pl -c %s -fd %s -l %s%s.txt -o %s%s -fs %s >> %s"%(config,data,listdir,sampleid,outdir,sampleid,step,out)
	os.system("echo \#! \/bin\/bash  > %s"%(out))
	os.system("echo \#$ -q anode64.q@anode64-0-3>> %s"%(out))
	##dellr815.q@dellr815-0-0 multi.q@multi-0-3
	os.system("echo \#$ -S \/bin\/bash  >> %s"%(out))
	os.system("echo \#$ -j y  >> %s"%(out))
	os.system("echo \#$ -N %s >> %s"%(sampleid,out))
	os.system("echo \#$ -e %s >> %s"%(logdir,out))
	os.system("echo \#$ -o %s >> %s"%(logdir,out))
	os.system('''echo perl /storage/home/mglee/source/SOAP/SOAPfuse-v1.26/SOAPfuse-RUN.pl -c %s -fd %s -l %s%s.txt -o %s%s  >> %s'''%(config,data,listdir,sampleid,outdir,sampleid,out))
	os.system("chmod 755 %s"%out)
	os.system("cd %s"%shdir)
	os.system("qsub -pe mpich %s %s"%(ncore,out)) 
