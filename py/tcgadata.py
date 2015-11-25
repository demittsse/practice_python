import os, glob

firpath="/storage/home/mglee/Raw_TCGA/CESC/"
outpath=firpath
chf=glob.glob("%s*.fastq"%firpath)
inf=open("/storage/home/mglee/Raw_TCGA/CESC/sh/list.txt")
legacy=[]; filename=[]; analysis=[] ; Tdict=dict()
for line in inf:
	if "<analysis_id>" in line: 
		analysisL=line.split("</analysis_id>")[0].replace("<analysis_id>","")
		analysis.append(analysisL)
	if "<filename>" in line: 
		#filenameL=line.split(".")[2].split(".tar.gz")[0]
		filenameL=line.split(".")[0].split("\t\t\t\t<filename>")[1]
		filename.append(filenameL)
	if "<legacy_sample_id>" in line: 
		legacyL=line.split("<legacy_sample_id>")[1].split("-")[0:5]
		legacyLi = "-".join(legacyL)+linenum
		if legacy
		legacy.append(legacyLi)
		Tdict[filenameL]=legacyLi 

for item in chf:
	fastq="_".join(item.split("/")[6].split("_")[0:5])
	level=str(int(item.split("/")[6].split("_")[5].split("L")[1]))
	pairn=item.split("/")[6].split("_")[6].split(".fastq")[0]
	
	try: print "ln -s %s %s_%s_%s.fastq"%(item, outpath,Tdict[fastq],level,pairn)
	except: print fastq
	#os.system("ln -s %s %s_%s_%s.fastq"%(item, outpath,Tdict[fastq],level,pairn))




UNCID_2561268.f99240d0-32ea-438a-b350-862202b18a30.140416_UNC11-SN627_0353_BC42B0ACXX_2_CAGATC.tar.gz
140513_UNC15-SN850_0364_AC4DVGACXX_ATGTCA_L007_2.fastq
140513_UNC15-SN850_0364_AC4DVGACXX_7_ATGTCA
'\t\t<legacy_sample_id>TCGA-VS-A8QM-01A-11R-A37O-07</legacy_sample_id>'
121011_UNC13-SN749_0197_AD16K1ACXX_2_ACAGTG': 'TCGA-EK-A3GM-01A
