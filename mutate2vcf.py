import msprime, pyslim, numpy, sys, getopt, tskit, os, warnings


def main(argv):
	inputfile = ''
	outputfile = ''
	try:
		opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
	except getopt.GetoptError:
		print ('test.py -i <inputfile> -o <outputfile>')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print ('test.py -i <inputfile> -o <outputfile>')
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg
		elif opt in ("-o", "--ofile"):
			outputfile = arg
# Get Slim trees
	warnings.simplefilter('ignore', msprime.TimeUnitsMismatchWarning)

	ts = tskit.load(inputfile)

# Recapitate

	pos = (0,19999999,20000000,39999999,40000000,59999999,60000000,79999999,80000000,100000001)
	rat = (1e-8,0.5,1e-8,0.5,1e-8,0.5,1e-8,0.5,1e-8)
	recomb_map = msprime.RateMap(position=pos, rate=rat)
	rts = pyslim.recapitate(ts, recombination_rate=recomb_map , ancestral_Ne=10000)

# Simplification

	rng = numpy.random.default_rng()
	alive_inds = pyslim.individuals_alive_at(rts, 0)
	keep_inds = rng.choice(alive_inds, 400, replace=False)
	keep_nodes = []

	for i in keep_inds:
		keep_nodes.extend(rts.individual(i).nodes)
	
	sts = rts.simplify(keep_nodes, keep_input_roots=True)

# Overlay mutations using coalescence; mutation rates is rounded up value from resequenced MAL lines (Exposit-Alonso et al., 2018), keep = T will keep selective mutations from SLiM (if any)
  

	next_id = pyslim.next_slim_mutation_id(sts)
	mts = msprime.sim_mutations(sts, rate=1e-8, model=msprime.SLiMMutationModel(type=0, next_id=next_id), keep=True)

	indlist = []
	for i in pyslim.individuals_alive_at(mts, 0):
		ind = mts.individual(i)
		if mts.node(ind.nodes[0]).is_sample():
			indlist.append(i)
			assert mts.node(ind.nodes[1]).is_sample()

	with open(outputfile, "w") as vcffile:
		mts.write_vcf(vcffile, individuals=indlist)


if __name__ == "__main__":
	main(sys.argv[1:])

