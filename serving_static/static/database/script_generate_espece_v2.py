from fonction_taxID import *

dico_nom_commun=lecture_data("test.csv")
dico_fr=wiki(dico_nom_commun)
dico=NCBI_taxID(dico_fr)
ecriture_data(dico,"eggs.csv")
