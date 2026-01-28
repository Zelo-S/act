import h5py

def print_structure(name, obj):
    print(name)

with h5py.File('/home/stevexing/act/sim_transferCube_scripted_multiview/episode_0.hdf5', 'r') as f:
    f.visititems(print_structure)