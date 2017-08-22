#!/usr/bin/env python3
"""
Downloads proximity files for given genes
Usage: python3 synapseDownload.py <list of genes> <optional credential file>
"""

import sys
import synapseclient # pip install synapseclient
import os

# Check argNum
if len(sys.argv)==3:
	creds = sys.argv[2];
elif len(sys.argv) !=2:
    sys.exit( __doc__);
else:
	creds = False;

# Obtain creds
def login( creds ):
	syn = synapseclient.Synapse()
	user = ""
	password = ""
	if creds:
		with open( creds , "r" ) as f:
			credentials = []
			for l in f:
				l = l.strip()
				credentials.append( l )
			user = credentials[0]
			password = credentials[1]
	else:
		user = input( 'Enter Synapse username: ' )
		password = input( 'Enter Synapse password: ' )
	syn.login( user , password )
	return syn

syn = login(creds)

# By default get the latest version. Add version=N if needed
for gene in sys.argv[1]:
    IDfile = open("/usr/local/Misc/gene_ID.txt");
    for line in IDfile:
        line = line.strip().split();
        if gene == line[0]:
            synID = line[2];
            break;
    IDfile.close();
    entity = syn.get(synID, downloadLocation="/usr/local/hotspot3d/preprocess/prioritization");