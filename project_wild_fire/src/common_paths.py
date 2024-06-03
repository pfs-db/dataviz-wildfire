from pathlib import Path


PROJECT_NAME = "project_wild_fire"
current_directory = Path.cwd().parents
PROJECT_PATH = current_directory[0].joinpath(PROJECT_NAME)
DATA_PATH = PROJECT_PATH.joinpath("data")
DOCS_PATH = PROJECT_PATH.joinpath("docs")
OUTPUT_PATH = PROJECT_PATH.joinpath("output")
SAMPLE_PATH = PROJECT_PATH.joinpath("sample")
# DATA = PATH()
