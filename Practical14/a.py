from xml.dom.minidom import parse
import xml.dom.minidom
import xml.sax
import matplotlib.pyplot as plt
import numpy as np
DOMTree=xml.dom.minidom.parse("go_obo.xml")
collection=DOMTree.documentElement
genes=collection.getElementsByTagName("term")
t=0
dict={}
new={}
num=[]
count=[]
for term in genes:
    t=t+1#When iterating to a term, t plus 1
    ids=term.getElementsByTagName('id')[0]
    id=ids.childNodes[0].data
    dict[id]=[]#create a dict to save each Go's childnodes.
    new[id]=0#create a dict to save each Go's number of childnodes.

print(t)#print the number of term
for term in genes:
    number = len(term.getElementsByTagName("is_a"))
    ids=term.getElementsByTagName('id')[0]
    id=ids.childNodes[0].data#take out the Go's id
    for i in range(0,number):# a for loop to itrates each <is-a>
        child = term.getElementsByTagName("is_a")[i]
        parent=child.childNodes[0].data
        dict[parent].append(id)#Add the names of the childnode of each Go to the list in dict.
def r(a):#Define a function that can evaluate the number of childnode.
    length=len(dict[a])
    for subgo in dict[a]:
        length=length+r(subgo)
    return length


for term in genes:
    ids = term.getElementsByTagName('id')[0]
    id = ids.childNodes[0].data
    m=r(id)
    new[id]=m#Store the number of childnodes derived from the function
    num.append(m)


x=np.array(num)#draw the boxplot which about the number of childNodes associated with each term
plt.boxplot(x,vert=True,whis=1.5,patch_artist=True,meanline=False,showbox=True,showcaps=True,showfliers=True,notch=False)
plt.ylabel('childnode')
plt.xlabel('Term')
plt.title('the number of childNodes associated with each term')
plt.show()

for term in genes:
    ids = term.getElementsByTagName('id')[0]
    id = ids.childNodes[0].data
    translations=term.getElementsByTagName('defstr')[0]
    translation=translations.childNodes[0].data
    if 'translation' in translation:#Exam if 'translation' is in the <defstr>
        h=new[id]
        count.append(h)

x = np.array(count)#draw the boxplot which about the number of childNodes of translation associated with each term
plt.boxplot(x, vert=True, whis=1.5, patch_artist=True, meanline=False, showbox=True, showcaps=True, showfliers=True,
            notch=False)
plt.ylabel('childnode')
plt.xlabel('Translation')
plt.title('the number of childNodes of translation associated with each term')
plt.show()





