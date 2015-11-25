import os,glob,time
# ACC  BLCA  CESC  CHOL  DLBC  ESCA  HNSC  KIRC  LAML  LGG  MESO  OV  PCPG  PRAD  READ  SARC  SKCM  STAD  THYM  UCS  UVM
cancer="CESC"
inpath="/storage/Project/TCGA/%s/"%cancer
outpath= "/storage/home/mglee/Raw_TCGA/%s/"%cancer
shdir="/storage/home/mglee/sh/"
logdir="/storage/home/mglee/log/"
os.system("mkdir %s"%outpath)


listf=open("/storage/home/mglee/Raw_TCGA/CESC/sh/list.txt")
legacy=[]; filename=[]; analysis=[] ; Tdict=dict()
for ff in listf:
	if "<analysis_id>" in ff: 
		analysisL=ff.split("</analysis_id>")[0].replace("<analysis_id>","")
		analysis.append(analysisL)
	if "<filename>" in ff: 
		#filenameL=line.split(".")[2].split(".tar.gz")[0]
		filenameL=ff.split(".")[0].split("\t\t\t\t<filename>")[1]
		filename.append(filenameL)
	
	if "<legacy_sample_id>" in ff: 
		legacyL=ff.split("<legacy_sample_id>")[1].split("-")[0:4]
		legacyLi = "-".join(legacyL)
		#if legacy
		legacy.append(legacyLi)
		Tdict[filenameL]=legacyLi 


inf=glob.glob("%s/*.tar.gz"%inpath)
#done=glob.glob("%s*.tar.gz"%outpath)
ncore=1

l=0 ; wwn=1 ; stop=220
for line in inf: # one sample
	l+=1
	if l <=wwn : continue 
	if l > stop  : continue  # control key ? 
	sampleid= line.split("/")[5]
	UNCID=sampleid.split(".")[0]
	#if outpath+UNCID+".tar.gz" in done:continue
	
	print UNCID,l
	
	out="%s/%s.sh"%(shdir,UNCID)
	os.system("echo \#! \/bin\/bash  > %s"%(out))
	os.system("echo \#$ -S \/bin\/bash  >> %s"%(out))
	os.system("echo \#$ -j y  >> %s"%(out))
	os.system("echo \#$ -N %s >> %s"%(UNCID,out))
	os.system("echo \#$ -e %s >> %s"%(logdir,out))
	os.system("echo \#$ -o %s >> %s"%(logdir,out))
	
	#os.system("echo cp %s/%s %s/%s.tar.gz"%(inpath, sampleid, outpath, UNCID))
	#os.system("echo cp %s/%s %s/%s.tar.gz >> %s"%(inpath, sampleid, outpath, UNCID, out))
	#os.system("echo mkdir %s/%s>>%s"%(outpath, Tdict[UNCID], out))
	#os.system("echo mv %s/%s.tar.gz %s/%s >> %s"%(outpath, UNCID, outpath, Tdict[UNCID], out))
	os.system("echo tar xzvf %s%s/%s.tar.gz>>%s"%(outpath, Tdict[UNCID], UNCID,out))
	
	os.system("chmod 755 %s"%out)
	os.system("cd %s"%shdir)
	os.system("qsub -pe mpich %s -q anode64.q %s"%(ncore,out)) 
	time.sleep(2)
	#os.system("qsub -pe mpich %s -q inode24.q%s"%(ncore,out)) 
