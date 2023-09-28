# SLiM3cassava
This repository is for scripts coded in Eidos (SLiM3-compatible) and Python (msprime-compatible) that run simulations of cassava population throughout its domestication. 

In short, our tree-sequence recording Wright-Fisher models start with a 'burn-in' period, in which a population of 10,000 indvidual plants is simulated for 100,000 generations. This simulates a neutral evolution  of wild cassava plants until they reach population 'equibilibrium'. Each of the indviduals has a simplified genome, coded as five chromosomes, each 20mb long with generic recombination rates (1e-08). After 100,000 generations our models induce changes that simulate cassava domestication. Domesticated population is allowed to evolve for another 5,000 generations.

We explore 4 different model groups, which differ in the effect of domestication on simulated populations after the burn-in period:

	Group1: WF_Coal_noCln_noSel_noSpc
	Domestication leads to no transition to cloning, and no selection.

	Group2: WF_Coal_ysCln_noSel_noSpc
	Domestication leads to transition to cloning (cloning rate set to 0.99), but no selection.

	Group3: WF_Coal_ysCln_ysSel_noSpc
	Domestication leads to transition to cloning (cloning rate set to 0.99), and positive selection (mimicking selection on loci underlying domestication). 1000 domestication loci are coded to appear 1000 generations before the domestication period. Those loci are beneficial with dominance coefficient 0.5 and a fixed selection coefficient of 0.05.

	Group4: WF_Coal_ysCln_hetSel_noSpc
	Domestication leads to transition to cloning (cloning rate set to 0.99), and negative selection (mimicking heterozygous advantage). At the time of transition to cloning, a class of neutral mutations become deleterious in homozygous state. The strength of selection is determined from gamma distribution with mean value of -0.03, and shape parameter of 0.2, the dominance coefficient is set to zero.

Each model group includes 12 demographic scenarios simulating 'domestication bottlenecks'. We model 2 bottleneck parameters, first, the bottleneck population size  (ne[min] = 100,500,1000,or 10000) and second, the recovery population size (ne[max] = 5000, 10000, or 20000).

In total, we tested 48 models. We ran each model in SLiM3 100 times. We saved the tree-sequence (geneaologies) and, where applicable, non-neutral mutations in SLiM3 'trees' format.

The tree-sequence were subsequently read into msprime. We carried out recapitation and simplification of tree-sequences to make sure that all sampled indviduals coalesce with a single root. We then used msprime coelescent model to overlay the tree-sequence with neutral mutations and exported it in vcf format.


