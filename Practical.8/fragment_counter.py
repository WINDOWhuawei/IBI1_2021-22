import re
seq='ATGCAATCGACTACGATCAATCGAGGGCC'
y=re.findall(r'\S+?GAATTC',seq)
print ((len(y)+1))
    
