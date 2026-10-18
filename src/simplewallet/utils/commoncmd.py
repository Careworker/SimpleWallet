import shlex; import subprocess
from os import getcwd, listdir
from os.path import isfile, isdir
from ..dircrawler.crawler import Crawler

class CommonCmd:

	@classmethod
	def pwd(self, internal: bool = False) -> str:
		if internal: return Crawler.posixize(getcwd())

		command = 'pwd'
		process = subprocess.run(command,
			stdout=subprocess.PIPE,stderr=subprocess.PIPE)
		returncode = process.returncode
		result = Crawler.posixize(process.stdout.decode().rstrip('\n'))
		if returncode == 0:
			return result
		else:
			return ''

	@classmethod
	def ls(self) -> list:
		files = [f for f in listdir('.') if isfile(f)]
		folders = [d for d in listdir('.') if isdir(d)]
		files.sort()
		folders.sort()
		return folders + files

	@classmethod
	def clear(self):
		subprocess.call('clear')

	@classmethod
	def copyfile(self, curr_filepath: str, new_filepath: str) -> dict:

		cfile = Crawler.escape(Crawler.posixize(curr_filepath))
		nfile = Crawler.escape(Crawler.posixize(new_filepath))

		command = shlex.split('cp {c} {n}'.format(c=cfile,n=nfile))
		process = subprocess.run(command,
			stdout=subprocess.PIPE,stderr=subprocess.PIPE)
		returncode = process.returncode
		if returncode == 0:
			return {'status': 200, 'message': 'File created: ' + str(new_filepath)}
		else:
			return {'status': 400, 'message': 'Error creating file for: ' + str(curr_filepath)}
