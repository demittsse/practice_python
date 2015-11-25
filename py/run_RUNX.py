import os,glob

maindir="/storage/home/mglee/LAML_fish/map_fusion/1.RUNX1_X1T1"
shdir=maindir+"/11.sh_LAML/"
logdir=maindir+"/2.negpos/"
#outdir=maindir+"/pos_res/"
outdir=maindir+"/neg_res/"
bamdir=outdir+"/1.BAM/"
bcfdir=outdir+"/2.mpile/"
donedir=bamdir+"/*"
ncore=8
bowtie="/storage/home/mglee/source/bowtie2-2.2.5/"
option=""
refdir="/storage/home/mglee/LAML_fish/map_fusion/1.RUNX1_X1T1/bowidx/RUNX"
inputdir="/storage/Project/TCGA/LAML/"


#inf=open("/storage/home/mglee/LAML_fish/map_fusion/RUNX1_X1T1/fishposList.txt","r")
#inf=open("/storage/home/mglee/LAML_fish/map_fusion/RUNX1_X1T1/14.result/Nosamlist.txt")
inf=open("/storage/home/mglee/LAML_fish/tophat/total_run.txt","r")

doneL=[];NosamL=[]
done=glob.glob("/storage/home/mglee/LAML_fish/map_fusion/1.RUNX1_X1T1/pos_res/1.BAM/*")
for item in done:
	dd=item.split("/")[9].split(".sorted.bam")[0]
	doneL.append(dd)
"""
nsf=open("/storage/home/mglee/LAML_fish/map_fusion/RUNX1_X1T1/14.result/Nosamlist.txt")
for ns in nsf:
	nsl=ns.replace("\n","")
	NosamL.append(nsl)
"""
#/storage/Project/TCGA/LAML
l=0 ; wwn=0 ; stop=200
for line in inf: # one sample
#	if "#" in line : continue  
	l+=1
	if l <=wwn : continue 
	if l > stop  : continue  # control key ? 
	mulnum=(stop-wwn)/4
	if l<=wwn+mulnum :node="1"
	if l<=wwn+2*mulnum and l> wwn+mulnum:node="2"
	if l<=wwn+3*mulnum and l> wwn+2*mulnum :node="3"
	if l<=wwn+4*mulnum and l> wwn+3*mulnum :node="4"
	sampleid=line.replace("\n","")
	if sampleid in doneL:continue
#	if sampleid in NosamL: continue
	print sampleid, node
	out="%s/%s.sh"%(shdir,sampleid)
	os.system("echo \#! \/bin\/bash  > %s"%(out))
	#os.system("echo \#$ -q anode64.q >>%s"%out)
	os.system("echo \#$ -q anode64.q@anode64-0-%s >> %s"%(node,out))
	#os.system("echo \#$ -q inode24.q@inode24-0-%s >> %s"%(node,out))
	os.system("echo \#$ -S \/bin\/bash  >> %s"%(out))
	os.system("echo \#$ -j y  >> %s"%(out))
	os.system("echo \#$ -N %s >> %s"%("".join(sampleid.split("-")[1:]),out))
	os.system("echo \#$ -e %s >> %s"%(logdir,out))
	os.system("echo \#$ -o %s >> %s"%(logdir,out))
	os.system('''echo %s/bowtie2 -x %s -p %s %s -1 %s/%s_1.fastq -2 %s/%s_2.fastq -S %s%s.sam>> %s'''%(bowtie,refdir,ncore,option,inputdir,sampleid,inputdir,sampleid,outdir,sampleid,out))
	os.system('''echo samtools view -Sbh %s/%s.sam \> %s/%s.bam>>%s'''%(outdir,sampleid,bamdir,sampleid,out))
	os.system('''echo samtools sort %s%s.bam %s/%s.sorted>>%s'''%(bamdir,sampleid,bamdir,sampleid,out))
	os.system('''echo samtools index %s%s.sorted.bam >>%s'''%(bamdir,sampleid,out))
	#os.system('''echo samtools mpileup -f %s1_RUNX1T1Comb.fa %s/%s.sorted.bam \> %s/%s.mpileup >>%s'''%(refdir,bamdir, sampleid,bcfdir,sampleid,out))
	os.system("chmod 755 %s"%out)
	os.system("cd %s"%shdir)
	os.system("qsub -pe mpich %s %s"%(ncore,out)) 

"""
import os,glob
runl=['TCGA-AB-2903', 'TCGA-AB-2930', 'TCGA-AB-2881', 'TCGA-AB-2844', 'TCGA-AB-2955', 'TCGA-AB-2933', 'TCGA-AB-2899', 'TCGA-AB-2919', 'TCGA-AB-2936', 'TCGA-AB-2918', 'TCGA-AB-2886', 'TCGA-AB-2834', 'TCGA-AB-2934', 'TCGA-AB-2938', 'TCGA-AB-2931', 'TCGA-AB-2884', 'TCGA-AB-2830', 'TCGA-AB-3006', 'TCGA-AB-2848', 'TCGA-AB-2956', 'TCGA-AB-2975', 'TCGA-AB-2950', 'TCGA-AB-2948', 'TCGA-AB-2909', 'TCGA-AB-2937', 'TCGA-AB-2875', 'TCGA-AB-2858', 'TCGA-AB-2910', 'TCGA-AB-2932', 'TCGA-AB-2870', 'TCGA-AB-2869', 'TCGA-AB-2940', 'TCGA-AB-2880', 'TCGA-AB-2924', 'TCGA-AB-2912', 'TCGA-AB-2895', 'TCGA-AB-2891', 'TCGA-AB-2908', 'TCGA-AB-2966', 'TCGA-AB-2900', 'TCGA-AB-2901', 'TCGA-AB-2944', 'TCGA-AB-2921', 'TCGA-AB-2959', 'TCGA-AB-2929', 'TCGA-AB-2987', 'TCGA-AB-2874', 'TCGA-AB-2887', 'TCGA-AB-2873', 'TCGA-AB-2986', 'TCGA-AB-2889', 'TCGA-AB-2914', 'TCGA-AB-2879']

inf=glob.glob("/storage/Project/TCGA/LAML/TCGA*_1.fastq")
ouf=open("/storage/home/mglee/LAML_fish/map_fusion/RUNX1_X1T1/fishposList.txt","w")
sameL=[]
for line in inf:
	dcl1=line.split("/")[5].split("_")[0].split("-")[1]
	dcl2=line.split("/")[5].split("_")[0].split("-")[2]
	dcl3="TCGA-"+dcl1+"-"+dcl2
	if dcl3 in runl: 
		WL=line.split("/")[5].split("_1.fastq")[0]
		sameL.append(WL)
"""
