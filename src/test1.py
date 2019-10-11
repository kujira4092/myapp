import subprocess

out = subprocess.check_output(["arduino-cli","board","list"])
out = str(out)

boardlist = ["Uno","mega"]

for x in range(5):
    if "Arduino/Genuino Mega or Mega 2560" in out:
        boardname = "Arduino/Genuino Mega or Mega 2560"

print(boardname)
