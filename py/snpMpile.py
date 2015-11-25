import os,glob,time
ref="/storage/home/Jieun/utils/ref/GRCh37.72.genome.chr.fa"
workdir="/storage2/Project/LungCancer_100PAT_exome/test/mpileup_test/"
bamdir=workdir+"/ln/"
outdir=workdir+"/result/" #/storage2/Project/LungCancer_100PAT_exome/test/mpileup_test/result
shdir=workdir+"/sh/"
logdir=workdir+"/log/"
inf=glob.glob("%s/*bam"%bamdir)
l=0 ; wwn=4 ;stop=5
for line in inf: 
	l+=1
	if l <=wwn : continue
	if l > stop  : continue 
	file=line.split("/")[8].split(".recal.bam")[0]
	print file
	print "samtools mpileup -E -uf %s %s > %s/%s.recal.mpileup"%(ref, line, outdir, file)
	print "bcftools view -cg %s%s.recal.mpileup > %s%s.vcf"%(outdir, file,outdir, file)
	os.system("samtools mpileup -E -uf %s %s > %s/%s.recal.mpileup"%(ref, line, outdir, file))
	os.system("bcftools view -cg %s%s.recal.mpileup > %s%s.vcf"%(outdir, file,outdir, file))
	time.sleep(2)

mpileup -uf /storage/home/Jieun/utils/ref/GRCh37.72.genome.chr.fa /storage2/Project/LungCancer_100PAT_exome/Pat99T.recal.bam  > /storage2/Project/LungCancer_100PAT_exome/test/mpileup_test/result/Pat99T.recal.mpileup
 
 
samtools mpileup -E -uf /storage/home/Jieun/utils/ref/GRCh37.72.genome.chr.fa /storage2/Project/LungCancer_100PAT_exome/test/mpileup_test//ln/Pat08T.recal.bam > /storage2/Project/LungCancer_100PAT_exome/test/mpileup_test//result//Pat08T.recal.mpileup
bcftools view -cg /storage2/Project/LungCancer_100PAT_exome/test/mpileup_test//result/Pat08T.recal.mpileup > /storage2/Project/LungCancer_100PAT_exome/test/mpileup_test//result/Pat08T.vcf


samtools mpileup -f /storage/home/Jieun/utils/ref/GRCh37.72.genome.chr.fa /storage2/Project/LungCancer_100PAT_exome/Pat99T.recal.bam  > /storage2/Project/LungCancer_100PAT_exome/test/mpileup_test/result/Pat99T.recal.mpileup
