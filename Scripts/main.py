import git_utils
import requests_manager
import file_handler

# Load local manifest
local_manifest_dict = file_handler.convert_manifest_to_dict()

# Query Git API for latest release info
response_json = requests_manager.get_latest_release_info(local_manifest_dict["url_prefix"], local_manifest_dict["repo_owner_name"], 
												local_manifest_dict["repo_name"], local_manifest_dict["url_suffix"]);

# Get remote release tag and first asset download link
remote_asset_download_link = response_json["assets"][0]["browser_download_url"]
remote_version_tuple = git_utils.parse_version(response_json["tag_name"])

# Create VersionDetails object for remote release
remote_version_details = git_utils.VersionDetails(remote_version_tuple, remote_asset_download_link)

# Get local release tag
local_version_tuple = git_utils.parse_version(local_manifest_dict["local_version"])

# Create VersionDetails object for local release
# Maybe add local_asset_download_link too and instead of checking version numbers, just compare download links?
local_version_details = git_utils.VersionDetails(local_version_tuple)

def main():
	if (git_utils.is_remote_version_newer(remote_version_details, local_version_details)):
		# Update required, start download latest version
		print("Update required")
		downloaded_file_path = requests_manager.download_file_from_url(remote_version_details.asset_download_link, file_handler.current_directory, 
																 local_manifest_dict["download_file_name"], local_manifest_dict["download_file_extension"])
	
		# Unzip downloaded file
		extracted_file_path = file_handler.unzip_file(downloaded_file_path)
	else:
		# Update not required, proceed to start game
		print("Update not required")

if __name__ == "__main__":
	main()
