inf=open("/home/ercsb/work/Result/LAML/practice_python/PSF75LAML.csv")
#ouf=open("/home/ercsb/work/Result/LAML/practice_python/PSF75LAML.tsv","w")
#ouf.write("Barcode\tGene\tValue\n")
rowD={};colD={}
rowLabel=[];colLabel=[]
for line in inf:
	if "Barcode" in line:continue 
	barcode=line.replace('"','').split(",")[1]
	S=line.replace('"','').split(",")[4];F=line.replace('"','').split(",")[5];P=line.replace('"','').split(",")[6]
	gene="_".join(line.replace('"','').split(",")[2:4])
	reverseg=gene.split("_")[1]+"_"+gene.split("_")[1]
	if barcode not in rowLabel:
		rowLabel.append(barcode)
	if reverseg and gene not in colLabel:
		colLabel.append(gene)
	for a in rowLabel:
		rowD[a]=rowLabel.index(a)+1
	for b in colLabel:
		colD[b]=colLabel.index(b)+1
	
	#try:print rowD[barcode],colD[gene]
	#except:print barcode, gene
	lines=line.split("\n")[0]
	if S=="Soapfuse" :
		r=2
		if F=="Fusionscan":
			r=4
			if P=="pyPRADA\n": 
				r=6
	row1="%s\t%s\t%s\n"%(rowD[barcode],colD[gene],r)
	print lines,row1
	#ouf.write(row1)
"""
	
p=[]
for line in inf:
	p.append('"'+"_".join(line.replace('"','').split(",")[2:4])+'"')
	print "[%s]" %",".join(p)


>>> colD
{'NSD1_NUP98': 1, 'DPM1_GRID1': 19, 'ABL1_BCR': 2, 'DNMT3B_MDM4': 15, 'RARA_PML': 3, 'RUNX1_RUNX1T1': 4, 'HNRNPH1_ERG': 5, 'PICALM_MLLT10': 6, 'POLR2A_FBN3': 7, 'CDC73_FAM172A': 8, 'MLLT10_PICALM': 9, 'CBFB_MYH11': 10, 'NUCB1_RUVBL2': 16, 'PML_RARA': 12, 'CHD1_MTOR': 21, 'SIK3_C11orf1': 13, 'BZW2_GUSB': 17, 'MLL_MLLT10': 18, 'BCR_ABL1': 11, 'RUNX1_MECOM': 20, 'TFG_GPR128': 14}
>>> rowD
{'TCGA-AB-3001-03A': 23, 'TCGA-AB-2886-03A': 10, 'TCGA-AB-2994-03A': 22, 'TCGA-AB-2875-03A': 9, 'TCGA-AB-2915-03A': 12, 'TCGA-AB-2938-03A': 28, 'TCGA-AB-2881-03A': 34, 'TCGA-AB-3007-03A': 24, 'TCGA-AB-2857-03A': 52, 'TCGA-AB-2844-03A': 48, 'TCGA-AB-2944-03A': 64, 'TCGA-AB-2872-03A': 56, 'TCGA-AB-2834-03A': 45, 'TCGA-AB-2832-03A': 43, 'TCGA-AB-2823-03A': 41, 'TCGA-AB-2950-03A': 19, 'TCGA-AB-2935-03A': 37, 'TCGA-AB-2918-03A': 36, 'TCGA-AB-2991-03A': 21, 'TCGA-AB-2819-03A': 3, 'TCGA-AB-3005-03A': 74, 'TCGA-AB-2842-03A': 47, 'TCGA-AB-3012-03A': 25, 'TCGA-AB-2870-03A': 33, 'TCGA-AB-2930-03A': 14, 'TCGA-AB-2911-03A': 59, 'TCGA-AB-2889-03A': 35, 'TCGA-AB-2897-03A': 57, 'TCGA-AB-2840-03A': 4, 'TCGA-AB-2856-03A': 7, 'TCGA-AB-2941-03A': 18, 'TCGA-AB-2937-03A': 15, 'TCGA-AB-2862-03A': 55, 'TCGA-AB-2803-03A': 39, 'TCGA-AB-2939-03A': 16, 'TCGA-AB-2980-03A': 65, 'TCGA-AB-2855-03A': 50, 'TCGA-AB-2901-03A': 27, 'TCGA-AB-2806-03A': 1, 'TCGA-AB-2985-03A': 67, 'TCGA-AB-2942-03A': 38, 'TCGA-AB-2858-03A': 8, 'TCGA-AB-2999-03B': 72, 'TCGA-AB-2904-03A': 11, 'TCGA-AB-2998-03A': 70, 'TCGA-AB-2849-03A': 5, 'TCGA-AB-2828-03A': 31, 'TCGA-AB-2931-03A': 61, 'TCGA-AB-2982-03B': 20, 'TCGA-AB-2846-03A': 32, 'TCGA-AB-2848-03A': 49, 'TCGA-AB-2814-03A': 2, 'TCGA-AB-2817-03A': 26}
"""
