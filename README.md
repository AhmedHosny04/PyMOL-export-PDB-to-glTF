
-----

# PyMOL Molecular Visualization to GLTF/GLB Exporter

This utility provides a robust, headless (non-GUI) method to convert Protein Data Bank (PDB) files into high-quality, Mol\*-styled 3D assets in the **glTF** format, ready for integration into web or mobile applications (e.g., Flutter).

## 🚀 Purpose

The script automates the process of loading a PDB file into PyMOL, applying standard molecular visualization (Cartoon for polymer, Ball & Stick for ligands), and exporting the resulting 3D geometry as a GLTF file, all without launching the PyMOL Graphical User Interface.

## 🛠️ Prerequisites

This script relies on PyMOL's ability to execute commands and the presence of a PyMOL-compatible GLTF export function.

1.  **PyMOL Installation:** You must have PyMOL installed and its executable accessible from your system's command line.

## 📦 Installation and Setup

1.  Place the provided Python script (`pymol_export.py` or similar) and your target PDB file (e.g., `4WKQ.pdb`) into the same working directory.
2.  The script will automatically use the Current Working Directory (CWD) for file resolution.


## ▶️ Usage

The script is executed using the PyMOL command line interface in headless mode.

### Command Format

Use the `-c` (command line mode) and `-r` (run script) flags together, passing the input PDB file and the desired output GLTF file as arguments:

```bash
pymol -cr pymol_export.py <INPUT_PDB_NAME> <OUTPUT_GLTF_NAME>
```

### Example

The following command loads the structure `4WKQ.pdb`, applies the styles, and exports the final 3D model to `4WKQ_Output.gltf`.

```bash
pymol -cr pymol_export.py 4WKQ.pdb 4WKQ_Output.gltf
```

**Note on `-cr` Flag:** The combination of `-c` and `-r` ensures that PyMOL runs in a non-GUI (command-line) mode and executes the specified script, making it ideal for automated pipelines.