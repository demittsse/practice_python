import os, glob, time

##step01 Untar
inf1=glob.glob("/storage/Project/TCGA/LGG/fasta/*/*tar.gz")
maindir="/storage/home/mglee/Raw_TCGA/LGG/"
tardir="/storage/home/mglee/Raw_TCGA/LGG/tar"
os.system("mkdir %s"%(tardir.split("tar")[0]))
os.system("mkdir %s"%(tardir))
for line in inf1: 
	if ".gto" in line: continue
	samname=line.split("/")[6]
	samline="mkdir %s/%s"%(tardir,samname)
	#print samline
	os.system(samline)
	tarline="tar xvzf %s -C %s/%s"%(line,tardir,samname)
	print tarline
	os.system(tarline)
	time.sleep(2)
## step02 softlink [3]

	
#2

legacy=[]; filename=[]; analysis=[] ; Tdict=dict()
for ff in listf:
	if "<analysis_id>" in ff: #3457cb70-f9ed-4e80-8493-f6585d29de6e
		analysisL=ff.split("</analysis_id>")[0].replace("\t\t<analysis_id>","")
		analysis.append(analysisL)
	if "<filename>" in ff: #UNCID...9d7ac.140721_
		#filenameL=line.split(".")[2].split(".tar.gz")[0]
		filenameL=ff.split(".")[0].split("\t\t\t\t<filename>")[1]
		filename.append(filenameL)
	
	if "<legacy_sample_id>" in ff:  #TCGA-AB-..
		legacyL=ff.split("<legacy_sample_id>")[1].split("-")[0:4]
		#legacyL=ff.split("<legacy_sample_id>")[1].split("</legacy_sample_id>")[0]
		legacyLi = "-".join(legacyL)
		#if legacy
		legacy.append(legacyLi)
		Tdict[analysisL]=legacyL 

len(Tdict.keys())


os.system("mkdir %s"%lndir)
inf2= glob.glob("%s/*/*.fastq"%tardir)
linenum=0
for item in inf2:
	linenum+=1
	ali="ln -s %s %s%s_%s"%(item, lndir, "-".join(Tdict[item.split("/")[7]]),item.split("_")[7])
	print ali,linenum
	os.system(ali)
	
##step01 Untar
inf1=glob.glob("/storage/Project/TCGA/CHOL/fasta/*/*tar.gz")
tardir="/storage/home/mglee/Raw_TCGA/CHOL/tar"
for line in inf1: 
	if ".gto" in line: continue
	samname=line.split("/")[6]
	samline="mkdir %s/%s"%(tardir,samname)
	#print samline
	#os.system(samline)
	tarline="tar xvzf %s -C %s/%s"%(line,tardir,samname)
	print tarline
	os.system(tarline)
	time.sleep(2)
	

## step02 softlink
import os, glob
cancertype="LGG/"
maindir="/storage/home/mglee/Raw_TCGA/"+cancertype+"/"
tardir=maindir+"tar"
lndir=maindir+"/ln_"+cancertype
listf=open("/storage/home/mglee/Raw_TCGA/LGG/LGG.xml")
legacy=[]; filename=[]; analysis=[] ; Tdict=dict()
for ff in listf:
	if "<analysis_id>" in ff: #3457cb70-f9ed-4e80-8493-f6585d29de6e
		analysisL=ff.split("<analysis_id>")[1].split("</analysis_id>")[0]
		#analysis.append(analysisL)
	if "<legacy_sample_id>" in ff:  #TCGA-AB-..
		legacyL=ff.split("<legacy_sample_id>")[1].split("-")[0:4]
		#legacyL=ff.split("<legacy_sample_id>")[1].split("</legacy_sample_id>")[0]
		legacyLi = "-".join(legacyL)+"_"+str(bnum)
		print legacyLi
		legacy.append(legacyL)
	if  legacyLi not in Tdict.keys():
		bnum=1
		Tdict[analysisL]=legacyLi
	if  legacyLi in Tdict.keys():
		bnum+=1
		Tdict[analysisL]=legacyLi
		
	if "<filename>" in ff: #UNCID...9d7ac.140721_
		#filenameL=line.split(".")[2].split(".tar.gz")[0]
		filenameL=ff.split(".")[0].split("\t\t\t\t<filename>")[1]
		filename.append(filenameL)
len(Tdict.keys())


