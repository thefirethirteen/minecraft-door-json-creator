# minecraft-door-json-creator
creates the necessary json files for correctly displaying door textures

## Requirements

- `python`
- Minecraft 1.19 client jar

You will need to provide the following files from the Minecraft jar into the `minecraft_assets` directory:
- from `assets/minecraft/blockstates`: 
  - `oak_door.json`
- from `assets/minecraft/models/block`:
  - `oak_door_bottom_left.json`
  - `oak_door_bottom_left_open.json`
  - `oak_door_bottom_right.json`
  - `oak_door_bottom_right_open.json`
  - `oak_door_top_left.json`
  - `oak_door_top_left_open.json`
  - `oak_door_top_right.json`
  - `oak_door_top_right_open.json`

# Usages:

## `creator.py`
creates the `final_assets` folder

`python creator.py [modid] [doorname]` where:
- `[modid]` is your mod's modid (e.g. `my_cool_mod`)
- `[doorname]` is the id of your door (e.g. `cooldoor` *not* `my_cool_mod:cooldoor`)

Notes:
- The `final_assets/[modid]/` and `final_assets/[modid]/[doorname]/` folders bear no significance to modding, but the `final_assets/[modid]/[doorname]/assets/` folder and its contents do (e.g you would find this exact folder with this exact file tree, in fabric's case, in `src/main/resources`.
- `creator.py` expects `json_manipulator.py` and `generic_assets/` (created by `json_manipulator.py`) to be present in the same directory
- running `creator.py` will remove the `final_assets/[modid]/[doorname]` folder if found
- `creator.py` runs `json_manipulator.py`

## `json_manipulator.py`
creates the `generic_assets` folder

`python json_manipulator.py`

Notes:
- *There is no need to run this yourself.*
- `json_manipulator.py` expects `minecraft_assets/` and the following files within it: 
`oak_door.json`
`oak_door_bottom_left.json`,
`oak_door_bottom_left_open.json`,
`oak_door_bottom_right.json`,
`oak_door_bottom_right_open.json`,
`oak_door_top_left.json`,
`oak_door_top_left_open.json`,
`oak_door_top_right.json`,
`oak_door_top_right_open.json`
to be present in the same directory
- running `json_manipulator.py` will remove the `generic_assets` folder if found

## `manual-cleanup.py`
cleans up ***only*** whatever the other scripts create

`python manual-cleanup.py`

## `manual-full-cleanup.py`
cleans up whatever the other scripts create ***and*** whatever the user provides

`python manual-full-cleanup.py`
