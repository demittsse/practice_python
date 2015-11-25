drop table IF EXISTS Cytoband;

CREATE TABLE Cytoband(
Chromosome INT DEFAULT NULL,
Start_pos INT  DEFAULT NULL,
End_pos INT DEFAULT NULL,
Chr_band varchar(20) DEFAULT NULL,
Chr_band_tail INT DEFAULT NULL);
LOAD DATA LOCAL INFILE "/home/ercsb/Desktop/work/Upload_DB/chromosome/cytoBandmod.txt" INTO TABLE Cytoband FIELDS TERMINATED BY "\t";

CREATE TABLE BLCA_PRADA(
uid INT DEFAULT NULL,
Cancer varchar(20) DEFAULT NULL,
Barcode_id varchar(255) DEFAULT NULL,
FG_name  varchar(255) DEFAULT NULL,
E_value FLOAT DEFAULT NULL,
Tier INT DEFAULT NULL, 
Frame varchar(20) DEFAULT NULL);

CREATE TABLE Annotation(

Gene varchar(255) DEFAULT NULL,
Gene_family TEXT DEFAULT NULL,
GO_term TEXT DEFAULT NULL,
Pathway TEXT DEFAULT NULL,
Kinase TEXT DEFAULT NULL,
Reactome TEXT DEFAULT NULL);

LOAD DATA LOCAL INFILE "/home/ercsb/Desktop/ChimerDB/func_anno/mergeanno2.txt" INTO TABLE Annotation FIELDS TERMINATED BY "\t";

 Gene_family.Family_gene, GO.GO_term,Kinase_dgidb.Gene_description, KEGG.Gene, Reactome.Term

drop table IF EXISTS TophatFusion;
CREATE TABLE TophatFusion(uid INT, Barcode_id varchar(255) DEFAULT NULL,  FG_name varchar(255) DEFAULT NULL, H_gene varchar(255) DEFAULT NULL, H_chr char(2) DEFAULT NULL,  H_position INT DEFAULT NULL, H_strand char(1) DEFAULT NULL, H_exon_num varchar(255) DEFAULT NULL, T_gene varchar(255) DEFAULT NULL,  T_chr char(2) DEFAULT NULL, T_position INT DEFAULT NULL, T_strand char(1) DEFAULT NULL, T_exon_num varchar(255) DEFAULT NULL, Transcript_id varchar(255) DEFAULT NULL, Spanreads_n INT DEFAULT NULL, Juncreads_n INT DEFAULT NULL, Fusion_type varchar(255) DEFAULT NULL, Frame_shift varchar(255) DEFAULT NULL, INDEX(uid));
LOAD DATA LOCAL INFILE "/storage3/Project/ChimerDB3/TEST/TCGA-93-A4JN-01A/THFPost_table.txt" INTO TABLE TophatFusion FIELDS TERMINATED BY "\t";

drop table IF EXISTS SoapFuse;
CREATE TABLE SoapFuse(uid INT, Cancertype varchar(255) DEFAULT NULL, Program varchar(255) DEFAULT NULL,  Barcode_id varchar(255) DEFAULT NULL,  FG_name varchar(255) DEFAULT NULL, H_gene varchar(255) DEFAULT NULL, H_chr char(2) DEFAULT NULL,  Hchr_band varchar(20) DEFUALT NULL, H_position INT DEFAULT NULL, H_strand char(1) DEFAULT NULL, H_exon_num varchar(255) DEFAULT NULL, T_gene varchar(255) DEFAULT NULL,  T_chr char(2) DEFAULT NULL, T_position INT DEFAULT NULL, T_strand char(1) DEFAULT NULL, T_exon_num varchar(255) DEFAULT NULL, Transcript_id varchar(255) DEFAULT NULL, Spanreads_n INT DEFAULT NULL, Juncreads_n INT DEFAULT NULL, Fusion_type varchar(255) DEFAULT NULL, Frame_shift varchar(255) DEFAULT NULL, INDEX(uid));
LOAD DATA LOCAL INFILE "/home/ercsb/Desktop/work/Upload_DB/up0706/luadresM.txt" INTO TABLE SoapFuse FIELDS TERMINATED BY "\t";

