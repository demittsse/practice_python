import os,glob,time
shdir="/storage/home/mglee/sh/"
logdir="/storage/home/mglee/log/"
inf=glob.glob("/storage/home/mglee/LAML_fish/map_fusion/1.RUNX1_X1T1/neg_res/1.BAM/*.sorted.bam")
#done=glob.glob("%s*.tar.gz"%outpath)
ncore=1
l=0
for line in inf: 
	sampleid= line.split("/")[9].split(".bam")[0]
	l+=1
	print sampleid
	
	out="%s/%s.sh"%(shdir,sampleid)
	os.system("echo \#! \/bin\/bash  > %s"%(out))
	os.system("echo \#$ -S \/bin\/bash  >> %s"%(out))
	os.system("echo \#$ -j y  >> %s"%(out))
	os.system("echo \#$ -N N%s >> %s"%(sampleid.split(".sorted")[0].split("TCGA-")[1],out))
	os.system("echo \#$ -e %s >> %s"%(logdir,out))
	os.system("echo \#$ -o %s >> %s"%(logdir,out))
	os.system("echo samtools view %s > /storage/home/mglee/LAML_fish/map_fusion/1.RUNX1_X1T1/neg_res/2.sorted/%s.txt >> %s"%(line,sampleid,out))
	os.system("chmod 755 %s"%out)
	os.system("cd %s"%shdir)
	os.system("qsub -pe mpich %s -q anode64.q %s"%(ncore,out)) 
	#os.system("qsub -pe mpich %s -q inode24.q%s"%(ncore,out)) 
	time.sleep()