os.system("mkdir %s"%lndir)
inf2= glob.glob("%s/*/*.fastq"%tardir)
linenum=0
for item in inf2:
	print item 
	linenum+=1
	try:
		print "ln -s %s %s%s_%s"%(item, lndir, Tdict[item.split("/")[8]],item.split("_")[7])
	except :print item.split("_")[7],linenum
	ali="ln -s %s %s%s_%s"%(item, lndir, Tdict[item.split("/")[8]],item.split("_")[7])
	os.system(ali)
	
import os, glob

uuid=[]; barcode=[]; Tdict=dict()
for ff in listf:
	
	barc1=ff.split("\t")[1]+"_"+str(bnum)
	sampname=ff.split("\t")[3]


os.system("mkdir %s"%lndir)
inf2= glob.glob("%s/*/*.fastq"%tardir)
linenum=0
for item in inf2:
	linenum+=1
	ali="ln -s %s %s%s_%s"%(item, lndir, "-".join(Tdict[item.split("/")[8]]),item.split("_")[7])
	print ali,linenum
	os.system(ali)
##############  CESC #############################
inf= glob.glob("/storage/home/mglee/Raw_TCGA/CESC/*-01A/*.tar.gz")
l=0 ; wwn=180 ; stop=220
for line in inf: # one sample
	l+=1
	if l <=wwn : continue 
	if l > stop  : continue  	
	dire=line.split("UNCID")[0]
	print dire
	
	os.system("tar xvzf %s -C %s"%(line,dire))
print "---------------------------------------------------------------------------------"


import os, glob
inf2= glob.glob("/storage/home/mglee/Raw_TCGA/CESC/*-01A/*.fastq")
for item in inf2:
	ali="ln -s %s /storage/home/mglee/Raw_TCGA/CESC/ln_CESC/%s_%s"%(item, item.split("/")[6],item.split("_")[7])
	print ali
	os.system(ali)


/storage/Project/TCGA/ESCA/fasta/*/*.tar

import os, glob, time
inf=glob.glob("/storage/Project/TCGA/ESCA/fasta/*/*.tar")
lndir="/storage/home/mglee/Raw_TCGA/ESCA/"
tarlist=[]
logdir="/storage/home/mglee/sh/"
ncore="1"
l=0 ; wwn=0 ;stop=100
for line in inf: 
	l+=1
	if l <=wwn : continue
	if l > stop  : continue 
	pp= "-".join(line.split("/")[7].split("-")[0:4])
	out = "%s%s.sh"%(logdir,pp)
	if pp in tarlist:
		print pp
	if pp not in tarlist:
		tarlist.append(pp)
	
	if pp=="TCGA-X8-AAAR-01A":continue
	print pp
	#os.system("mkdir %s%s"%(lndir, pp))
	#os.system("ln -s %s %s%s"%(line,lndir, pp))
	os.system("echo \#! \/bin\/bash  > %s"%(out))
	os.system("echo \#$ -q anode64.q@anode64-0-2 >> %s"%(out))
	os.system("echo \#$ -q inode24.q>> %s"%(out))
	#os.system("echo \#$ -S \/bin\/bash  >> %s"%(out))
	os.system("echo \#$ -j y  >> %s"%(out))
	os.system("echo \#$ -N %s >> %s"%(pp,out))
	os.system("echo \#$ -e %s >> %s"%(logdir,out))
	os.system("echo \#$ -o %s >> %s"%(logdir,out))
	#os.system('''echo mkdir %s%s >> %s'''%(lndir, pp ,out))
	#os.system('''echo ln -s %s %s%s >> %s'''%(line, lndir, pp,out))
	os.system('''echo tar xvf %s%s/%s -C %s%s >> %s'''%(lndir, pp,line.split("/")[7],lndir, pp,out))
	os.system('''echo gunzip %s%s/*.fastq.gz >> %s'''%(lndir, pp,out))
	os.system('''echo ln -s %s%s/*_1.fastq %s/ln_ESCA/%s_1.fastq>> %s'''%(lndir, pp,lndir,pp,out))
	os.system('''echo ln -s %s%s/*_2.fastq %s/ln_ESCA/%s_2.fastq>> %s'''%(lndir, pp,lndir,pp,out))
	os.system("chmod 755 %s"%out)
	os.system("cd %s"%logdir)
	os.system("qsub -pe mpich %s %s"%(ncore,out)) 
	time.sleep(1)
