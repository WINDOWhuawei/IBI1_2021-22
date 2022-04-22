import re
seq='ATGCAATCGACTACGATCAATCGAGGGCC'
y=re.findall(r'\S+?GAATTC',seq)# use re.findall to get the number of cuts.
print ((len(y)+1))
    
