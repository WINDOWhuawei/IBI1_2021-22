import re
fname=input('Enter the file name:')
xfile=open(fname)
y=''
for line in xfile:
    if line.startswith('>'):
        if 'GAATTC' in y:
            z = re.findall(r'\S+?GAATTC',y)
            print('gene name:', (x),'number of fragments:',str((len(z)+1)),'   ', (y))
        y=''
        x = str((re.findall(r'gene:(\S+)', line)))
    if re.match(r'A|T|C|G', line):
        y = str(y + line)
        y = str(''.join(y.split()))
