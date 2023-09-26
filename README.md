# SLiM3cassava
This repository is for scripts coded in Eidos (SLiM3 compatible) and Python (msprime compatible) that run simulations of cassava population throughout it's domestication. 

Four model groups have been explored in SLiM3:

Group1: WF_Coal_noCln_noSel_noSpc - models with no transition to cloning, no selection
Group2: WF_Coal_ysCln_noSel_noSpc - models with transition to cloning, but no selection
Group3: WF_Coal_ysCln_ysSel_noSpc - models with transition to cloning, and positive selection (mimicking selection in loci underlying domestication)
Group4: WF_Coal_ysCln_hetSel_noSpc - models with transition to cloning, and negative selection (mimicking heterozygous advantage)

Each model group includes 12 demographic scenarios, changing bottleneck population size and final population size.
