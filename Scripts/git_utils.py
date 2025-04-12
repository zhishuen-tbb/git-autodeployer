class VersionDetails:
	version_tuple: tuple[int, int, int]
	asset_download_link: str | None

	def __init__(self, version_tuple, asset_download_link = None):
		self.version_tuple = version_tuple
		self.asset_download_link = asset_download_link

def is_remote_version_newer(remote_version_details: "VersionDetails", local_version_details: "VersionDetails"):
	if (remote_version_details.version_tuple > local_version_details.version_tuple):
		return True
	else:
		return False

def parse_version(version_string):
	parts = version_string.lstrip("v").split(".")

	return tuple(map(int, parts))
