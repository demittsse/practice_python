import string, os, sys, time, glob

gp='EML4-ALK'
hchr='chr2'
hbp=42522656
tchr='chr2'
tbp=29446394

inf2 =open('/storage/home/iamlife/fusionscan/making_depth_graph/predict_from_depth/refGene.txt','r')

gpdic={}
gpdic2={}
glist=[]
gplist=[]
gp_pat_bp_dic={}
gp_chr_dic={}

gps = gp.split('-')
gplist.append(gp)
hg=gps[0]
tg=gps[1]
gp_pat_bp_dic[hg]=hbp
gp_pat_bp_dic[tg]=tbp
gp_chr_dic[hg]=hchr
gp_chr_dic[tg]=tchr
if hg not in glist:
	glist.append(hg)
if tg not in glist:
	glist.append(tg)


gene_str_dic={}
while 1:
	line= inf2.readline()
	if not line: break
        lines = line[:-1].split('\t')

        ref=lines[1]
	chr=lines[2]
	strand=lines[3]
	exstart_list=lines[9].split(',')[:-1]
	exend_list=lines[10].split(',')[:-1]
	gene=lines[12]
	gene_str_dic[gene]=strand
	if gene in glist:
		if gpdic.has_key(gene):
			list=gpdic[gene]
			list2=gpdic2[gene]
                	for ex in range(len(exstart_list)):
                        	EX=int(exstart_list[ex])
				EX2=int(exend_list[ex])
				if EX not in list:
					list.append(EX)
				if EX2 not in list2:
					list2.append(EX2)
			gpdic[gene]=list
			gpdic2[gene]=list2
		else:
			list=[]
			list2=[]
			for ex in range(len(exstart_list)):
                                EX=int(exstart_list[ex])
				EX2=int(exend_list[ex])
                                if EX not in list:
                                        list.append(EX)
				if EX2 not in list2:
					list2.append(EX2)
                        gpdic[gene]=list
			gpdic2[gene]=list2




#for gp in gplist:
	
#patlist=glob.glob('/storage/home/iamlife/lymphoma/fq_dir/PE_fq_dir/dir2*_1.fastq')
grepos=os.popen('ls /storage/home/iamlife/lymphoma/fq_dir/tophat_result/tophat_DLBCL_* -d')
patlist=[]
for line in grepos.xreadlines():
        if line not in patlist:
                patlist.append(line[:-1])
