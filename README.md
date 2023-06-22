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
3. Navigate to Docking_Vina directory
   ```
   cd Docking_Vina
   ```
4. Install ADFR-Suite (SKIP THIS STEP IF DONE ALERADY):
   ```
   tar zxvf ADFR.tar.gz
   ```
   ```
   cd ADFRsuite_x86_64Linux_1.0
   ```
   ```
   ./install.sh
   ```
   Now just navigate to bin and copy the prepare_receptor and prepare_ligand files in Docking_Vina directory.
   
5. Make sure you have your receptor file (in pdb format) and ligand file (in mol2 format) in the Docking_Vina directory. Now just run the python script
   ```
   python docking_vina.py
   ```
6. Now just enter your receptor file, ligand file, output flie names and the x,y,z coordinates of your grid center (Note:In case of box coordinates, just mention single value which will be used for all dimensions(x,y,z). For example for a box size of (60,60,60), just enter 60 as box_size).
7. That's it!! wait for the docking process to complete and then locate the output file created in the Docking_Vina directory. 
