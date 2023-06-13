import os
import tqdm
receptor = input('Enter receptor file name (in pdb) : ')
ligand = input('Enter ligand file name(in sdf) : ')
x = float(input('Enter x coordinate: '))
y = float(input('Enter y coordinate: '))
z = float(input('Enter z coordinate: '))
box= float(input('Enter box coordinate: '))
output_file = str(input('Enter output file name: '))

import subprocess
subprocess.run(['./prepare_receptor', '-r', receptor, '-o', 'receptor.pdbqt'])
subprocess.run(['./prepare_ligand', '-r', ligand, '-o', 'ligand.pdbqt'])
center = []
center.append(x)
center.append(y)
center.append(z)

box_size = []
box_size.append(box)
box_size.append(box)
box_size.append(box)

import docking_HSA
from docking_HSA import docking
docking(ligand_file = 'ligand.pdbqt', receptor_file = 'receptor.pdbqt', center = center, box_size = box_size, output = output_file)