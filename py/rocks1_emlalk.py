import os,glob,time

#maindir="/storage/home/mglee/LAML_fish/map_fusion/b1.RUNX1_RUNX1T1"
#maindir="/storage3/Project/mglee/LAML_fish/3.EML_ALK/"
maindir="/storage3/Project/mglee/LAML_fish/4.all_EML4ALK/neg/"
shdir=maindir+"/0.sh_LAML/"
logdir=maindir+"/log/"
outdir=maindir+"/1.SAM/"
bamdir=maindir+"/2.BAM/"
sortdir=maindir+"/3.sorted/"
bcfdir=maindir+"/4.mpile/"

ncore=2
bowtie="/storage3/Project/mglee/programs/bowtie-1.1.1/"
option=""
samtools="/storage3/Project/mglee/programs/tophat-2.0.14.Linux_x86_64/./samtools_0.1.18"
#refdir="/storage3/Project/mglee/LAML_fish/2.100LC/2.ref/fs"
refdir="/storage3/Project/mglee/LAML_fish/4.all_EML4ALK/ref/EML4_ALK"
#refFile=refdir+"_merge.fa"
refFile=refdir+".fa"
inputdir="/storage/Project/dbGap/TCGA/LUAD/ln_fasta_real/"
os.system("mkdir %s"%maindir)
os.system("mkdir %s %s %s %s %s %s"%(shdir, logdir, outdir, bamdir, sortdir, bcfdir))

#inf=open("/storage3/Project/mglee/LAML_fish/1.EML4_ALK/poslist.txt")
inf=open("/storage3/Project/mglee/2.TCGA_THF/10.LUAD/list/LUADlist.txt")
doneL=[];NosamL=[]
#done=glob.glob("%s/*"%sortdir)
done=glob.glob("/storage3/Project/mglee/LAML_fish/4.all_EML4ALK/3.sorted/*")
for item in done:
	dd=item.split("/")[6].split(".sorted.bam")[0]
	doneL.append(dd)

l=0 ; wwn=570 ; stop=580
for line in inf: # one sample
#	if "#" in line : continue  
	l+=1
	if l <=wwn : continue 
	if l > stop  : continue  # control key ? 
	node="2"
	sampleid=line.replace("\n","")
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
	os.system("echo \#$ -N T%s >> %s"%("".join(sampleid.split("-")[1:]),out))
	os.system("echo \#$ -e %s >> %s"%(logdir,out))
	os.system("echo \#$ -o %s >> %s"%(logdir,out))
	os.system('''echo %s/bowtie %s -p %s %s -1 %s/%s_1.fastq -2 %s/%s_2.fastq -S %s%s.sam>> %s'''%(bowtie,refdir,ncore,option,inputdir,sampleid,inputdir,sampleid,outdir,sampleid,out))
	os.system('''echo %s view -Sbh -F 4 %s/%s.sam \> %s/%s.bam>>%s'''%(samtools, outdir,sampleid,bamdir,sampleid,out))
	os.system('''echo %s sort %s%s.bam %s/%s.sorted>>%s'''%(samtools,bamdir,sampleid,sortdir,sampleid,out))
	os.system('''echo %s index %s%s.sorted.bam >>%s'''%(samtools,sortdir,sampleid,out))
	os.system('''echo %s mpileup -f %s %s/%s.sorted.bam \> %s/%s.mpileup >>%s'''%(samtools, refFile,sortdir, sampleid,bcfdir,sampleid,out))
	os.system("chmod 755 %s"%out)
	os.system("cd %s"%shdir)
	os.system("qsub -pe mpich %s %s"%(ncore,out)) 
	time.sleep(1)
