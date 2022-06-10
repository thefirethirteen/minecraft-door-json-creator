import json
import os
import shutil
import re

# CONSTANTS

MINECRAFT_JSONS_DIR = "minecraft_assets"
MINECRAFT_JSONS_DIR_PATH = os.path.join("./", MINECRAFT_JSONS_DIR)

GENERIC_JSONS_DIR = "generic_assets"
GENERIC_JSONS_DIR_PATH = os.path.join("./", GENERIC_JSONS_DIR)

BLOCKSTATE_DICT = \
    {
        "minecraft:block/oak_door_bottom_left": "modid:block/door_bottom_left",
        "minecraft:block/oak_door_bottom_left_open": "modid:block/door_bottom_left_open",
        "minecraft:block/oak_door_bottom_right": "modid:block/door_bottom_right",
        "minecraft:block/oak_door_bottom_right_open": "modid:block/door_bottom_right_open",
        "minecraft:block/oak_door_top_left": "modid:block/door_top_left",
        "minecraft:block/oak_door_top_left_open": "modid:block/door_top_left_open",
        "minecraft:block/oak_door_top_right": "modid:block/door_top_right",
        "minecraft:block/oak_door_top_right_open": "modid:block/door_top_right_open"
    }

TEXTURE_DICT = \
    {
        "minecraft:block/oak_door_bottom": "modid:block/door_bottom",
        "minecraft:block/oak_door_top": "modid:block/door_top"
    }

MODEL_FILENAME_DICT = \
    {
        "oak_door_bottom_left.json": "door_bottom_left.json",
        "oak_door_bottom_left_open.json": "door_bottom_left_open.json",
        "oak_door_bottom_right.json": "door_bottom_right.json",
        "oak_door_bottom_right_open.json": "door_bottom_right_open.json",
        "oak_door_top_left.json": "door_top_left.json",
        "oak_door_top_left_open.json": "door_top_left_open.json",
        "oak_door_top_right.json": "door_top_right.json",
        "oak_door_top_right_open.json": "door_top_right_open.json"
    }

# Create a folder for the resulting files

if not os.path.isdir(GENERIC_JSONS_DIR_PATH):
    os.mkdir(GENERIC_JSONS_DIR_PATH)
else:
    shutil.rmtree(GENERIC_JSONS_DIR_PATH)
    os.mkdir(GENERIC_JSONS_DIR_PATH)

# Generic blockstate file

with open(os.path.join(MINECRAFT_JSONS_DIR_PATH, "oak_door.json"), "r") as oak_door_blockstate_file:
    oak_door_blockstate = json.load(oak_door_blockstate_file)

generic_door_blockstate = oak_door_blockstate

for orientation in generic_door_blockstate["variants"]:
    generic_door_blockstate["variants"][orientation]["model"] = BLOCKSTATE_DICT[generic_door_blockstate["variants"][orientation]["model"]]

with open(os.path.join(GENERIC_JSONS_DIR_PATH, "generic_door.json"), "w") as generic_door_blockstate_file:
    json.dump(generic_door_blockstate, generic_door_blockstate_file, indent=2)

# Generic model files

oak_door_model_files = os.listdir(MINECRAFT_JSONS_DIR_PATH)

for file in oak_door_model_files:
    if not re.search("oak_door_", file):
        oak_door_model_files.remove(file)

for file in oak_door_model_files:
    with open(os.path.join(MINECRAFT_JSONS_DIR_PATH, file), "r") as oak_door_model_file:
        oak_door_model = json.load(oak_door_model_file)

    generic_door_model = oak_door_model
    for texture in generic_door_model["textures"]:
        generic_door_model["textures"][texture] = TEXTURE_DICT[generic_door_model["textures"][texture]]

    with open(os.path.join(GENERIC_JSONS_DIR_PATH, MODEL_FILENAME_DICT[file]), "w") as generic_door_model_file:
        json.dump(generic_door_model, generic_door_model_file, indent=2)
