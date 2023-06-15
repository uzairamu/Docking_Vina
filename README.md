# Docking_Vina
Perform molecular docking using autodock vina in a more simplified and interactive interface.
Note: You must know the x,y,z coordinates of grid as desired for your docking ( you can use any available software (PyMol) to visualize your receptor protein and get the coordinates of desired location of grid center)

1. Install Autodock vina if not already installed. 
    Just run 'sudo apt install autodock-vina' in the terminal if you are using Ubuntu. 
2. Clone the repository :
   Open the terminal in an approiate location in your device and clone the repo simply using:
   ```
   git clone https://github.com/uzairamu/Docking_Vina.git
   ```
4. Navigate to Docking_Vina directory
   ```
   cd Docking_Vina
   ```
6. Make sure you have your receptor file (in pdb format) and ligand file (in mol2 format) in the Docking_Vina directory. Now just run the python script
   ```
   python docking_vina.py
   ```
8. Now just enter your receptor file, ligand file, output flie names and the x,y,z coordinates of your grid center (Note:In case of box coordinates, just mention single value which will be used for all dimensions(x,y,z). For example for a box size of (60,60,60), just enter 60 as box_size).
9. That's it!! wait for the docking process to complete and then locate the output file created in the Docking_Vina directory. 
