import os, glob
Respath="/storage/home/mglee/LAML_fish/map_fusion/1.RUNX1_X1T1/pos_res/"
fileP=glob.glob("%s/1.BAM/*mapped.bam"%Respath)
for item in fileP:
	dd=item.split("/")[10].split(".mapped.bam")[0]
	print dd
	neg=os.popen("samtools view %s.mapped.bam cut -f 3,6| sort |uniq -c| grep RUNX1_RUNX1T1"%(dd))
	reads = neg.read().split("\n")
	for read in reads:
		print read
