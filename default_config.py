from pathlib import Path

# absolute path to project directory
pp = Path(__file__).parent.absolute()

paths = {
    "data_path": 'your/path/to/the/dropbox/folder',  # Change this to where your downloaded hackathon data is located
    "cache_path": pp / "cache"
}