drop table IF EXISTS Overlap_test;
CREATE TABLE Overlap_test(Cancertype varchar(255) DEFAULT NULL, Program varchar(255) DEFAULT NULL,  Barcode_id varchar(255) DEFAULT NULL,  FG_name varchar(255) DEFAULT NULL, H_gene varchar(255) DEFAULT NULL, H_chr char(2) DEFAULT NULL,  H_position INT DEFAULT NULL, H_strand char(1) DEFAULT NULL, T_gene varchar(255) DEFAULT NULL,  T_chr char(2) DEFAULT NULL, T_position INT DEFAULT NULL, T_strand char(1) DEFAULT NULL);
LOAD DATA LOCAL INFILE "/home/ercsb/Desktop/work/Upload_DB/up0706/luad4lap.txt" INTO TABLE Overlap_test FIELDS TERMINATED BY "\t";

drop table IF EXISTS Test_chromband;
CREATE TABLE Test_chromband(Cancertype varchar(255) DEFAULT NULL, Program varchar(255) DEFAULT NULL,  Barcode_id varchar(255) DEFAULT NULL,  FG_name varchar(255) DEFAULT NULL, H_gene varchar(255) DEFAULT NULL, H_chr char(2) DEFAULT NULL,  Hchr_band varchar(255) DEFAULT null, H_position INT DEFAULT NULL,  T_gene varchar(255) DEFAULT NULL,  T_chr char(2) DEFAULT NULL, Tchr_band varchar(255) DEFAULT null, T_position INT DEFAULT NULL);
LOAD DATA LOCAL INFILE "/home/ercsb/Desktop/work/Upload_DB/up0706/pr4_pq.txt" INTO TABLE Test_chromband FIELDS TERMINATED BY "\t";

dbname=Chitars;
filename="/storage3/Project/ChimerDB3/TEST/Chitars_table.txt";
drop table IF EXISTS Chitars;
CREATE TABLE Chitars(uid INT, FG_name varchar(255) DEFAULT NULL, H_gene varchar(255) DEFAULT NULL, H_chr char(2) DEFAULT NULL,  H_position_start INT DEFAULT NULL, H_position_end INT DEFAULT NULL,H_strand char(1) DEFAULT NULL, H_trans_start INT DEFAULT NULL, H_trans_end INT DEFAULT NULL, T_gene varchar(255) DEFAULT NULL,  T_chr char(2) DEFAULT NULL, T_position_start INT DEFAULT NULL, T_position_end INT DEFAULT NULL, T_strand char(1) DEFAULT NULL, T_trans_start INT DEFAULT NULL, T_trans_end INT DEFAULT NULL, Transcript_id varchar(255) DEFAULT NULL, Chimera_id varchar(255) DEFAULT NULL, Fusion_type varchar(255) DEFAULT NULL, Frame_shift varchar(255) DEFAULT NULL, INDEX(uid));
LOAD DATA LOCAL INFILE "/storage3/Project/ChimerDB3/TEST/Chitars_table.txt" INTO TABLE Chitars FIELDS TERMINATED BY "\t";

