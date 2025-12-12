# Version: 1.1.0

from pymol import cmd 
import os
import sys

# --- Configuration ---
try:
    # Get the directory of the running script
    SCRIPT_DIR = os.getcwd()
except Exception:
    # Fallback if running interactively or path is not available
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# --- Argument Parsing ---

def parse_arguments():
    """
    Parses command-line arguments for input PDB and output GLTF filenames.
    """
    # sys.argv[0] is the script name. We need 2 more arguments.
    if len(sys.argv) < 5:
        print("\n❌ ERROR: Missing required arguments.")
        print(f"Usage: pymol -cr {os.path.basename(__file__)} <INPUT_PDB_NAME> <OUTPUT_GLTF_NAME>")
        print("Example: pymol -cr export_gltf_final_cli.py 4WKQ.pdb styled_4WKQ.gltf")
        # Close PyMOL session and exit with error code.
        cmd.quit()
        sys.exit(1)
        
    pdb_filename = sys.argv[3]
    output_filename = sys.argv[4]
    
    # Ensure the output filename has the correct extension
    if not output_filename.lower().endswith(('.gltf')):
        output_filename += '.gltf'
        
    return pdb_filename, output_filename

# Get arguments
PDB_FILENAME, OUTPUT_FILENAME = parse_arguments()

def resolve_path(path, base_dir):
    """
    If `path` is absolute, return it unchanged.
    If `path` is relative, resolve it relative to `base_dir`.
    """
    if os.path.isabs(path):
        return path
    return os.path.join(base_dir, path)

# Resolve input and output paths
PDB_FILE_PATH = os.path.normpath(resolve_path(PDB_FILENAME, SCRIPT_DIR))
OUTPUT_GLTF_PATH = os.path.normpath(resolve_path(OUTPUT_FILENAME, SCRIPT_DIR))


# --- Main PyMOL Execution Block ---

print(f"--- PyMOL Export Utility ---")
print(f"Base Directory: {SCRIPT_DIR}")
print(f"Loading: {PDB_FILE_PATH}")

try:
    # 1. Load the structure
    cmd.load(PDB_FILE_PATH, 'mol')
    
    # Check if the file loaded successfully
    if 'mol' not in cmd.get_names():
        raise FileNotFoundError(f"Could not load PDB file: {PDB_FILE_PATH}")

    # 2. Export the styled scene
    print(f"Exporting styled scene to: {OUTPUT_GLTF_PATH}")
    cmd.save(OUTPUT_GLTF_PATH) 
    
    print(f"✅ Success: Scene saved to {OUTPUT_GLTF_PATH}")
    
except FileNotFoundError as e:
    print(f"❌ ERROR: File not found or failed to load. Details: {e}")
    sys.exit(1) # Exit with error code

except Exception as e:
    print(f"❌ A critical error occurred during PyMOL scripting or export: {e}")
    sys.exit(1) # Exit with error code

finally:
    # 3. Quit the PyMOL session cleanly, regardless of success or failure
    cmd.quit() 
    print("PyMOL session closed.")