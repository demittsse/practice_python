import string,sys,os,re,glob,time
from datetime import date
today=date.today()


#flist=glob.glob('/storage3/Project/mglee/TCGA_SOAP/10.LUAD/13.result_LUAD/UNCID_[0-9][0-9][0-9][0-9][0-9][0-9][0-9]/final_fusion_genes/LUAD/LUAD.final.Fusion.specific.for.trans')
flist=glob.glob('/storage3/Project/mglee/lymphoma/SOAP/result/S*/final_fusion_genes/GBM/LUAD.final.Fusion.specific.for.trans')
print flist
print len(flist)

outf=open('lymphoma'+str(today),'w')
for f in flist:
	inf=open(f,'r')
	pat=f.split('/')[7]
	print pat 
	while 1:
		line=inf.readline()
		if not line: break
		if "up_gene" in line: continue
		if line[0:5]!='Hgene':
			outf.write(pat+'\t'+line)
			outf.flush()
