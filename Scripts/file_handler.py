from pathlib2 import Path
import yaml
import zipfile
import re
import os
import shutil

current_directory = Path(__file__).parent
manifest_file_path = current_directory/"manifest.yaml"

def convert_manifest_to_dict():
	with open(manifest_file_path) as file:
		return yaml.load(file, Loader = yaml.FullLoader)

def unzip_file(file_path):
	extract_path = re.sub(r"\.zip$", "", file_path)

	# This checks if extract_path already exists as a file/folder, and removes it if true
	# Should double confirm if we should proceed with this approach
	if os.path.exists(extract_path):
		if os.path.isdir(extract_path):
			shutil.rmtree(extract_path)
		else:
			os.remove(extract_path)
	
	with zipfile.ZipFile(file_path, "r") as zip_ref:
		zip_ref.extractall(extract_path)

	return extract_path
