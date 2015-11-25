\#! \/bin\/bash
prada="/storage/home/mglee/source/pyPRADA_1.2/"
refdir="/storage/home/mglee/source/ref/Prada/PRADA-reference-hg19/"
sampleid=$1


#2_e1_1 $sampleid.end1.fastq $sampleid.end1.sai
/$prada/tools/bwa-0.5.7-mh/bwa aln -t 12 $refdir/Ensembl64.transcriptome.plus.genome.fasta $sampleid.end1.fastq > $sampleid.end1.sai

#2_e1_2 $sampleid.end1.sai & $sampleid.end1.fastq $sampleid.end1.sam
/$prada/tools/bwa-0.5.7-mh/bwa samse -s -n 100 $refdir/Ensembl64.transcriptome.plus.genome.fasta $sampleid.end1.sai $sampleid.end1.fastq > $sampleid.end1.sam

#2_e1_3 $sampleid.end1.sam $sampleid.end1.bam
/$prada/tools/samtools-0.1.16/samtools view -bS -o $sampleid.end1.bam $sampleid.end1.sam

#2_e1_4 $sampleid.end1.bam $sampleid.end1.sorted.bam
/$prada/tools/samtools-0.1.16/samtools sort -on -m 1000000000 $sampleid.end1.bam $sampleid.end1.sorted

# 2_e2_1 sampelid.end2.fastq $sampleid.end2.sai
/$prada/tools/bwa-0.5.7-mh/bwa aln -t 12 $refdir/Ensembl64.transcriptome.plus.genome.fasta $sampleid.end2.fastq > $sampleid.end2.sai

#2_e2_2 $sampleid.end2.sai & $sampleid.end2.fastq $sampleid.end2.sam
/$prada/tools/bwa-0.5.7-mh/bwa samse -s -n 100 $refdir/Ensembl64.transcriptome.plus.genome.fasta $sampleid.end2.sai $sampleid.end2.fastq > $sampleid.end2.sam

# 2_e2_3 $sampleid.end2.sam $sampleid.end2.bam
/$prada/tools/samtools-0.1.16/samtools view -bS -o $sampleid.end2.bam $sampleid.end2.sam

#2_e2_4 $sampleid.end2.bam $sampleid.end2.sorted.bam
/$prada/tools/samtools-0.1.16/samtools sort -n -m 1000000000 $sampleid.end2.bam $sampleid.end2.sorted

#3_e1_1 $sampleid.end1.sorted.bam $sampleid.end1.remapped.bam
java -Djava.io.tmpdir=tmp/ -cp /$prada/tools/GATK//RemapAlignments.jar -Xmx8g org.broadinstitute.cga.tools.gatk.rna.RemapAlignments M=$refdir/Ensembl64.transcriptome.plus.genome.map IN=$sampleid.end1.sorted.bam OUT=$sampleid.end1.remapped.bam R=$refdir/Homo_sapiens_assembly19.fasta REDUCE=TRUE


#3_e1_2 $sampleid.end1.remapped.bam $sampleid.end1.remapped.sorted.bam
/$prada/tools/samtools-0.1.16/samtools sort -n -m 1000000000 $sampleid.end1.remapped.bam $sampleid.end1.remapped.sorted

#3_e2_1 $sampleid.end2.sorted.bam $sampleid.end2.remapped.bam
java -Djava.io.tmpdir=tmp/ -cp /$prada/tools/GATK//RemapAlignments.jar -Xmx8g org.broadinstitute.cga.tools.gatk.rna.RemapAlignments M=$refdir/Ensembl64.transcriptome.plus.genome.map IN=$sampleid.end2.sorted.bam OUT=$sampleid.end2.remapped.bam R=$refdir/Homo_sapiens_assembly19.fasta REDUCE=TRUE

#3_e2_2 $sampleid.end2.remapped.bam $sampleid.end2.remapped.sorted.bam
/$prada/tools/samtools-0.1.16/samtools sort -n -m 1000000000 $sampleid.end2.remapped.bam $sampleid.end2.remapped.sorted 
#rm -f $sampleid.end2.sorted.bam
#rm -f $sampleid.end2.remapped.bam

