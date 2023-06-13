import vina
from vina.vina import Vina
def docking(receptor_file,ligand_file,center : list, box_size : list, output : str):
    box = list(box_size)
    grid_center = list(center)
    v=Vina(sf_name='vina')
    v.set_receptor(receptor_file)
    v.set_ligand_from_file(ligand_file)
    v.compute_vina_maps(center= center,box_size= box_size)
    energy_minimized = v.optimize()
    v.write_pose('pose.pdbqt' , overwrite = True)
    v.dock(exhaustiveness=32, n_poses=20)
    v.write_poses(pdbqt_filename = output , n_poses=5, overwrite=True)
    return(f'Score after minimization : %.3f (kcal/mol) {energy_minimized[0]}')
