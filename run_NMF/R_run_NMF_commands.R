library(NMF)

nmf_nonnorm = read.table("/home/nmf_results/concat_mat_norm_counts_varfil.txt", header = TRUE, sep = "\t")
nmf_nonnorm_mat = nmf_nonnorm
nmf_nonnorm_mat$feature = NULL
nmf_nonnorm_mat = as.matrix(nmf_nonnorm_mat)
row.names(nmf_nonnorm_mat) = nmf_nonnorm$feature

nmf_norm = read.table("/home/nmf_results/concat_mat_norm_counts_varfil_pynorm.txt", header = FALSE, sep = "\t")
colnames(nmf_norm) = colnames(nmf_nonnorm_mat)
rownames(nmf_norm) = row.names(nmf_nonnorm_mat)
nmf_norm = as.matrix(nmf_norm)
dim(nmf_norm)

res2_int = nmf(nmf_norm, 5, seed=111223, nrun=30)
w2 <- basis(res2_int)
h2 = coef(res2_int)

write.table(w2, file = "/home/nmf_results/nmf_rank5_w.txt", sep = "\t", quote = FALSE)
write.table(h2, file = "/home/nmf_results/nmf_rank5_h.txt", sep = "\t", quote = FALSE)
