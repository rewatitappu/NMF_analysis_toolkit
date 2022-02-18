#pvalue adjustment for data matrices

files <- list.files(path= "/home/nmf_results/", pattern = "corr.txt$")
lapply(files, function(x) {
	df = read.table(file=paste("/home/nmf_results/", x, sep=""), header = FALSE, sep="\t")
	colnames(df) = c("ENSG",  "cpg", "t_statistic", "p_value")
	padj = p.adjust(df$p_value, method = "fdr", n = length(df$p_value))
	df_new = cbind(df, padj)
	write.table(df_new, file=paste("/home/nmf_results/", x, "_padj.txt", sep=""), sep="\t", quote=FALSE)
	
})
