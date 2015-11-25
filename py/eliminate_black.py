""">>> ts=set(toplist)-set(soaplist)
>>> set(toplist)-ts
set(['RUNX1_RUNX1T1', 'PML_RARA', 'HLA-G_HLA-C'])
>>> sc=set(soaplist)-set(scanlist)
>>> set(soaplist)-sc
set([])
>>> ct=set(scanlist)-set(toplist)
>>> set(scanlist)-ct
set([])

sc2=set(soaplist2)-set(scanlist2)
set(soaplist2)-sc2
"""

black=open("/storage3/Project/ChimerDB3/Black2Gold/black_01.txt")
blacklist=[]
for a in black:
	head=a.split("_")[0]
	tail=a.split("_")[1].split("\n")[0]
	blacklist.append("%s_%s"%(head,tail))
	blacklist.append("%s_%s"%(tail,head))
#print blacklist
geneset=['NSD1_NUP98', 'NUP98_NSD1', 'ABL1_BCR', 'RARA_PML', 'MECOM_RPN1', 'HNRNPH1_ERG', 'MLL_ELL', 'NCOR2_SCARB1', 'CDC73_FAM172A', 'MLLT10_PICALM', 'PICALM_MLLT10', 'PML_RARA', 'RUNX1_RUNX1T1', 'DNMT3B_MDM4', 'PRMT1_TLE6', 'MLL_MLLT10', 'DPM1_GRID1', 'RUNX1_MECOM', 'CHD1_MTOR']
test=[]
soapfusef=open("/home/ercsb/work/copynum/LAML_result.txt")
fusionscanf=open("/storage3/Project/fusiongene/result_TCGA/LAML_FusionScan_candidate_result.txt")
tophatf=open("/storage/home/mglee/Tophat/LAML/tophatfusion_out/result.txt")
pradaf=open("/home/ercsb/work/Result/LAML/practice_python/LAML_PRADA.csv")
#topout=open("/home/ercsb/work/Result/LAML/tophatLAML.txt","w")
#Soapout=open("/home/ercsb/work/Result/LAML/soapLAML.txt","w")
total=[]; toplist=[];soaplist=[];scanlist=[];pradalist=[];toplist2=[];soaplist2=[];scanlist2=[];pradalist2=[]

for top in tophatf:
	thead=top.split("\t")[1]
	ttail=top.split("\t")[4]
	tgeneP="%s_%s"%(thead,ttail)
	tgeneP2="%s_%s"%(ttail,thead)
	total.append(tgeneP)
	if tgeneP not in toplist:
		toplist.append(tgeneP)
	if tgeneP2 not in toplist2:
		toplist2.append(tgeneP2)
	#print tgeneP
	#if tgeneP in blacklist:
	#	print "black:%s"%tgeneP

blacksoap=[]
for soap in soapfusef:
	shead=soap.split("\t")[1]
	stail=soap.split("\t")[8]
	sgeneP="%s_%s"%(shead,stail)
	sgeneP2="%s_%s"%(stail,shead)
	#print sgeneP
	if sgeneP in blacklist:
		if sgeneP not in blacksoap:
			blacksoap.append(sgeneP)
	#total.append(sgeneP)
	if sgeneP not in soaplist:
		soaplist.append(sgeneP)
	if sgeneP2 not in soaplist2:
		soaplist2.append(sgeneP2)



for fus in fusionscanf:
	chead=fus.split("\t")[2]
	ctail=fus.split("\t")[6]
	cgeneP="%s_%s"%(chead,ctail)
	cgeneP2="%s_%s"%(ctail,chead)
	#total.append(sgeneP)
	if cgeneP not in scanlist:
		scanlist.append(cgeneP)
	if cgeneP2 not in scanlist2:
		scanlist2.append(cgeneP2)

for pyprada in pradaf:
	colP=pyprada.split(",")[3].replace('"','').split("__")
	pgeneP="%s_%s"%(colP[0],colP[1])
	pgeneP2="%s_%s"%(colP[1],colP[0])
	if pgeneP not in pradalist:
		pradalist.append(pgeneP)
		
	if pgeneP2 not in pradalist2:
		pradalist2.append(pgeneP2)
	if pgeneP in geneset:
		if pyprada not in test:
			test.append(pyprada)

for t in test : print  t
from itertools import combinations

data = dict(
	tophat = set(list(toplist)),
	soap= set(list(soaplist)),
	fusionscan= set(list(scanlist)),
	prada = set(list(pradalist)),)

variations = {}

for i in range(len(data)):
	for v in combinations(data.keys(),i+1):
		vsets = [ data[x] for x in v ]
		variations[tuple(sorted(v))] = reduce(lambda x,y: x.intersection(y), vsets)

for k,v in sorted(variations.items(),key=lambda x: (len(x[0]),x[0])):
	print "%r:%r\n\t%r" % (k,len(v),v)