CREATE TABLE TCGA_index(
Sample_id varchar(255) DEFAULT NULL, FG_name varchar(255) DEFAULT NULL, Barcode_id varchar(255) DEFAULT NULL,Validation varchar(255) DEFAULT NULL,Program varchar(255) DEFAULT NULL, INDEX(Sample_id));
LOAD DATA LOCAL INFILE "/storage3/Project/ChimerDB3/TEST/TCGA-93-A4JN-01A/TCGA_index.txt" INTO TABLE TCGA_index  FIELDS TERMINATED BY "\t";
#################CLINICAL#############
drop table IF EXISTS Clinical_data;
CREATE TABLE LUAD_Clinical_data(Bcr_patient_uuid TEXT DEFAULT NULL,Bcr_patient_barcode TEXT DEFAULT NULL,Form_completion_date TEXT DEFAULT NULL,Histologic_diagnosis TEXT DEFAULT NULL,Prospective_collection TEXT DEFAULT NULL,Retrospective_collection TEXT DEFAULT NULL,Gender TEXT DEFAULT NULL,Race TEXT DEFAULT NULL,Ethnicity TEXT DEFAULT NULL,History_other_malignancy TEXT DEFAULT NULL,Anatomic_organ_subdivision TEXT DEFAULT NULL,Location_lung_parenchyma TEXT DEFAULT NULL,Histologic_diagnosis_2 TEXT DEFAULT NULL,Initial_pathologic_dx_year TEXT DEFAULT NULL,Residual_tumor TEXT DEFAULT NULL,Ajcc_staging_edition TEXT DEFAULT NULL,Ajcc_tumor_pathologic_pt TEXT DEFAULT NULL,Ajcc_nodes_pathologic_pn TEXT DEFAULT NULL,Ajcc_metastasis_pathologic_pm TEXT DEFAULT NULL,Ajcc_pathologic_tumor_stage TEXT DEFAULT NULL,Ajcc_tumor_clinical_ct TEXT DEFAULT NULL,Ajcc_nodes_clinical_cn TEXT DEFAULT NULL,Ajcc_metastasis_clinical_cm TEXT DEFAULT NULL,Ajcc_clinical_tumor_stage TEXT DEFAULT NULL,Pulmonary_function_test_indicator TEXT DEFAULT NULL,Fev1_percent_ref_prebroncholiator TEXT DEFAULT NULL,Fev1_percent_ref_postbroncholiator TEXT DEFAULT NULL,Fev1_fvc_ratio_prebroncholiator TEXT DEFAULT NULL,Fev1_fvc_ratio_postbroncholiator TEXT DEFAULT NULL,Carbon_monoxide_diffusion_dlco TEXT DEFAULT NULL,Kras_gene_analysis_indicator TEXT DEFAULT NULL,Kras_mutation_found TEXT DEFAULT NULL,Kras_mutation_identified_type TEXT DEFAULT NULL,Egfr_mutation_status TEXT DEFAULT NULL,Egfr_mutation_identified_type TEXT DEFAULT NULL,Eml4_alk_translocation_status TEXT DEFAULT NULL,Eml4_alk_translocation_variant TEXT DEFAULT NULL,History_neoadjuvant_treatment TEXT DEFAULT NULL,Eml4_alk_analysis_type TEXT DEFAULT NULL,Tobacco_smoking_history_indicator TEXT DEFAULT NULL,Tobacco_smoking_year_started TEXT DEFAULT NULL,Tobacco_smoking_year_stopped TEXT DEFAULT NULL,Vital_status TEXT DEFAULT NULL,Tobacco_smoking_pack_years_smoked TEXT DEFAULT NULL,Karnofsky_score TEXT DEFAULT NULL,Ecog_score TEXT DEFAULT NULL,Performance_status_timing TEXT DEFAULT NULL,Radiation_treatment_adjuvant TEXT DEFAULT NULL,Treatment_outcome_first_course TEXT DEFAULT NULL,Tumor_status TEXT DEFAULT NULL,New_tumor_event_dx_indicator TEXT DEFAULT NULL,Birth_days_to TEXT DEFAULT NULL,Last_contact_days_to TEXT DEFAULT NULL,Death_days_to TEXT DEFAULT NULL,Age_at_initial_pathologic_diagnosis TEXT DEFAULT NULL,Anatomic_neoplasm_subdivision_other TEXT DEFAULT NULL,Days_to_initial_pathologic_diagnosis TEXT DEFAULT NULL,Disease_code TEXT DEFAULT NULL,Extranodal_involvement TEXT DEFAULT NULL,Icd_10 TEXT DEFAULT NULL,Icd_o_3_histology TEXT DEFAULT NULL,Icd_o_3_site TEXT DEFAULT NULL,Informed_consent_verified TEXT DEFAULT NULL,Patient_id TEXT DEFAULT NULL,Project_code TEXT DEFAULT NULL,Targeted_molecular_therapy TEXT DEFAULT NULL,Tissue_source_site TEXT DEFAULT NULL,Tumor_tissue_site TEXT DEFAULT NULL);
LOAD DATA LOCAL INFILE "/storage3/Project/ChimerDB3/TEST/TCGA-93-A4JN-01A/Clinic_data/Biotab/nationwidechildrens.org_clinical_patient_luad.txt" INTO TABLE LUAD_Clinical_data FIELDS TERMINATED BY "\t" IGNORE 2 LINES;

