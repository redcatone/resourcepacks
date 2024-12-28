# Simple script to create resource pack zips for multiple Minecraft version

import pathlib
import zipfile
import json

# What resource packs to export
RESOURCE_PACKS = {
    "vanillacrate": {
        "pack": {
            "description": "Retextures Immersive Engineering's crate to vanilla chest texture"
        }
    },
}

# Mapping of Resource Pack versions to their Minecraft versions
# https://minecraft.wiki/w/Pack_format#List_of_resource_pack_formats
VERSIONS = {
    1: "1.6.1-1.8.9",
    2: "1.9-1.10.2",
    3: "1.11-1.12.2",
    4: "1.13-1.14.4",
    5: "1.15-1.16.1",
    6: "1.16.2-1.16.5",
    7: "1.17-1.17.1",
    8: "1.18-1.18.2",
    9: "1.19-1.19.2",
    12: "1.19.3",
    13: "1.19.4",
    15: "1.20-1.20.1",
    18: "1.20.2",
    22: "1.20.3-1.20.4",
    32: "1.20.5-1.20.6",
    34: "1.21-1.21.1",
    42: "1.21.2-1.21.3",
    46: "1.21.4"
}


for resource_pack_name, mcmeta in RESOURCE_PACKS.items():
    base_directory = pathlib.Path(__file__).parent.parent.resolve()  # first parent is "script" directory, second parent is repo directory
    for version in VERSIONS:
        mcmeta = mcmeta.copy()
        mcmeta["pack"]["pack_format"] = version
        zip_path = base_directory / pathlib.Path(f"releases/{resource_pack_name}-{VERSIONS[version]}.zip")
        with zipfile.ZipFile(zip_path, "w") as zip:
            zip.writestr("pack.mcmeta", json.dumps(mcmeta, indent=4))
            assets_path = base_directory / pathlib.Path(f"{resource_pack_name}/src/assets")
            for path in assets_path.rglob("*.*"):
                zip.write(path, arcname=path.relative_to(assets_path.parent))
