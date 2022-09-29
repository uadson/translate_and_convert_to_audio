import os
from pathlib import Path


BASE = Path(__file__).resolve().parent.parent


def search():
	path_dir = os.listdir(BASE)
	for i in range(len(path_dir)):
		if path_dir[i] == 'media':
			return i


def get_media_folder():
	media_dir = search()
	path_dir = os.listdir(BASE)
	return path_dir[media_dir]


def get_audio_file(file):
	file = f"{file}.mp3"
	media_folder = get_media_folder()
	media_path = os.path.join(BASE, media_folder)
	audio = os.path.join(media_path, file)
	return audio


def delete_file(file):
	file = f"{file}.mp3"
	media_folder = get_media_folder()
	media_path = os.path.join(BASE, media_folder)
	media = os.path.join(media_path, file)
	os.remove(media)
