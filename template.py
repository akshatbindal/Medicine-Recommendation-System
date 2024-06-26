import os
from pathlib import Path

list_of_files = [
    f"src/__init__.py",
    f"src/components/__init__.py",
    f"src/pipeline/__init__.py",
    f"src/utils",
    f"src/logger.py",
    f"src/exception.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
    "app.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass