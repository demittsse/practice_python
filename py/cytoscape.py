from __future__ import print_function
import requests
def get_psiquic_uniprot(query, **kwargs):
	kwargs['format'] = kwargs.get('format', 'tab27')
	server = 'http://www.ebi.ac.uk/Tools/webservices/psicquic/uniprot/webservices/current/search/query'
	req = requests.get('%s/%s' % (server, query),
	params=kwargs)
	return req.content
from collections import defaultdict
genes_species = defaultdict(set)
interactions = {}
def get_gene_name(my_id, alt_names):
	toks = alt_names.split('|')
	for tok in toks:
		if tok.endswith('(gene name)'):
			return tok[tok.find(':') + 1: tok.find('(')]
	return my_id + '?' # no name...
def get_vernacular_tax(tax):
	return tax.split('|')[0][tax.find('(') + 1:-1]
def add_interactions(species):
	for rec in species.split('\n'):
		toks = rec.rstrip().split('\t')
		if len(toks) < 15:
			continue # empty line at the end
		id1 = toks[0][toks[0].find(':') + 1:]
		id2 = toks[1][toks[1].find(':') + 1:]
		gene1, gene2 = get_gene_name(id1, toks[4]), get_gene_name(id2, toks[5])
		tax1, tax2 = get_vernacular_tax(toks[9]), get_vernacular_tax(toks[10])
		inter_type = toks[11][toks[11].find('(') + 1:-1]
		miscore = float(toks[14].split(':')[1])
		genes_species[tax1].add(gene1)
		genes_species[tax2].add(gene2)
		interactions[((tax1, gene1), (tax2, gene2))] =  {'score': miscore, 'type': inter_type}

human = get_psiquic_uniprot('uniprotkb:P04637')
add_interactions(human)
rat = get_psiquic_uniprot('uniprotkb:P10361')
add_interactions(rat)
mouse = get_psiquic_uniprot('uniprotkb:P02340')
add_interactions(mouse)
