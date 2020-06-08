import glob
import os

PANDA_1_1 = "E:\\Panda3D-1.1.0\\bin\\bam2egg.exe"
PANDA_1_11 = "C:\\Panda3D-1.11.0-x64\\bin\\egg2bam.exe"

for bam in glob.glob("**/*.bam", recursive=True):
    os.system(f"{PANDA_1_1} -o {bam[:-3] + 'egg'} {bam}")
    print(f"Decompiled: {bam}!")

for egg in glob.glob("**/*.egg", recursive=True):
    os.system(f"{PANDA_1_11} -o {egg[:-3] + 'bam'}  {egg}")
    os.remove(egg)
    print(f"Compiled: {egg}!")