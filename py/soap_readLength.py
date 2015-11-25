import os, glob

inputdir="/storage/home/mglee/Raw_TCGA/CESC/ln_CESC/"
listdir="/storage/home/mglee/Soap_TCGA/13.CESC/01.list/"
fircol= inputdir.split("/")[-3]
seccol= inputdir.split("/")[-2]
inf1=glob.glob("%sTCGA*_1.fastq"%inputdir)

for line in inf1:
	count= os.popen("head -n2 %s | tail -n1 |awk '{print length($1)}'"%(line))
	reads = count.read().split("\n")[0]
	sampleid = line.split("/")[7].split("_")[0]
	ouf=open("%s%s.txt"%(listdir,sampleid),"w")
	ouf.write("%s\t%s\t%s\t%s"%(fircol, seccol, sampleid, reads))
	