#4_1$sampleid.end1.remapped.sorted.bam &$sampleid.end2.remapped.sorted.bam $sampleid.paired.bam
java -Djava.io.tmpdir=tmp/ -Xmx8g -jar /$prada/tools/GATK//PairMaker.jar IN1=$sampleid.end1.remapped.sorted.bam IN2=$sampleid.end2.remapped.sorted.bam OUTPUT=$sampleid.paired.bam TMP_DIR=tmp/ 
#rm -f $sampleid.end1.remapped.sorted.bam
#rm -f $sampleid.end2.remapped.sorted.bam

#4_2 $sampleid.paired.bam $sampleid.paired.sorted.bam
/$prada/tools/samtools-0.1.16/samtools sort -m 1000000000 $sampleid.paired.bam $sampleid.paired.sorted
#rm -f $sampleid.paired.bam
##5 $sampleid.paired.sorted.bam $sampleid.withRG.paired.sorted.bam
java -Xmx8g -jar /$prada/tools/Picard//AddOrReplaceReadGroups.jar I=$sampleid.paired.sorted.bam O=$sampleid.withRG.paired.sorted.bam RGLB=$sampleid RGPL=illumina RGPU=$sampleid RGSM=$sampleid
#rm -f $sampleid.paired.sorted.bam

##6_1 $sampleid.withRG.paired.sorted .bam $sampleid.withRG.paired.sorted.bam.bai
/$prada/tools/samtools-0.1.16/samtools index $sampleid.withRG.paired.sorted.bam $sampleid.withRG.paired.sorted.bam $sampleid.orig.csv
java -Xmx8g -jar /$prada/tools/GATK//GenomeAnalysisTK.jar -l INFO -R $refdir/Homo_sapiens_assembly19.fasta --default_platform illumina --knownSites $refdir/dbsnp_135.b37.vcf -I $sampleid.withRG.paired.sorted.bam --downsample_to_coverage 10000 -T CountCovariates -cov ReadGroupCovariate -cov QualityScoreCovariate -cov CycleCovariate -cov DinucCovariate -nt 12 -recalFile $sampleid.orig.csv
#6_2 $sampleid.withRG.paired.sorted .bam & $sampleid.orig.csv $sampleid.withRG.GATKRecalibrated.bam
java -Xmx8g -jar /$prada/tools/GATK//GenomeAnalysisTK.jar -l INFO -R $refdir/Homo_sapiens_assembly19.fasta --default_platform illumina -I $sampleid.withRG.paired.sorted.bam -T TableRecalibration --out $sampleid.withRG.GATKRecalibrated.bam -recalFile $sampleid.orig.csv
#rm -f $sampleid.withRG.paired.sorted.bam
##7$sampleid.withRG.GATKRecalibrated.bam $sampleid.withRG.GATKRecalibrated.flagged.bam
java -Xmx8g -jar /$prada/tools/Picard//MarkDuplicates.jar I=$sampleid.withRG.GATKRecalibrated.bam O=$sampleid.withRG.GATKRecalibrated.flagged.bam METRICS_FILE=$sampleid.Duplicates_metrics.txt VALIDATION_STRINGENCY=SILENT TMP_DIR=tmp/$sampleid.withRG.GATKRecalibrated.flagged.bam $sampleid.withRG.GATKRecalibrated.flagged.bam.bai
/$prada/tools/samtools-0.1.16/samtools index $sampleid.withRG.GATKRecalibrated.flagged.bam 

#rm -f $sampleid.withRG.GATKRecalibrated.bam
#8 $sampleid.withRG.GATKRecalibrated.flagged.bam $sampleid/
java -Xmx8g -jar /$prada/tools/RNA-SeQC_v1.1.7.jar -ttype 2 -t $refdir/Homo_sapiens.GRCh37.64.gtf -r $refdir/Homo_sapiens_assembly19.fasta -s '$sampleid|$sampleid.withRG.GATKRecalibrated.flagged.bam|Disc' -o $sampleid/ 
