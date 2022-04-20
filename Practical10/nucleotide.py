import re
sequence=input('Enter the DNA sequence:')

def nucleotide(i):
    i=sequence.upper()#Converts all lower case in Suquence to upper case
    a=0
    t=0
    c=0
    g=0
    for r in range(int(len(i))):#Count the total amount of each nucleic acid
        if i[r]=='A':
            a=a+1
        if i[r]=='T':
            t=t+1
        if i[r]=='C':
            c=c+1
        if i[r]=='G':
            g=g+1
    a=a/int(len(i))#caculate the	percentage	of	nucleotides	in the sequence
    t=t/int(len(i))
    c=c/int(len(i))
    g=g/int(len(i))
    print('%.2f%%'%(a*100),'%.2f%%'%(t*100),'%.2f%%'%(c*100),'%.2f%%'%(g*100))#Keep the decimal and convert them to percentage
    return a,t,c,g

nucleotide (sequence)
#example:#nucleotide (sequence)
# Enter the DNA sequence:atgccg
#16.67% 16.67% 33.33% 33.33%