CREATE TABLE LAML_Clinical_data(Bcr_patient_uuid TEXT DEFAULT NULL,Bcr_patient_barcode TEXT DEFAULT NULL,Form_completion_date TEXT DEFAULT NULL,Histologic_diagnosis TEXT DEFAULT NULL,Prospective_collection TEXT DEFAULT NULL,Retrospective_collection TEXT DEFAULT NULL,Gender TEXT DEFAULT NULL,Race TEXT DEFAULT NULL,Ethnicity TEXT DEFAULT NULL,History_other_malignancy TEXT DEFAULT NULL,Anatomic_organ_subdivision TEXT DEFAULT NULL,Location_lung_parenchyma TEXT DEFAULT NULL,Histologic_diagnosis_2 TEXT DEFAULT NULL,Initial_pathologic_dx_year TEXT DEFAULT NULL,Residual_tumor TEXT DEFAULT NULL,Ajcc_staging_edition TEXT DEFAULT NULL,Ajcc_tumor_pathologic_pt TEXT DEFAULT NULL,Ajcc_nodes_pathologic_pn TEXT DEFAULT NULL,Ajcc_metastasis_pathologic_pm TEXT DEFAULT NULL,Ajcc_pathologic_tumor_stage TEXT DEFAULT NULL,Ajcc_tumor_clinical_ct TEXT DEFAULT NULL,Ajcc_nodes_clinical_cn TEXT DEFAULT NULL,Ajcc_metastasis_clinical_cm TEXT DEFAULT NULL,Ajcc_clinical_tumor_stage TEXT DEFAULT NULL,Pulmonary_function_test_indicator TEXT DEFAULT NULL,Fev1_percent_ref_prebroncholiator TEXT DEFAULT NULL,Fev1_percent_ref_postbroncholiator TEXT DEFAULT NULL,Fev1_fvc_ratio_prebroncholiator TEXT DEFAULT NULL,Fev1_fvc_ratio_postbroncholiator TEXT DEFAULT NULL,Carbon_monoxide_diffusion_dlco TEXT DEFAULT NULL,Kras_gene_analysis_indicator TEXT DEFAULT NULL,Kras_mutation_found TEXT DEFAULT NULL,Kras_mutation_identified_type TEXT DEFAULT NULL,Egfr_mutation_status TEXT DEFAULT NULL,Egfr_mutation_identified_type TEXT DEFAULT NULL,Eml4_alk_translocation_status TEXT DEFAULT NULL,Eml4_alk_translocation_variant TEXT DEFAULT NULL,History_neoadjuvant_treatment TEXT DEFAULT NULL,Eml4_alk_analysis_type TEXT DEFAULT NULL,Tobacco_smoking_history_indicator TEXT DEFAULT NULL,Tobacco_smoking_year_started TEXT DEFAULT NULL,Tobacco_smoking_year_stopped TEXT DEFAULT NULL,Vital_status TEXT DEFAULT NULL,Tobacco_smoking_pack_years_smoked TEXT DEFAULT NULL,Karnofsky_score TEXT DEFAULT NULL,Ecog_score TEXT DEFAULT NULL,Performance_status_timing TEXT DEFAULT NULL,Radiation_treatment_adjuvant TEXT DEFAULT NULL,Treatment_outcome_first_course TEXT DEFAULT NULL,Tumor_status TEXT DEFAULT NULL,New_tumor_event_dx_indicator TEXT DEFAULT NULL,Birth_days_to TEXT DEFAULT NULL,Last_contact_days_to TEXT DEFAULT NULL,Death_days_to TEXT DEFAULT NULL,Age_at_initial_pathologic_diagnosis TEXT DEFAULT NULL,Anatomic_neoplasm_subdivision_other TEXT DEFAULT NULL,Days_to_initial_pathologic_diagnosis TEXT DEFAULT NULL,Disease_code TEXT DEFAULT NULL,Extranodal_involvement TEXT DEFAULT NULL,Icd_10 TEXT DEFAULT NULL,Icd_o_3_histology TEXT DEFAULT NULL,Icd_o_3_site TEXT DEFAULT NULL,Informed_consent_verified TEXT DEFAULT NULL,Patient_id TEXT DEFAULT NULL,Project_code TEXT DEFAULT NULL,Targeted_molecular_therapy TEXT DEFAULT NULL,Tissue_source_site TEXT DEFAULT NULL,Tumor_tissue_site TEXT DEFAULT NULL);
LOAD DATA LOCAL INFILE "/storage3/Project/ChimerDB3/Clinical/nationwidechildrens.org_clinical_patient_laml.txt" INTO TABLE LAML_Clinical_data FIELDS TERMINATED BY "\t" IGNORE 2 LINES;

