
import re
xfile = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
fout=open('cut_genes.fa','w')
y=''
for line in xfile:
    if  line.startswith('>'):#find out the gene sequence
            if 'GAATTC' in y:#check if recognition sequence of restriction endonuclease in the sequence
                  #print('gene name:', (x), '   lengeth:', len(y))
                  font=open('cut_genes.fa','a')#write the gene name,length,sequence into cut_gene.fa
                  fout.write('>'+str(x))
                  fout.write(str(len(y))+'\n')
                  fout.write(y+'\n')
            y=''#reset y
            x=str((re.findall(r'gene:(\S+)',line)))# gain the gene name.
    if  re.match(r'A|T|C|G',line):#find the begain of base sequence.
            y=str(y+line)#Put the base sequence in y
            y=str(''.join(y.split()))#remove the space in y
fout.close
yfile=open('cut_genes.fa')
for line in yfile:#open the new-write file.
    print (line[:-1])




