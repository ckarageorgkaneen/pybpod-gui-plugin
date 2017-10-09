
import shutil
from send2trash import send2trash as send2trash_original


def send2trash(path):
	try:
		send2trash_original(path)
	except:
		shutil.rmtree(path)