CREATE TABLE GBM_Clinical_data(Bcr_patient_uuid TEXT DEFAULT NULL,Bcr_patient_barcode TEXT DEFAULT NULL,Form_completion_date TEXT DEFAULT NULL,Histologic_diagnosis TEXT DEFAULT NULL,Prospective_collection TEXT DEFAULT NULL,Retrospective_collection TEXT DEFAULT NULL,Gender TEXT DEFAULT NULL,Race TEXT DEFAULT NULL,Ethnicity TEXT DEFAULT NULL,History_other_malignancy TEXT DEFAULT NULL,Anatomic_organ_subdivision TEXT DEFAULT NULL,Location_lung_parenchyma TEXT DEFAULT NULL,Histologic_diagnosis_2 TEXT DEFAULT NULL,Initial_pathologic_dx_year TEXT DEFAULT NULL,Residual_tumor TEXT DEFAULT NULL,Ajcc_staging_edition TEXT DEFAULT NULL,Ajcc_tumor_pathologic_pt TEXT DEFAULT NULL,Ajcc_nodes_pathologic_pn TEXT DEFAULT NULL,Ajcc_metastasis_pathologic_pm TEXT DEFAULT NULL,Ajcc_pathologic_tumor_stage TEXT DEFAULT NULL,Ajcc_tumor_clinical_ct TEXT DEFAULT NULL,Ajcc_nodes_clinical_cn TEXT DEFAULT NULL,Ajcc_metastasis_clinical_cm TEXT DEFAULT NULL,Ajcc_clinical_tumor_stage TEXT DEFAULT NULL,Pulmonary_function_test_indicator TEXT DEFAULT NULL,Fev1_percent_ref_prebroncholiator TEXT DEFAULT NULL,Fev1_percent_ref_postbroncholiator TEXT DEFAULT NULL,Fev1_fvc_ratio_prebroncholiator TEXT DEFAULT NULL,Fev1_fvc_ratio_postbroncholiator TEXT DEFAULT NULL,Carbon_monoxide_diffusion_dlco TEXT DEFAULT NULL,Kras_gene_analysis_indicator TEXT DEFAULT NULL,Kras_mutation_found TEXT DEFAULT NULL,Kras_mutation_identified_type TEXT DEFAULT NULL,Egfr_mutation_status TEXT DEFAULT NULL,Egfr_mutation_identified_type TEXT DEFAULT NULL,Eml4_alk_translocation_status TEXT DEFAULT NULL,Eml4_alk_translocation_variant TEXT DEFAULT NULL,History_neoadjuvant_treatment TEXT DEFAULT NULL,Eml4_alk_analysis_type TEXT DEFAULT NULL,Tobacco_smoking_history_indicator TEXT DEFAULT NULL,Tobacco_smoking_year_started TEXT DEFAULT NULL,Tobacco_smoking_year_stopped TEXT DEFAULT NULL,Vital_status TEXT DEFAULT NULL,Tobacco_smoking_pack_years_smoked TEXT DEFAULT NULL,Karnofsky_score TEXT DEFAULT NULL,Ecog_score TEXT DEFAULT NULL,Performance_status_timing TEXT DEFAULT NULL,Radiation_treatment_adjuvant TEXT DEFAULT NULL,Treatment_outcome_first_course TEXT DEFAULT NULL,Tumor_status TEXT DEFAULT NULL,New_tumor_event_dx_indicator TEXT DEFAULT NULL,Birth_days_to TEXT DEFAULT NULL,Last_contact_days_to TEXT DEFAULT NULL,Death_days_to TEXT DEFAULT NULL,Age_at_initial_pathologic_diagnosis TEXT DEFAULT NULL,Anatomic_neoplasm_subdivision_other TEXT DEFAULT NULL,Days_to_initial_pathologic_diagnosis TEXT DEFAULT NULL,Disease_code TEXT DEFAULT NULL,Extranodal_involvement TEXT DEFAULT NULL,Icd_10 TEXT DEFAULT NULL,Icd_o_3_histology TEXT DEFAULT NULL,Icd_o_3_site TEXT DEFAULT NULL,Informed_consent_verified TEXT DEFAULT NULL,Patient_id TEXT DEFAULT NULL,Project_code TEXT DEFAULT NULL,Targeted_molecular_therapy TEXT DEFAULT NULL,Tissue_source_site TEXT DEFAULT NULL,Tumor_tissue_site TEXT DEFAULT NULL);
LOAD DATA LOCAL INFILE "/storage3/Project/ChimerDB3/Clinical/nationwidechildrens.org_clinical_patient_gbm.txt" INTO TABLE GBM_Clinical_data FIELDS TERMINATED BY "\t" IGNORE 2 LINES;

