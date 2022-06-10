import os
import sys
import shutil
import json
import re
import subprocess

# CONSTANTS

GENERIC_JSONS_DIR: str = "generic_assets"
GENERIC_JSONS_DIR_PATH: str = os.path.join("./", GENERIC_JSONS_DIR)

FINAL_JSONS_DIR: str = "final_assets"
FINAL_JSONS_DIR_PATH: str = os.path.join("./", FINAL_JSONS_DIR)

# RUNTIME CONSTANTS

MODID_JSONS_DIR: str = sys.argv[1]
MODID_JSONS_DIR_PATH: str = os.path.join(FINAL_JSONS_DIR_PATH, MODID_JSONS_DIR)

DOOR_JSONS_DIR: str = sys.argv[2]
DOOR_JSONS_DIR_PATH: str = os.path.join(MODID_JSONS_DIR_PATH, DOOR_JSONS_DIR)

BLOCKSTATE_DICT: dict = \
    {
        "modid:block/door_bottom_left": sys.argv[1] + ":block/" + sys.argv[2] + "_bottom_left",
        "modid:block/door_bottom_left_open": sys.argv[1] + ":block/" + sys.argv[2] + "_bottom_left_open",
        "modid:block/door_bottom_right": sys.argv[1] + ":block/" + sys.argv[2] + "_bottom_right",
        "modid:block/door_bottom_right_open": sys.argv[1] + ":block/" + sys.argv[2] + "_bottom_right_open",
        "modid:block/door_top_left": sys.argv[1] + ":block/" + sys.argv[2] + "_top_left",
        "modid:block/door_top_left_open": sys.argv[1] + ":block/" + sys.argv[2] + "_top_left_open",
        "modid:block/door_top_right": sys.argv[1] + ":block/" + sys.argv[2] + "_top_right",
        "modid:block/door_top_right_open": sys.argv[1] + ":block/" + sys.argv[2] + "_top_right_open"
    }

TEXTURE_DICT: dict = \
    {
        "modid:block/door_bottom": sys.argv[1] + ":block/" + sys.argv[2] + "_bottom",
        "modid:block/door_top": sys.argv[1] + ":block/" + sys.argv[2] + "_top"
    }

MODEL_FILENAME_DICT: dict = \
    {
        "door_bottom_left.json": sys.argv[2] + "_bottom_left.json",
        "door_bottom_left_open.json": sys.argv[2] + "_bottom_left_open.json",
        "door_bottom_right.json": sys.argv[2] + "_bottom_right.json",
        "door_bottom_right_open.json": sys.argv[2] + "_bottom_right_open.json",
        "door_top_left.json": sys.argv[2] + "_top_left.json",
        "door_top_left_open.json": sys.argv[2] + "_top_left_open.json",
        "door_top_right.json": sys.argv[2] + "_top_right.json",
        "door_top_right_open.json": sys.argv[2] + "_top_right_open.json"
    }

# MODDING RUNTIME CONSTANTS
# assets/[modid]

MODDING_ASSETS_DIR: str = "assets"
MODDING_ASSETS_DIR_PATH: str = os.path.join(DOOR_JSONS_DIR_PATH, MODDING_ASSETS_DIR)

MODDING_MODID_DIR: str = sys.argv[1]
MODDING_MODID_DIR_PATH: str = os.path.join(MODDING_ASSETS_DIR_PATH, MODDING_MODID_DIR)

# assets/[modid]/blockstates

MODDING_BLOCKSTATES_DIR: str = "blockstates"
MODDING_BLOCKSTATES_DIR_PATH: str = os.path.join(MODDING_MODID_DIR_PATH, MODDING_BLOCKSTATES_DIR)

# assets/[modid]/models/block/

MODDING_MODELS_DIR: str = "models"
MODDING_MODELS_DIR_PATH: str = os.path.join(MODDING_MODID_DIR_PATH, MODDING_MODELS_DIR)

MODDING_MODELS_BLOCK_DIR: str = "block"
MODDING_MODELS_BLOCK_DIR_PATH: str = os.path.join(MODDING_MODELS_DIR_PATH, MODDING_MODELS_BLOCK_DIR)


# Create the folders for the resulting files

if not os.path.isdir(FINAL_JSONS_DIR_PATH):
    os.mkdir(FINAL_JSONS_DIR_PATH)

if not os.path.isdir(MODID_JSONS_DIR_PATH):
    os.mkdir(MODID_JSONS_DIR_PATH)

if not os.path.isdir(DOOR_JSONS_DIR_PATH):
    os.mkdir(DOOR_JSONS_DIR_PATH)
else:
    shutil.rmtree(DOOR_JSONS_DIR_PATH)
    os.mkdir(DOOR_JSONS_DIR_PATH)

os.mkdir(MODDING_ASSETS_DIR_PATH)
os.mkdir(MODDING_MODID_DIR_PATH)
os.mkdir(MODDING_BLOCKSTATES_DIR_PATH)
os.mkdir(MODDING_MODELS_DIR_PATH)
os.mkdir(MODDING_MODELS_BLOCK_DIR_PATH)

# Run json_manipulator.py to get the generic assets

subprocess.Popen([sys.executable, "json_manipulator.py"]).wait()

# Create blockstate file

with open(os.path.join(GENERIC_JSONS_DIR_PATH, "generic_door.json"), "r") as generic_door_blockstate_file:
    generic_door_blockstate = json.load(generic_door_blockstate_file)

door_blockstate = generic_door_blockstate

for orientation in door_blockstate["variants"]:
    door_blockstate["variants"][orientation]["model"] = BLOCKSTATE_DICT[door_blockstate["variants"][orientation]["model"]]

with open(os.path.join(MODDING_BLOCKSTATES_DIR_PATH, sys.argv[2] + ".json"), "w") as door_blockstate_file:
    json.dump(door_blockstate, door_blockstate_file, indent=2)

# Create model files

generic_door_model_files = os.listdir(GENERIC_JSONS_DIR_PATH)

for file in generic_door_model_files:
    if not re.search("door_", file):
        generic_door_model_files.remove(file)

for file in generic_door_model_files:
    with open(os.path.join(GENERIC_JSONS_DIR_PATH, file), "r") as generic_door_model_file:
        generic_door_model = json.load(generic_door_model_file)

    door_model = generic_door_model
    for texture in door_model["textures"]:
        door_model["textures"][texture] = TEXTURE_DICT[door_model["textures"][texture]]

    with open(os.path.join(MODDING_MODELS_BLOCK_DIR_PATH, MODEL_FILENAME_DICT[file]), "w") as door_model_file:
        json.dump(door_model, door_model_file, indent=2)
