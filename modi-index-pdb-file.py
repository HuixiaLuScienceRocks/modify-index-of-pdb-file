# renumber_pdb.py

input_file = "glpa.pdb"
output_file = "glpa_renumbered.pdb"
start_index = 2026

with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    index = start_index
    for line in infile:
        if line.startswith(("ATOM", "HETATM")):
            # Replace atom serial number (columns 7–11) with new index
            new_line = line[:6] + f"{index:5d}" + line[11:]
            outfile.write(new_line)
            index += 1
        else:
            # Write other lines unchanged (e.g., TER, END)
            outfile.write(line)

print(f"Renumbered PDB saved as: {output_file}")