CREATE TABLE DLBC_Clinical_data(Bcr_patient_uuid TEXT DEFAULT NULL,Bcr_patient_barcode TEXT DEFAULT NULL,Form_completion_date TEXT DEFAULT NULL,Histologic_diagnosis TEXT DEFAULT NULL,Prospective_collection TEXT DEFAULT NULL,Retrospective_collection TEXT DEFAULT NULL,Gender TEXT DEFAULT NULL,Race TEXT DEFAULT NULL,Ethnicity TEXT DEFAULT NULL,History_other_malignancy TEXT DEFAULT NULL,Anatomic_organ_subdivision TEXT DEFAULT NULL,Location_lung_parenchyma TEXT DEFAULT NULL,Histologic_diagnosis_2 TEXT DEFAULT NULL,Initial_pathologic_dx_year TEXT DEFAULT NULL,Residual_tumor TEXT DEFAULT NULL,Ajcc_staging_edition TEXT DEFAULT NULL,Ajcc_tumor_pathologic_pt TEXT DEFAULT NULL,Ajcc_nodes_pathologic_pn TEXT DEFAULT NULL,Ajcc_metastasis_pathologic_pm TEXT DEFAULT NULL,Ajcc_pathologic_tumor_stage TEXT DEFAULT NULL,Ajcc_tumor_clinical_ct TEXT DEFAULT NULL,Ajcc_nodes_clinical_cn TEXT DEFAULT NULL,Ajcc_metastasis_clinical_cm TEXT DEFAULT NULL,Ajcc_clinical_tumor_stage TEXT DEFAULT NULL,Pulmonary_function_test_indicator TEXT DEFAULT NULL,Fev1_percent_ref_prebroncholiator TEXT DEFAULT NULL,Fev1_percent_ref_postbroncholiator TEXT DEFAULT NULL,Fev1_fvc_ratio_prebroncholiator TEXT DEFAULT NULL,Fev1_fvc_ratio_postbroncholiator TEXT DEFAULT NULL,Carbon_monoxide_diffusion_dlco TEXT DEFAULT NULL,Kras_gene_analysis_indicator TEXT DEFAULT NULL,Kras_mutation_found TEXT DEFAULT NULL,Kras_mutation_identified_type TEXT DEFAULT NULL,Egfr_mutation_status TEXT DEFAULT NULL,Egfr_mutation_identified_type TEXT DEFAULT NULL,Eml4_alk_translocation_status TEXT DEFAULT NULL,Eml4_alk_translocation_variant TEXT DEFAULT NULL,History_neoadjuvant_treatment TEXT DEFAULT NULL,Eml4_alk_analysis_type TEXT DEFAULT NULL,Tobacco_smoking_history_indicator TEXT DEFAULT NULL,Tobacco_smoking_year_started TEXT DEFAULT NULL,Tobacco_smoking_year_stopped TEXT DEFAULT NULL,Vital_status TEXT DEFAULT NULL,Tobacco_smoking_pack_years_smoked TEXT DEFAULT NULL,Karnofsky_score TEXT DEFAULT NULL,Ecog_score TEXT DEFAULT NULL,Performance_status_timing TEXT DEFAULT NULL,Radiation_treatment_adjuvant TEXT DEFAULT NULL,Treatment_outcome_first_course TEXT DEFAULT NULL,Tumor_status TEXT DEFAULT NULL,New_tumor_event_dx_indicator TEXT DEFAULT NULL,Birth_days_to TEXT DEFAULT NULL,Last_contact_days_to TEXT DEFAULT NULL,Death_days_to TEXT DEFAULT NULL,Age_at_initial_pathologic_diagnosis TEXT DEFAULT NULL,Anatomic_neoplasm_subdivision_other TEXT DEFAULT NULL,Days_to_initial_pathologic_diagnosis TEXT DEFAULT NULL,Disease_code TEXT DEFAULT NULL,Extranodal_involvement TEXT DEFAULT NULL,Icd_10 TEXT DEFAULT NULL,Icd_o_3_histology TEXT DEFAULT NULL,Icd_o_3_site TEXT DEFAULT NULL,Informed_consent_verified TEXT DEFAULT NULL,Patient_id TEXT DEFAULT NULL,Project_code TEXT DEFAULT NULL,Targeted_molecular_therapy TEXT DEFAULT NULL,Tissue_source_site TEXT DEFAULT NULL,Tumor_tissue_site TEXT DEFAULT NULL);
LOAD DATA LOCAL INFILE "/storage3/Project/ChimerDB3/Clinical/nationwidechildrens.org_clinical_patient_dlbc.txt" INTO TABLE DLBC_Clinical_data FIELDS TERMINATED BY "\t" IGNORE 2 LINES;


