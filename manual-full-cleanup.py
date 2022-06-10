import os
import shutil
import re

# Provided by the user, CONSTANTS from json_manipulator.py

MINECRAFT_JSONS_DIR = "minecraft_assets"
MINECRAFT_JSONS_DIR_PATH = os.path.join("./", MINECRAFT_JSONS_DIR)

user_provided_files = os.listdir(MINECRAFT_JSONS_DIR_PATH)

for file in user_provided_files:
    if not re.search(".json", file):
        user_provided_files.remove(file)

for file in user_provided_files:
    os.remove(os.path.join(MINECRAFT_JSONS_DIR_PATH, file))

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
