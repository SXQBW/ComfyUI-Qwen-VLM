import importlib.util
import os
import importlib
import sys
import subprocess
import folder_paths

supported_LLava_extensions = set(['.bin'])

try:
    folder_paths.folder_names_and_paths["QWEN"] = (folder_paths.folder_names_and_paths["QWEN"][0], supported_LLava_extensions)
except:
    # check if QWEN exists otherwise create
    if not os.path.isdir(os.path.join(folder_paths.models_dir, "QWEN")):
        os.mkdir(os.path.join(folder_paths.models_dir, "QWEN"))
        
    folder_paths.folder_names_and_paths["QWEN"] = ([os.path.join(folder_paths.models_dir, "QWEN")], supported_LLava_extensions)

# Define the check_requirements_installed function here or import it



node_list = [
    "QwenVLM",
]

NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

for module_name in node_list:
    imported_module = importlib.import_module(f".nodes.{module_name}", __name__)

    NODE_CLASS_MAPPINGS = {**NODE_CLASS_MAPPINGS, **imported_module.NODE_CLASS_MAPPINGS}
    NODE_DISPLAY_NAME_MAPPINGS = {**NODE_DISPLAY_NAME_MAPPINGS, **imported_module.NODE_DISPLAY_NAME_MAPPINGS}



