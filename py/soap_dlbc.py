import os,glob 

maindir="/storage/home/mglee/Soap_TCGA/12.DLBC"
shdir=maindir+"/11.sh_DLBC/"
logdir=maindir+"/log"
outdir=maindir+"/13.result_DLBC/"
listdir=maindir+"/12.list_DLBC/"
ncore=8
config="/storage/home/mglee/Soap_TCGA/DLBCcon.txt"
data="/storage/home/yeeun/"
inputdir="/storage/home/yeeun/"
##step=1
##Snumber="s0%s"%step

inf=open("/storage/home/mglee/Soap_TCGA/12.DLBC/LUADSL.txt")
l=0 ; wwn=8 ;stop=20
for line in inf: 
	l+=1
	if l <=wwn : continue
	if l > stop  : continue 
	sampleid= line.replace("\n","")
	print sampleid
	out="%s/%s.sh"%(shdir,sampleid)
	##print "perl /storage3/Project/mglee/programs/SOAPfuse-v1.26/SOAPfuse-RUN.pl -c %s -fd %s -l %s%s.txt -o %s%s -fs %s >> %s"%(config,data,listdir,sampleid,outdir,sample
id,step,out)
	os.system("echo \#! \/bin\/bash  > %s"%(out))
	os.system("echo \#$ -q anode64.q@anode64-0-3>> %s"%(out))
	##dellr815.q@dellr815-0-0 multi.q@multi-0-3
	os.system("echo \#$ -S \/bin\/bash  >> %s"%(out))
	os.system("echo \#$ -j y  >> %s"%(out))
	os.system("echo \#$ -N %s >> %s"%(sampleid,out))
	os.system("echo \#$ -e %s >> %s"%(logdir,out))
	os.system("echo \#$ -o %s >> %s"%(logdir,out))
	os.system('''echo perl /storage/home/mglee/source/SOAP/SOAPfuse-v1.26/SOAPfuse-RUN.pl -c %s -fd %s -l %s%s.txt -o %s%s  >> %s'''%(config,data,listdir,sampleid,outdir,sa
mpleid,out))
	os.system("chmod 755 %s"%out)
	os.system("cd %s"%shdir)
	os.system("qsub -pe mpich %s %s"%(ncore,out))
