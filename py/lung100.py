import os,glob,time
#grep EML4_ALK *.mpileup | cut -f1 | sort |uniq | cut -d":" -f1
#maindir="/storage/home/mglee/LAML_fish/map_fusion/b1.RUNX1_RUNX1T1"
maindir="/storage3/Project/mglee/LAML_fish/2.100LC/"
shdir=maindir+"/0.sh_LAML/"
logdir=maindir+"/log/"
#outdir=maindir+"/pos_res/"
outdir=maindir+"/1.SAM/"
bamdir=maindir+"/2.BAM/"
sortdir=maindir+"/3.sorted/"
bcfdir=maindir+"/4.mpile/"
donedir=bamdir+"/*"
ncore=1
bowtie="/storage3/Project/mglee/programs/bowtie-1.1.1/"
option=""
samtools="/storage3/Project/mglee/programs/tophat-2.0.14.Linux_x86_64/./samtools_0.1.18"
#refdir="/storage/home/mglee/LAML_fish/map_fusion/b1.RUNX1_RUNX1T1/Fa/RUNX"
refdir="/storage3/Project/mglee/LAML_fish/1.EML4_ALK/bowidx/EML4_ALK"
refFile=refdir+"_merge.fa"
#refFile=refdir+".fa"
inputdir="/storage2/Project/LungCancer_100PAT_mRNa/"
#os.system("mkdir %s")
#os.system("mkdir %s %s %s %s %s %s"%(shdir, logdir, outdir, bamdir, sortdir, bcfdir))

inf=glob.glob("/storage2/Project/LungCancer_100PAT_mRNa/*.fq")

doneL=[];NosamL=[]
done=glob.glob("%s/*"%sortdir)
for item in done:
	dd=item.split("/")[8].split(".sorted.bam")[0]
	doneL.append(dd)
"""
nsf=open("/storage/home/mglee/LAML_fish/map_fusion/RUNX1_X1T1/14.result/Nosamlist.txt")
for ns in nsf:
	nsl=ns.replace("\n","")
	NosamL.append(nsl)
"""
#/storage/Project/TCGA/LAML
l=0 ; wwn=85 ; stop=86
for line in inf: # one sample
#	if "#" in line : continue  
	l+=1
	if l <=wwn : continue 
	if l > stop  : continue  # control key ? 
	node="0"
	"""mulnum=(stop-wwn)/4
	if l<=wwn+mulnum :node="1"
	if l<=wwn+2*mulnum and l> wwn+mulnum:node="2"
	if l<=wwn+3*mulnum and l> wwn+2*mulnum :node="3"
	if l<=wwn+4*mulnum and l> wwn+3*mulnum :node="4"""
	sampleid="Pat11T"
	#sampleid=line.split("/")[4].split("_")[0]
	if sampleid in doneL:continue
#	if sampleid in NosamL: continue
	print sampleid, node
	out="%s/%s.sh"%(shdir,sampleid)
	os.system("echo \#! \/bin\/bash  > %s"%(out))
	#os.system("echo \#$ -q anode64.q >>%s"%out)
	os.system("echo \#$ -q dellr815.q@dellr815-0-%s >> %s"%(node,out))
	#os.system("echo \#$ -q multi.q@multi-0-%s >> %s"%(node,out))
	os.system("echo \#$ -S \/bin\/bash  >> %s"%(out))
	os.system("echo \#$ -j y  >> %s"%(out))
	os.system("echo \#$ -N T%s >> %s"%(sampleid,out))
	os.system("echo \#$ -e %s >> %s"%(logdir,out))
	os.system("echo \#$ -o %s >> %s"%(logdir,out))
	os.system('''echo %s/bowtie %s -p %s %s -1 %s/%s_1.fq -2 %s/%s_2.fq -S %s%s.sam>> %s'''%(bowtie,refdir,ncore,option,inputdir,sampleid,inputdir,sampleid,outdir,sampleid,out))
	os.system('''echo %s view -Sbh -F 4 %s/%s.sam \> %s/%s.bam>>%s'''%(samtools, outdir,sampleid,bamdir,sampleid,out))
	os.system('''echo %s sort %s%s.bam %s/%s.sorted>>%s'''%(samtools,bamdir,sampleid,sortdir,sampleid,out))
	os.system('''echo %s index %s%s.sorted.bam >>%s'''%(samtools,sortdir,sampleid,out))
	os.system('''echo %s mpileup -f %s %s/%s.sorted.bam \> %s/%s.mpileup >>%s'''%(samtools, refFile,sortdir, sampleid,bcfdir,sampleid,out))
	os.system("chmod 755 %s"%out)
	os.system("cd %s"%shdir)
	os.system("qsub -pe mpich %s %s"%(ncore,out)) 
	time.sleep(1)
