import requests

def get_latest_release_info(url_prefix, repo_owner_name, repo_name, url_suffix):
	url = "%s%s/%s%s" % (url_prefix, repo_owner_name, repo_name, url_suffix)

	response = requests.get(url)

	response_json = response.json()

	return response_json

def download_file_from_url(url, output_path, file_name, file_extension):
	response = requests.get(url, stream = True)

	download_path = "%s/%s%s" % (output_path, file_name, file_extension)

	if response.status_code == 200:

		with open(download_path, "wb") as file:
			for chunk in response.iter_content(chunk_size = 8192):
				file.write(chunk)

		print("Download was successful.")
	else:
		print("Download failed.")
