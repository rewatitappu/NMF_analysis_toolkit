.libPaths( c( .libPaths(), "/mnt/cluster/R/packages/") )
library(stringr)
library(ggplot2)
library(DESeq2)

#Import the output of featureCounts.
#Change the samples to analyse in the counts_req line. File paths are the input.
counts=read.csv("/home/bams/feature_counts_out.txt", sep="", head=T, skip=1, row.names = "Geneid")
print(head(counts, 10))
colData <- read.csv("/home/phenoData.txt", sep="\t", row.names=1)
all(rownames(colData) %in% colnames(counts[,6:ncol(counts)]))
counts_req = counts[,c(6:ncol(counts))]
dds=DESeqDataSetFromMatrix(countData = counts_req, colData = colData,design = ~ Type)
ddds=DESeq(dds)
normalized_counts <- counts(ddds, normalized=TRUE)
write.table(normalized_counts, file = "/home/bams/rna_seq_polyA_norm.txt", sep = "\t", quote=FALSE)
rlog_trans <- rlog(ddds)
rlog_counts <- assay(rlog_trans)
write.table(rlog_counts, file = "/home/bams/rna_seq_polyA_rlog.txt", sep = "\t", quote=FALSE)
