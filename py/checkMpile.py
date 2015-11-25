import os,glob
inf=glob.glob("/storage3/Project/mglee/LAML_fish/4.all_EML4ALK/neg/4.mpile/*.mpileup")
ouf=open("/home/ercsb/work/LUADTrans/allexon/Neg_exist.txt","w")
for filen in inf:
	f=open(filen)
	for line in f:
		
		readLength=line.split("\t")[0].split("_")[1].split("/")[1]
		exist=line.split("\t")[1]
		if int(exist) >= int(readLength):
			ouf.write("%s\t%s"%(filen,line))
			print "exist!!"
			print filen, line
			
