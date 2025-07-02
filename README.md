## Command:
python modi-index-pdb-file.py

# more importantly, when running metadynamics:

if the serial number of an atom is greater than 99999, it is written in hybrid-36 notation (see pdbreader).
The main use of pdbrenumber is thus that of producing files where atoms are numbered using hybrid-36 convention.

### in BSC MN5:
#### module load openmpi/4.1.5-gcc fftw/3.3.10-gcc-ompi plumed/2.9.0-gcc-ompi
#### plumed pdbrenumber --ipdb input.pdb --opdb output.pdb
