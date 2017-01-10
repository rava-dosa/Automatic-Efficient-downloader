import os 

os.chdir('ebook-dl.com/item')
##############=destination of file in which you want to write such as /home/apoorva/check/name.txt
os.system( 'find ./  -printf "%f\n" > ##############/name.txt')

f = open("##############/name.txt",'r')
lines=f.readlines()
f.close()

f = open("##############/name.txt",'w')

for line in lines:
	f.write('http://ebook-dl.com/download/' + line )
	


f = open("##############/name.txt",'r')
lines=f.readlines()
f.close()


f = open("##############/name.txt",'w')

for line in lines:
	new=line.replace(".html","")
	f.write(new)





