
---

# PyMOL Molecular Visualization to GLTF Exporter

This utility provides a robust, headless (non-GUI) method to convert Protein Data Bank (PDB) files into high-quality, Mol*-styled 3D assets in the **glTF** format, ready for integration into web or mobile applications (e.g., Flutter).

## 🚀 Purpose

The script automates the process of loading a PDB file into PyMOL, applying standard molecular visualization (Cartoon for polymers, Ball & Stick for ligands), and exporting the resulting 3D geometry as a GLTF file—without launching the PyMOL graphical interface.

## 🛠️ Prerequisites

This script relies on PyMOL’s command execution functionality and a PyMOL-compatible GLTF export mechanism.

1. **PyMOL Installation:** Ensure that PyMOL is installed and accessible from your system’s command line.

## 📦 Installation and Setup

1. Place the provided Python script (`pymol_export.py` or similar) in any directory.
2. You may place your PDB files either:

   * in the **same working directory**,
   * or specify an **absolute** or **relative** path to them (see “Usage”).

The script can resolve both filenames and paths automatically.

## ▶️ Usage

Run the script using PyMOL’s headless mode:

### Command Format

```bash
pymol -cr pymol_export.py <INPUT_PDB_PATH> <OUTPUT_GLTF_PATH>
```

### ✔ File Path Options

You may supply:

* **A filename only**
  (Resolved relative to the current working directory)

* **A relative path**
  Example: `../data/4WKQ.pdb`

* **An absolute path**
  Example: `/home/user/proteins/4WKQ.pdb`

The same applies to the output GLTF path.

### Example: Filename Only

```bash
pymol -cr pymol_export.py 4WKQ.pdb 4WKQ_Output.gltf
```

### Example: Absolute Path

```bash
pymol -cr pymol_export.py /home/user/4WKQ.pdb /home/user/output/4WKQ_Output.gltf
```

**Note:** The `-cr` flags ensure that PyMOL runs in non-GUI mode and executes the script immediately, making this approach ideal for automation and pipelines.
