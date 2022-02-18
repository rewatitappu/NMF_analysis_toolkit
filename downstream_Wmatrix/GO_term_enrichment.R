#GO-term enrichment analysis for genes

library(goseq)
library(TxDb.Hsapiens.UCSC.hg38.knownGene)
library(biomaRt)
library(missMethyl)

files <- list.files(path= "/home/Documents/", pattern = "q99_features.txt$")
sink("/home/Documents/go_all_q99.txt")
lapply(files, function(x) {
   mrna = read.table(file=paste("/home/Documents/", x, sep=""), header = TRUE, sep="\t")
	assayed.genes = nmf_nonnorm$feature
	de.genes <- unique(mrna$feature)
	gene.vector=as.integer(assayed.genes%in%de.genes)
	names(gene.vector)=assayed.genes
	pwf=nullp(gene.vector,'hg38','ensGene', bias.data=NULL, plot.fit = TRUE)
	GO.wall=goseq(pwf,"hg38","ensGene")
	padj = p.adjust(GO.wall$over_represented_pvalue, method="BH")
	GO.wall.padj = cbind(GO.wall, padj)
	if(length(GO.wall.padj) > 1){
		write.table(GO.wall.padj, file = paste("/home/Documents/", x, "_99_genes.goseq", sep=""), sep = "\t")
	}
})
sink()

files <- list.files(path= "/home/Documents/", pattern = "q90_features.txtcpg.txt$")
sink("/home/Documents/meth_q90_go_all.txt")
lapply(files, function(x) {
   	meth = read.table(file=paste("/home/Documents/", x, sep=""), header = TRUE, sep="\t")
	sig.cpg <- meth$features
	print(x)
	gst <- gometh(sig.cpg=as.character(sig.cpg), collection="GO")
	print(topGSA(gst))
	
})
sink()
