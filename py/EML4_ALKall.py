import os, glob

gtfPath="/storage/home/mglee/LAML_fish/map_fusion/hg19.gtf" ## 1. write gtf path
nibPath="/storage/home/mglee/LAML_fish/map_fusion/" ## 2. write nibfrag path
chrFaPath="/storage/home/mglee/LAML_fish/map_fusion/" ## 2. put chr.fa path
HNMID="NM_001145076" ## 3. put Head NMID
TNMID="NM_004304" ## 4. put Tail NMID
HGname="EML4" ## 5. put Head Gene name
TGname="ALK" ## 6. put Tail Gene name
FGname=HGname+"_"+TGname

genedir="/storage/home/mglee/LAML_fish/map_fusion/5.All%s/"%(FGname)
Fadir="/storage/home/mglee/LAML_fish/map_fusion/5.All%s/Fa/"%(FGname)
fusout="%s/%s_%s_merge.fa"%(Fadir,HGname,TGname)
#os.system("mkdir %s"%genedir)
#os.system("mkdir %s"%Fadir)
"""
Hgtf=[];Tgtf=[]
gtf=open(gtfPath)
Hstart_codon="";Hstop_codon="";Tstart_codon="";Tstop_codon="";
Hchr="";Tchr=""
for line in gtf:
	if HNMID in line:
		if "exon" in line:
			llsp1=line.split("\t")[3]; rlsp1=line.split("\t")[4] ; joinlsp1=str(int(llsp1)+1)+" "+str(int(rlsp1)+1)
			Hgtf.append(joinlsp1)
			Hchr=line.split("\t")[0] ;
		if "start_codon" in line: Hstart_codon=line.split("\t")[3]
		if "stop_codon" in line: Hstop_codon=line.split("\t")[3]
	
	if TNMID in line:
		if "exon" in line:
			llsp2=line.split("\t")[3]; rlsp2=line.split("\t")[4] ;  joinlsp2=str(int(llsp2)+1)+" "+str(int(rlsp2)+1)
			Tgtf.append(joinlsp2)
			Tchr=line.split("\t")[0]
		if "start_codon" in line: Tstart_codon=line.split("\t")[3]
		if "stop_codon" in line: Tstop_codon=line.split("\t")[3]
	

if int(Hstart_codon)> int(Hstop_codon):
	Hgtf=sorted(Hgtf, reverse=True)
	print "Head reverse"
else : Hgtf=sorted(Hgtf)

if int(Tstart_codon)> int(Tstop_codon):
	Tgtf=sorted(Tgtf, reverse=True)
	print "Tail reverse"
else : Tgtf=sorted(Tgtf)

for H1exonNum in range(1,len(Hgtf)-1):
	H2exonNum=H1exonNum+1
	head1fa="%s/%s_exon%s.fa"%(Fadir,HGname,str(H1exonNum))
	head2fa="%s/%s_exon%s.fa"%(Fadir,HGname,str(H2exonNum))
	os.system("%s./nibFrag -upper -name=%s_exon%s %s/%s.fa.nib %s + %s" %(nibPath, HGname, str(H1exonNum), chrFaPath, Hchr, Hgtf[H1exonNum-1],head1fa))
	os.system("%s./nibFrag -upper -name=%s_exon%s %s/%s.fa.nib %s + %s" %(nibPath, HGname, str(H2exonNum), chrFaPath,Hchr, Hgtf[H2exonNum-1],head2fa))

for T1exonNum in range(1,len(Tgtf)-1):
	T2exonNum=T1exonNum+1 
	tail1fa="%s/%s_exon%s.fa"%(Fadir,TGname,str(T1exonNum))
	tail2fa="%s/%s_exon%s.fa"%(Fadir,TGname,str(T2exonNum))
	os.system("%s./nibFrag -upper -name=%s_exon%s %s/%s.fa.nib %s + %s" %(nibPath, TGname, str(T1exonNum), chrFaPath, Tchr,Tgtf[T1exonNum-1],tail1fa))
	os.system("%s./nibFrag -upper -name=%s_exon%s %s/%s.fa.nib %s + %s" %(nibPath, TGname, str(T2exonNum), chrFaPath, Tchr, Tgtf[T2exonNum-1],tail2fa))
"""
import os, glob
HGname="EML4" ## 5. put Head Gene name
TGname="ALK" ## 6. put Tail Gene name
FGname=HGname+"_"+TGname
Fadir=genedir="/home/ercsb/work/LUADTrans/allexon/Fa/"
def extractFA(inpath):
	inf=open(inpath)
	out=[]
	for line in inf:
		if ">" in line:continue
		out.append(line.split("\n")[0])
	outfa="".join(out)
	return outfa
	

Hdict=dict(); Tdict=dict()
Hinf=glob.glob("%s%s*.fa"%(Fadir,HGname))
hlinenum=0
for hin in Hinf:
	hlinenum+=1
	#Nstr= hin.split("/")[8].split(".fa")[0]
	Nstr= hin.split("/")[7].split(".fa")[0]
	Hdict[Nstr]=extractFA(hin)
	

Tinf=glob.glob("%s%s*.fa"%(Fadir,TGname))
Tlinenum=0
for Tin in Tinf:
	Tlinenum+=1
	#N2str= Tin.split("/")[8].split(".fa")[0]
	N2str= Tin.split("/")[7].split(".fa")[0]
	Tdict[N2str]=extractFA(Tin)
	print N2str,Tlinenum

oufname="%s/modRef.fa"%genedir
#ouf=open(oufname,"w")
Total=dict()
for hkey,hvalue in Hdict.items():
	for tkey,tvalue in Tdict.items():
		#fircol=">%s/%s_%s/%s\n"%(hkey.replace("exon",""),len(str(hvalue)),tkey.replace("exon",""),len(str(tvalue)))
		#seccol="%s%s\n"%(hvalue,tvalue)
		fircol="%s/%s_%s/%s"%(hkey.replace("exon",""),len(str(hvalue)),tkey.replace("exon",""),len(str(tvalue)))
		seccol="%s%s\n"%(hvalue,tvalue)
		Total[fircol]=seccol
		#ouf.write(fircol)
		#ouf.write(seccol)
		#ouf.write("\n")

		#Total[fircol]=seccol

ouf.close()
