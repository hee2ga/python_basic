uncleos="cttatacg"

for i in range(0,len(uncleos),3):
    codon=uncleos[i:i+3]
    if len(codon)==3:
        print(codon)
    