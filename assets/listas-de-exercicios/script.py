import subprocess
import os
resolucoes = [x for x in os.listdir('.') if x.startswith('resolucao') and os.path.isdir(x)]
for f in resolucoes:
    cmd = ['zip','-r',f+'.zip',f]
    print(cmd)
    subprocess.run(cmd)
