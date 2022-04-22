import re
fname=input('Enter the file name:')
xfile=open(fname)
y=''
for line in xfile:
    if line.startswith('>'):#Find each gene segment
        if 'GAATTC' in y:#Search for the recognition sequence of restriction endonuclease
            z = re.findall(r'\S+?GAATTC',y)#Use re.find to calculate the cuts
            print('gene name:', (x),'number of fragments:',str((len(z)+1)),'   ', (y))
        y=''#reset y
        x = str((re.findall(r'gene:(\S+)', line)))#gain the gene name
    if re.match(r'A|T|C|G', line):#use y to get out the base sequence
        y = str(y + line)
        y = str(''.join(y.split()))#Remove the Spaces in y
