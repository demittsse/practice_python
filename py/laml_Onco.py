import os,glob 

Tophat="/storage3/Project/mglee/programs/tophat-2.0.14.Linux_x86_64/tophat"
shdir="/storage3/Project/mglee/LAML_fish/oncofuse/shdir"
oncofuse="java -Xmx1G -jar /home/ercsb/oncofuse-1.0.9b1/Oncofuse.jar /storage3/Project/mglee/LAML_fish/result/"
DoneL=[]
# wwn=0;stop=3have to run
inf=glob.glob("/storage3/Project/mglee/LAML_fish/result/tophat_TCGA*/fusions.out")
Done=glob.glob("/storage3/Project/mglee/LAML_fish/oncofuse/shdir/*.sh")
for item in Done:
	att=item.split("tophat_")[1].split(".")[0]	
	if att not in DoneL:
		DoneL.append(att)
	

#l=0 ; wwn=200 ;stop=210
for line in inf: 
#	l+=1
#	if l <=wwn : continue
#	if l > stop  : continue 
	sampleid= line.split("/")[6]
	if sampleid in DoneL:
		continue
	print sampleid, len(sampleid)
	out="%s/%s.sh"%(shdir,sampleid)
	os.system("echo \#! \/bin\/bash  > %s"%(out))
	os.system('''echo %s/%s/fusions.out tophat AVG %s/result/%s.txt >> %s'''%(oncofuse,sampleid,shdir,sampleid,out))
	os.system("chmod 755 %s"%out)
	os.system("cd %s"%shdir)
	os.system("%s/./%s.sh"%(shdir,sampleid))

##Exception in thread "main" java.io.FileNotFoundException: /storage3/Project/mglee/LAML_fish/oncofuse/shdir/result/tophat_TCGA-AB-2817-03A_5.txt (그런 파일이나 디렉터리가 없습니다)
