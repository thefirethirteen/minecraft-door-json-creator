import os
import shutil

# Created by json_manipulator.py

GENERIC_JSONS_DIR = "generic_assets"
GENERIC_JSONS_DIR_PATH = os.path.join("./", GENERIC_JSONS_DIR)

if os.path.isdir(GENERIC_JSONS_DIR_PATH):
    shutil.rmtree(GENERIC_JSONS_DIR_PATH)

# Created by creator.py

FINAL_JSONS_DIR: str = "final_assets"
FINAL_JSONS_DIR_PATH: str = os.path.join("./", FINAL_JSONS_DIR)

if os.path.isdir(FINAL_JSONS_DIR_PATH):
    shutil.rmtree(FINAL_JSONS_DIR_PATH)