"""
print patlist
for pat2 in patlist:
	pat=pat2.split('/')[-1].split('tophat_DLBCL_')[1]
	print pat2
	print pat
	if 1==1:
		gps=gp.split('-')
		hg=gps[0]
		tg=gps[1]
                hchr=gp_chr_dic[hg]
                tchr=gp_chr_dic[tg]
		hlist=gpdic[hg]
		hlist2=gpdic2[hg]
		tlist=gpdic[tg]
		tlist2=gpdic2[tg]
		hlist.sort()
		hlist2.sort()
		tlist.sort()
		tlist2.sort()
		hmin=hlist[0]
		hmax=hlist2[-1]
		tmin=tlist[0]
		tmax=tlist2[-1]

		hstrand=gene_str_dic[hg]
		tstrand=gene_str_dic[tg]
		print 'tstrand='+tstrand
                hbp=gp_pat_bp_dic[hg]
                tbp=gp_pat_bp_dic[tg]

		
                hbploci=0
                tbploci=0
                hflag='f'
                tflag='f'

		Hmin=10000000000
		Hmax=0
		cc=0
		all_xlist1=[]
		list_for_1=[]
		list_for_2=[]
		h1list=[]
		"""
                gpout=open(hg+'_depth_graph.txt','w')
		hT=open('EML4_depth_in_'+pat+'.sorted','r')
		h1=0
		h1_=0
		while 1:
			cc+=1
			all_xlist1.append(str(cc))
			line=hT.readline()
			if not line: break
			lines=line[:-1].split('\t')
			exon_nt=lines[3]
			exon_nt2=lines[4]
			exbd=int(lines[1])
			exbd2=int(lines[2])
			int_exon_nt=int(exon_nt2)
			h1list.append(exon_nt2)
                        if hflag=='f' and (hbp-6<=exbd) and (exbd<=hbp+6):
                                hbploci=cc
                                hflag='t'
                        if hflag=='f' and (hbp-6<=exbd2) and (exbd2<=hbp+6):
                                hbploci=cc

			if int_exon_nt<Hmin:
				Hmin=int_exon_nt
			if Hmax<int_exon_nt:
				Hmax=int_exon_nt
			nu=lines[3]
			h1+=int(exon_nt2)
			if nu=='1':
				h1_=h1/cc
				list_for_1.append(cc)
				h1=0
				print h1_

		for h in range(len(h1list)):
			gpout.write(str(h)+'\t'+h1list[h]+'\n')
			gpout.flush()
			h+=1
		gpout.close()


		all_xlist1=all_xlist1[:-1]

		#print all_xlist1
		#print all_xlist1[:-1]
                tout=open(pat+'temp.py','w')
                totalw='import matplotlib\n'
                totalw+='matplotlib.use(\"Agg\")\n'
                totalw+='import pylab\n'
                totalw+='import numpy as n\n'
                totalw+='import matplotlib.mlab as mlab\n'
                totalw+='import matplotlib.pyplot as plt\n'
                totalw+='import matplotlib.legend as legend\n'
                totalw+='fig = plt.figure()\n'
                totalw+='fig.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)\n'
                totalw+='ax1 = fig.add_subplot(111)\n'

                totalw+='index = '+str(all_xlist1)+'\n'
                tout.write(totalw)
                tout.flush()

		list_for_1=list_for_1[1:]
		print list_for_1
		list_for_1_=[]
                totalw=''

		print 'before'
		if hstrand=='-':
			h1list.reverse()
			for fo in list_for_1:
				list_for_1_.append(len(all_xlist1)-fo)
                        totalw+='y1 = '+str(h1list)+'\n'
		else:
			list_for_1_=list_for_1
                        totalw+='y1 = '+str(h1list)+'\n'

                totalw+='ax1.plot(index,y1,color=\"red\")\n' # draw line type graph
		#totalw+='ax1.bar(index,y1,width=0.1,facecolor=\"red\")\n' # bar plot
                totalw+='index2 = '+str(list_for_1_)+'\n'

		print hstrand
		print 'after'
                for f in list_for_1_:
                        totalw+='ax1.axvline(x='+str(f)+'., color=\"c\",ls=\"dashed\")\n'
		list_for_1_.append(len(all_xlist1))
		f0=0
		
		ddd=[]
		for f2 in range(len(list_for_1_)):
			F2=list_for_1_[f2]
			f3=(F2+f0)/2
			ddd.append(f3)
			#print str(f3) + ' -- '+str(h4__[f2])
			#totalw+='ax1.plot(x='+str(f3)+',y='+str(h4__[f2])+',color=\"black\",ls=\"ro\")\n'
			f0=F2
		#totalw+='ax1.plot('+str(ddd)+','+str(h4__)+',\"ro\")\n'

                totalw+='ax1.set_title(\"Depth Graph for '+hg+'\")\n'
                totalw+='ax1.set_xlabel(\"mRNA nucleotide\\n(Dash line means exon boundary)\")\n'
                totalw+='ax1.set_ylabel(\"Depth\")\n'
		Hlen=len(all_xlist1)/10*7
                Hgap=Hmax-Hmin
                Hp=Hgap/10
		Hp2=Hgap/21

#                totalw+='ax1.annotate(\"S1109571\", xy=('+str(Hlen)+','+str(Hmax+1*Hp2)+'), color=\"black\", size=8, weight=\"bold\")\n'

		if hstrand=='-': 
			hbploci2=len(all_xlist1)-hbploci
		else:
			hbploci2=hbploci
		totalw+='ax1.annotate(\"BP\", xy=('+str(hbploci2)+',0), xytext=('+str(hbploci2)+',80), arrowprops=dict(facecolor=\"yellow\", shrink=0.02), horizontalalign
ment=\"center\", weight=\"bold\")\n'
                #totalw+='ax1.annotate(\"BP\", xy=('+str(hbploci2)+',300), xytext=('+str(hbploci2)+',400), arrowprops=dict(facecolor=\"yellow\", shrink=0.02), horizontala
