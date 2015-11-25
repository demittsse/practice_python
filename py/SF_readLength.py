import os, glob

inputdir="/storage/home/mglee/Raw_TCGA/CHOL/ln_CHOL/"
listdir="/storage/home/mglee/Soap_TCGA/15.CHOL/01.list/"
os.system("mkdir %s"%listdir)
fircol= inputdir.split("/")[-3]
seccol= inputdir.split("/")[-2]
inf1=glob.glob("%sTCGA*_1.fastq"%inputdir)

for line in inf1:
	count= os.popen("head -n2 %s | tail -n1 |awk '{print length($1)}'"%(line))
	reads = count.read().split("\n")[0]
	sampleid = line.split("/")[7].split("_1.fastq")[0]
	ouf=open("%s%s.txt"%(listdir,sampleid),"w")
	ouf.write("%s\t%s\t%s\t%s"%(fircol, seccol, sampleid, reads))
	
import os, glob

inputdir="/storage/home/mglee/Raw_TCGA/ACC/"
listdir="/storage/home/mglee/Soap_TCGA/14.ACC/01.list/"
fircol= inputdir.split("/")[-3]
seccol= inputdir.split("/")[-2]
inf1=glob.glob("%sTCGA*_1.fastq"%inputdir)

for line in inf1:
	count= os.popen("head -n2 %s | tail -n1 |awk '{print length($1)}'"%(line))
	reads = count.read().split("\n")[0]
	sampleid = line.split("/")[6].split("_1.fastq")[0]
	ouf=open("%s%s.txt"%(listdir,sampleid),"w")
	ouf.write("%s\t%s\t%s\t%s"%(fircol, seccol, sampleid, reads))
	
