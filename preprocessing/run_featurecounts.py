import os, sys, re



os.system("featureCounts -p -s 2 -Q 1 -a /mnt/home/Homo_sapiens.GRCh38.100.gtf -o /home/bams/feature_counts_output.txt /home/bams/*_sorted.bam")