lignment=\"center\", weight=\"bold\")\n'

                totalw+='fig.savefig(\"'+hg+'_depth_in_'+pat+'.png\")\n'


                tout.write(totalw)
                tout.flush()
                os.system('/share/apps/bin/python2.7 '+pat+'temp.py')

		"""
                Tmin=10000000000
                Tmax=0
                cc=0
                all_xlist1=[]
                h1list=[]
		list_for_1=[]
		list_for_2=[]
                gpout=open(tg+'_depth_graph.txt','w')
		print 'ALK_depth_in_'+pat+'.sorted'
                hT=open('ALK_depth_in_'+pat+'.sorted','r')
                h1=0
                h1_=0
                while 1:
                        cc+=1
                        all_xlist1.append(str(cc))
                        line=hT.readline()
                        if not line: break
                        lines=line[:-1].split('\t')
                        exon_nt=lines[3]
                        exon_nt2=lines[4]
                        exbd=int(lines[1])
                        exbd2=int(lines[2])
                        int_exon_nt=int(exon_nt2)
                        h1list.append(exon_nt2)
                        if tflag=='f' and (tbp-6<=exbd) and (exbd<=tbp+6):
                                tbploci=cc
                                tflag='t'
                        if tflag=='f' and (tbp-6<=exbd2) and (exbd2<=tbp+6):
                                tbploci=cc

                        if int_exon_nt<Tmin:
                                Tmin=int_exon_nt
                        if Tmax<int_exon_nt:
                                Tmax=int_exon_nt
                        nu=lines[3]
                        h1+=int(exon_nt2)
                        if nu=='1':
                                h1_=h1/cc
                                list_for_1.append(cc)
                                h1=0
                                print h1_

                for h in range(len(h1list)):
                        gpout.write(str(h)+'\t'+h1list[h]+'\n')
                        gpout.flush()
                        h+=1
                gpout.close()


                all_xlist1=all_xlist1[:-1]

                tout=open(pat+'temp.py','w')
                totalw='import matplotlib\n'
                totalw+='matplotlib.use(\"Agg\")\n'
                totalw+='import pylab\n'
                totalw+='import numpy as n\n'
                totalw+='import matplotlib.mlab as mlab\n'
                totalw+='import matplotlib.pyplot as plt\n'
                totalw+='import matplotlib.legend as legend\n'
                totalw+='fig = plt.figure()\n'
                totalw+='fig.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)\n'
                totalw+='ax1 = fig.add_subplot(111)\n'

                totalw+='index = '+str(all_xlist1)+'\n'
                tout.write(totalw)
                tout.flush()

                list_for_1=list_for_1[1:]
                print list_for_1
                list_for_1_=[]
                totalw=''

                print 'before'
                if tstrand=='-':
                        h1list.reverse()
                        for fo in list_for_1:
                                list_for_1_.append(len(all_xlist1)-fo)
                        totalw+='y1 = '+str(h1list)+'\n'
                else:
                        list_for_1_=list_for_1
                        totalw+='y1 = '+str(h1list)+'\n'

                totalw+='ax1.plot(index,y1,color=\"red\")\n'

                totalw+='index2 = '+str(list_for_1_)+'\n'

                print tstrand
                print 'after'
                for f in list_for_1_:
                        totalw+='ax1.axvline(x='+str(f)+'., color=\"c\",ls=\"dashed\")\n'
                list_for_1_.append(len(all_xlist1))
                f0=0

                ddd=[]
                for f2 in range(len(list_for_1_)):
                        F2=list_for_1_[f2]
                        f3=(F2+f0)/2
                        ddd.append(f3)
                        #print str(f3) + ' -- '+str(h4__[f2])
                        #totalw+='ax1.plot(x='+str(f3)+',y='+str(h4__[f2])+',color=\"black\",ls=\"ro\")\n'
                        f0=F2
#                totalw+='ax1.plot('+str(ddd)+','+str(h4__)+',\"ro\")\n'

                totalw+='ax1.set_title(\"Depth Graph for '+tg+'\")\n'
                totalw+='ax1.set_xlabel(\"mRNA nucleotide\\n(Dash line means exon boundary)\")\n'
                totalw+='ax1.set_ylabel(\"Depth\")\n'
                Tlen=len(all_xlist1)/10*7
                Tgap=Tmax-Tmin
                Tp=Tgap/10
                Tp2=Tgap/21
                #totalw+='ax1.annotate(\"S1109571\", xy=('+str(Tlen)+','+str(Tmax+1*Tp2)+'), color=\"black\", size=8, weight=\"bold\")\n'

                if tstrand=='-':
                        tbploci2=len(all_xlist1)-tbploci
                else:
                        tbploci2=tbploci
                totalw+='ax1.annotate(\"BP\", xy=('+str(tbploci2)+',0), xytext=('+str(tbploci2)+',80), arrowprops=dict(facecolor=\"yellow\", shrink=0.02), horizontalalign
ment=\"center\", weight=\"bold\")\n'
		print 'len c='+str(len(all_xlist1))
		print tbploci
		print tbploci2
                #totalw+='ax1.annotate(\"BP\", xy=('+str(tbploci2)+',250), xytext=('+str(tbploci2)+',330), arrowprops=dict(facecolor=\"yellow\", shrink=0.02), horizontala
lignment=\"center\", weight=\"bold\")\n'

                totalw+='fig.savefig(\"'+tg+'_depth_in_'+pat+'.png\")\n'


                tout.write(totalw)
                tout.flush()
                os.system('/share/apps/bin/python2.7 '+pat+'temp.py')


