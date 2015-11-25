./igvtools count -w 50 --strands read /storage3/Project/mglee/LAML_fish/4.all_EML4ALK/neg/3.sorted/TCGA-67-6215-01A_1.sorted.bam stdout /home/ercsb/work/LUADTrans/allexon/EML4_ALK.fa
./igvtools count --query EML4_1/298_ALK_12/162:288-318 /storage3/Project/mglee/LAML_fish/4.all_EML4ALK/neg/3.sorted/TCGA-67-6215-01A_1.sorted.bam stdout /home/ercsb/work/LUADTrans/allexon/EML4_ALK.fa

	
import os, glob,time
reflist=open("/home/ercsb/work/LUADTrans/allexon/reflist.txt")
for line in reflist:
	
	chrom=line.split(">")[1].split("\n")[0]
	print chrom
	comline= "python posexcIGV.py %s "%(chrom)
	print comline
	os.system(comline)
	time.sleep(3)

import sys, os, glob,time
inf1=glob.glob("/storage3/Project/mglee/LAML_fish/4.all_EML4ALK/3.sorted/*.sorted.bam")
#inf1=glob.glob("/storage3/Project/mglee/LAML_fish/4.all_EML4ALK/neg/3.sorted/*.sorted.bam")

for item in inf1:
	chrom=sys.argv[1]
	rstand=int(chrom.split("_")[1].split("/")[1])
	rStart=rstand-10
	rEnd=rstand+10
	
	comline= "~/work/transcript/IGVTools/./igvtools count --query %s:%s-%s %s stdout /home/ercsb/work/LUADTrans/allexon/EML4_ALK.fa"%(chrom, rStart, rEnd, item)
	print comline
	#os.system(">/home/ercsb/work/LUADTrans/allexon/IGVresult/%s.txt"%(chrom.replace("/","#")))
	os.system(comline)

filename=sys.argv[1].replace("/","#")
Filename="/home/ercsb/work/LUADTrans/allexon/IGVresult/P_%s.txt"%filename 
sys.stdout = open(Filename, 'w')
