#!/usr/bin/env python3
import datetime
import json
from pathlib import Path

with Path("data/oc.json").open() as f:
    data: list = json.load(f)

existing = {x["id"] for x in data}

for filename in Path("assets").glob("*.png"):
    if "_" in filename.stem:
        stripped = filename.with_stem(filename.stem.split("_", 1)[0])
        filename.rename(stripped)
        filename = stripped
    ident = int(filename.stem)
    if ident not in existing:
        data.insert(0, {"id": ident, "dt": datetime.datetime.now().astimezone().isoformat()})

with Path("data/oc.json.new").open("w") as f:
    json.dump(data, f, indent=2)

Path("data/oc.json.new").rename("data/oc.json")
