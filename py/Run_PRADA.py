import os,glob 

Prada="/storage/home/mglee/source/pyPRADA_1.2/./prada-preprocess-bimod"
maindir="/storage/home/mglee/TCGA_PRADA/ACC/"
shdir=maindir+"/11.sh_ACC/"
logdir=maindir+"/log" #logpath=outpath+'/log/'+logfilename
outdir=maindir

conf="/storage/home/mglee/source/pyPRADA_1.2/conf.txt"
refdir="/storage/home/mglee/source/THF/tophat_ref"
step="2_e1_1"
ncore=12
inputdir="/storage/home/mglee/Raw_TCGA/ACC/"
# wwn=0;stop=3have to run
inf=glob.glob("/storage/home/mglee/Raw_TCGA/ACC/TCGA*_1.fastq")
l=0 ; wwn=1 ; stop=100
for line in inf: # one sample
#	if "#" in line : continue  
	l+=1
	if l <=wwn : continue 
	if l > stop  : continue  # control key ? 
	mulnum=(stop-wwn)/4
	if l<=wwn+mulnum : node="1"
	if l<=wwn+2*mulnum and l> wwn+mulnum: node="2"
	if l<=wwn+3*mulnum and l> wwn+2*mulnum : node="3"
	if l<=wwn+4*mulnum and l> wwn+3*mulnum : node="4"
	#else: node="1"
	sampleid= line.split("/")[6].split("_1.fastq")[0]
	print sampleid
	out="%s/%s.sh"%(shdir,sampleid)
	#print '''%s inputdir %s -sample %s/TCGA-OR-A5K9-01A_1 -conf %s  -tag %s -platform illumina -step %s -intermediate no --pbs %s -outdir %s -submit no '''%(Prada,inputdir,inputdir,conf,sampleid,step,sampleid,outdir)
	os.system('''%s inputdir %s -sample %s%s -conf %s  -tag %s -platform illumina -step %s -intermediate no --pbs %s -outdir %s -submit no '''%(Prada,inputdir,inputdir,sampleid,conf,sampleid,step,sampleid,outdir))
	os.system("chmod 755 %s"%out)
	os.system("cd %s"%shdir)
	os.system("qsub -pe mpich %s -q anode64.q@anode64-0-%s %s"%(ncore,node,out)) 
	#os.system("qsub -pe mpich %s -q inode24.q@inode24-0-%s %s"%(ncore,node,out)) 
