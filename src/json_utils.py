import json
from pathlib import Path


def write_json(path: str, network: dict) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        json.dump(network, f, indent=4, ensure_ascii=False)


def read_json(path: str) -> dict:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"File {path} does not exist")
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)
