import os
print("Unblocked Command Prompt by ThePiGuy24, because the admins decided to block the normal cmd...\n\nThere are a few changes,\nsuch as cd now accepts drive letters and doesn't give errors,\nbut other than that, its just regular cmd.\n")
os.chdir("C:\\Windows\\system32")
while True:
	command = input(os.getcwd()+">")
	if command.startswith("cd "):
		try:
			os.chdir(command.replace("cd ","",1))
		except:
			os.chdir(os.getcwd()+"\\"+command.replace("cd ","",1))
		finally:
			pass
	elif command.startswith("taskkill "):
		try:
			os.system(command.replace("taskkill ","C:\\windows\\system32\\taskkill.exe ",1))
		except:
			pass
	elif command.startswith("exit"):
		print("Closing...")
		quit()
	else:
		try:
			os.system(command)
		except:
			pass