##################
drop table IF EXISTS Sample_info;
CREATE TABLE Sample_info(Bcr_patient_uuid TEXT DEFAULT NULL,Bcr_sample_barcode TEXT DEFAULT NULL,Bcr_sample_uuid TEXT DEFAULT NULL,Intermediate_dimension TEXT DEFAULT NULL,Is_ffpe TEXT DEFAULT NULL,Longest_dimension TEXT DEFAULT NULL,Pathology_report_uuid TEXT DEFAULT NULL,Sample_type TEXT DEFAULT NULL,Sample_type_id TEXT DEFAULT NULL,Shortest_dimension TEXT DEFAULT NULL,Vial_number TEXT DEFAULT NULL);
LOAD DATA LOCAL INFILE "/storage3/Project/ChimerDB3/TEST/TCGA-93-A4JN-01A/sample_luad.txt" INTO TABLE Sample_info FIELDS TERMINATED BY "\t" IGNORE 2 LINES;

drop table IF EXISTS Kinase_dgidb;
CREATE TABLE Kinase_dgidb(Gene varchar(255) DEFAULT NULL, Gene_description TEXT DEFAULT NULL, Source varchar(255) DEFAULT NULL);
LOAD DATA LOCAL INFILE "/storage3/Project/ChimerDB3/Kinase/dgidb_export_2015-04-13.tsv" INTO TABLE Kinase_dgidb FIELDS TERMINATED BY "\t" IGNORE 1 LINES;

CREATE TABLE Gene_family(URL varchar(255) DEFAULT NULL,	Family_gene varchar(255) DEFAULT NULL,	 Family_gene_description varchar(255) DEFAULT NULL, Symbol varchar(255) DEFAULT NULL,	HGNC_id INT DEFAULT NULL);
LOAD DATA LOCAL INFILE "/storage3/Project/ChimerDB3/FamilyGene/genefam_list.txt" INTO TABLE Gene_family FIELDS TERMINATED BY "\t" IGNORE 1 LINES;

drop table IF EXISTS CN_93A4JN01A;
CREATE TABLE CN_93A4JN01A(Sample BLOB DEFAULT NULL,Chr CHAR(2) DEFAULT NULL,Pos_start INT DEFAULT NULL, Pos_end INT DEFAULT NULL, Num_Probes FLOAT DEFAULT NULL,Segment_Mean FLOAT DEFAULT NULL);
LOAD DATA LOCAL INFILE "/storage3/Project/ChimerDB3/TEST/TCGA-93-A4JN-01A/CopyNumber/TAROK_p_TCGA_264_N_GenomeWideSNP_6_B03_1306632.hg19.seg.txt" INTO TABLE CN_93A4JN01A FIELDS TERMINATED BY "\t" IGNORE 1 LINES;

