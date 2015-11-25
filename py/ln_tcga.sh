#!/bin/sh
cancer="BLCA"
#$ -N TCGA_$cancer
#$ -e /storage/home/mglee/Raw_TCGA/logs
#$ -o /storage/home/mglee/Raw_TCGA/logs

mkdir /storage/home/mglee/Raw_TCGA/$cancer
echo "link"
ls /storage/Project/TCGA/$cancer/fasta/*.gto | cut -d'.' -f1 | cut -d'/' -f7 | uniq | while read line; do
echo "$line"
TCGA=`cat /storage/Project/TCGA/$cancer/list.txt | grep -A 3 $line | grep 'legacy_sample_id' | cut -d'>' -f2 | cut -d'-' -f 1,2,3,4`;
if [ -e /storage/Project/dbGap/TCGA/$cancer/ln_fasta/${TCGA}_1_1.fastq ]
then
ln -s /storage/Project/TCGA/$cancer/fasta/$line/*_1.fastq /storage/home/mglee/Raw_TCGA/$cancer/${TCGA}_2_1.fastq
ln -s /storage/Project/TCGA/$cancer/fasta/$line/*_2.fastq /storage/home/mglee/Raw_TCGA/$cancer/${TCGA}_2_2.fastq
else
ln -s /storage/Project/TCGA/$cancer/fasta/$line/*_1.fastq /storage/home/mglee/Raw_TCGA/$cancer${TCGA}_1_1.fastq
ln -s /storage/Project/TCGA/$cancer/fasta/$line/*_2.fastq /storage/home/mglee/Raw_TCGA/$cancer/${TCGA}_1_2.fastq
fi
echo "end"
done


5TB  ACC  BLCA  CESC  CHOL  DLBC  ESCA  HNSC  KIRC  LAML  LGG  MESO  OV  PCPG  PRAD  READ  SARC  SKCM  STAD  THYM  UCS  UVM
[mglee@ercsbrocks2 CESC]$ ls TCGA-XS-A8TJ-01A
UNCID_2546126.tar.gz
cat /storage/home/mglee/Raw_TCGA/CESC/sh/list.txt | grep -A 3 UNCID_2553096 | grep 'legacy_sample_id' | cut -d'>' -f2 | cut -d'-' -f 1,2,3,4
