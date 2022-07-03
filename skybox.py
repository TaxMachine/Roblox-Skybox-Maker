import os,glob,sys
from tabnanny import check

match sys.platform:
	case 'linux':
		robloxdir = glob.glob(f"{os.getenv('HOME')}/.local/share/grapejuice/prefixes/player/drive_c/users/{os.getenv('LOGNAME')}/AppData/Local/Roblox/Versions/version-*/PlatformContent/pc/textures/sky")[0]
	case 'win32':
		robloxdir = glob.glob(f"{os.getenv('LOCALAPPDATA')}/Roblox/Versions/version-*/PlatformContent/pc/textures/sky")[0]

class skybox:
	def checkdir():
		if not os.path.exists('./input'):
			os.mkdir('./input')
			print('You need to put images in the input directory')
			print("""
			Name Rules:
			- bk, back
			- ft, front
			- up
			- dn, down
			- rt, right
			- lf, left
			""")
			exit(1)
		elif len(os.listdir('./input')) == 0:
			print("There is no images in the input directory")
			exit(1)

	def makebox():
		skybox.checkdir()
		for files in os.listdir('./input'):
			if "up" in files:
				os.system(f'copy ./input/{files} ./input/sky512_up.dds')
				os.system(f'copy ./input/sky512_up.dds {robloxdir}/sky512_up.tex')
			elif "down" in files:
				os.system(f'copy ./input/{files} ./input/sky512_dn.dds')
				os.system(f'copy ./input/sky512_dn.dds {robloxdir}/sky512_dn.tex')
			elif "right" in files:
				os.system(f'copy ./input/{files} ./input/sky512_rt.dds')
				os.system(f'copy ./input/sky512_rt.dds {robloxdir}/sky512_rt.tex')
			elif "left" in files:
				os.system(f'copy ./input/{files} ./input/sky512_lf.dds')
				os.system(f'copy ./input/sky512_lf.dds {robloxdir}/sky512_lf.tex')
			elif "back" in files:
				os.system(f'copy ./input/{files} ./input/sky512_bk.dds')
				os.system(f'copy ./input/sky512_bk.dds {robloxdir}/sky512_bk.tex')
			elif "front" in files:
				os.system(f'copy ./input/{files} ./input/sky512_ft.dds')
				os.system(f'copy ./input/sky512_ft.dds {robloxdir}/sky512_ft.tex')
			else: continue