LOAD DATA LOCAL INFILE "/storage3/Project/ChimerDB3/TEST/refGene.txt" INTO TABLE refGene FIELDS TERMINATED BY "\t";
CREATE TABLE Mitelman_recurrent (
   Chromosome                                         VARCHAR(5) ,
   Arm                                               VARCHAR(2) ,
   Band                                               INT ,
   Aberration                                        VARCHAR(255) ,
   Code                                               VARCHAR(10) ,
   Organ                                              VARCHAR(10) ,
   Total_cases                                        VARCHAR(5) ,
   Gene                                               VARCHAR(255) ,
   Chr_order                                          INT ,
   Type                                               CHAR(1)
)
;
LOAD DATA LOCAL INFILE "/storage3/Project/ChimerDB3/Mitelman/recurrent_data.dat" INTO TABLE Mitelman_recurrent FIELDS TERMINATED BY "\t";
CREATE TABLE Mitelman_recurrent_num (
   Chromosome                                         VARCHAR(5) ,
   Abnormality                                        VARCHAR(5) ,
   Code                                               VARCHAR(10) ,
   Organ                                              VARCHAR(10) ,
   Total_cases                                        VARCHAR(5) ,
   Chr_order                                          INT
)
;
LOAD DATA LOCAL INFILE "/storage3/Project/ChimerDB3/Mitelman/recurrent_num_data.dat" INTO TABLE Mitelman_recurrent_num FIELDS TERMINATED BY "\t" IGNORE 1 LINES;

CREATE TABLE ID_index (
	Sample_id VARCHAR(255) DEFAULT NULL,	Source VARCHAR(255) DEFAULT NULL,	Tcga_barcode_id VARCHAR(255) DEFAULT NULL, 	Raw_data_id VARCHAR(255) DEFAULT NULL
	);
(Sample_id,	Source,	Tcga_barcode_id,	Raw_data_id)

INSERT INTO ID_index(Sample_id,Source,Tcga_barcode_id,Raw_data_id) VALUES (SF93A4JN01A,SoapFuse,TCGA-93-A4JN-01A,NA);
INSERT INTO ID_index (Sample_id,	Source,	Tcga_barcode_id,	Raw_data_id) VALUES (TH93A4JN01A,	TophatFusion,	TCGA-93-A4JN-01A,	NA);
INSERT INTO ID_index (Sample_id,	Source,	Tcga_barcode_id,	Raw_data_id) VALUES ('FS93A4JN01A',	'FusionScan',	'TCGA-93-A4JN-01A',	'NA');
INSERT INTO ID_index (Sample_id,	Source,	Tcga_barcode_id,	Raw_data_id) VALUES ('PR93A4JN01A',	'PRADA','TCGA-93-A4JN-01A',	'NA');

INSERT INTO `Chimer3`.`ID_index` (`Sample_id`, `Source`, `Tcga_barcode_id`, `Raw_data_id`) VALUES ('FS93A4JN01A',	'FusionScan',	'TCGA-93-A4JN-01A',	'NA'), ('PR93A4JN01A',	'PRADA','TCGA-93-A4JN-01A',	'NA');

CREATE TABLE LUAD_Fusionscan_test(
	uid INT,
	Cancertype 	 	VARCHAR(20) DEFAULT NULL,
	Program 	VARCHAR(20) DEFAULT NULL,
	Tcga_barcode_id 	VARCHAR(255) DEFAULT NULL,
	FG_name VARCHAR(255) DEFAULT NULL,
	H_gene 	VARCHAR(255) DEFAULT NULL,
	H_chr 	INT,
	H_position 	INT,
	H_strand 	VARCHAR(20) DEFAULT NULL,
	H_exon_num VARCHAR(20) DEFAULT NULL,
	T_gene	VARCHAR(255) DEFAULT NULL,
	T_chr	INT,
	T_position INT,
	T_strand	VARCHAR(20) DEFAULT NULL,
	T_exon_num	VARCHAR(20) DEFAULT NULL,
	Transcript_id VARCHAR(20) DEFAULT NULL,
	Seed	INT
	);
LOAD DATA LOCAL INFILE "/storage3/Project/mglee/2.TCGA_THF/10.LUAD/list/LUADfustest.txt" INTO TABLE LUAD_Fusionscan_test FIELDS TERMINATED BY "\t";
