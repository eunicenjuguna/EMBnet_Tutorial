

with open('viroids.fasta') as f:# opening the file
    for line in f: # the fil will  b saved as variable f
        print(line.strip())#print the line
f.close()# then close

lines = []
with open('viroids.fasta') as f:
    lines = f.readlines()
f.close() 

with open('output', 'w') as f:
    f.write('Item to output')
f.close()

lines = []#open lines
with open('viroids.fasta') as fin:
    lines = fin.readlines()
fin.close()

with open('sequence', 'w') as fout:
    fout.write(lines[3])
fout.close()
