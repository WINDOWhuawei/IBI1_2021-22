
import re
xfile = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
fout=open('cut_genes.fa','w')
y=''
for line in xfile:
    if  line.startswith('>'):
            if 'GAATTC' in y:
                  #print('gene name:', (x), '   lengeth:', len(y))
                  font=open('cut_genes.fa','a')
                  fout.write('>'+str(x))
                  fout.write(str(len(y))+'\n')
                  fout.write(y+'\n')
            y=''
            x=str((re.findall(r'gene:(\S+)',line)))
    if  re.match(r'A|T|C|G',line):
            y=str(y+line)
            y=str(''.join(y.split()))
fout.close
yfile=open('cut_genes.fa')
for line in yfile:
    print (line[:-1])




