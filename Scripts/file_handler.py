from pathlib2 import Path
import yaml

current_directory = Path(__file__).parent
manifest_file_path = current_directory/"manifest.yaml"

def convert_manifest_to_dict():
	with open(manifest_file_path) as file:
		return yaml.load(file, Loader = yaml.FullLoader)
