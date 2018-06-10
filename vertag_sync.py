#!/usr/bin/env python
import subprocess as subp
from version import Version
import sys, re

def check_mod():
    pipe = subp.Popen(["git", "status"], stdout=subp.PIPE)
    lines = pipe.stdout.readlines()
    changed = False
    
    patt = re.compile("modified: ")
    for line in lines:
        if patt.search(line.decode()):
            changed = True
            break

    if changed:
        version = Version.strip()
        if version[-1] in ["*", "-"]:
            pass
        else:
            with open("version.py", 'w') as fpd:
                fpd.write(f'Version = "{version}*"\n')
            print(f"files modified and Version changed to '{version}*'\n")

    sys.exit(0)

###
def update_tag():
    pipe = subp.Popen(["git", "tag"], stdout=subp.PIPE)
    ver_tags = pipe.stdout.readlines()
    ver_tag = ver_tags[-1].decode().strip()
    ver_file = Version.strip()

    print('current tag/version:')
    print(f"  version in git-tag : {ver_tag}")
    print(f"  version in file: {ver_file}")

    if ver_file[-1] in ['*', '-']:
        ver_temp = ver_file[:-1]
    else:
        ver_temp = ver_file

    ans = input(f"New Version-Tag [{ver_file}]: ")
    if len(ans.strip()) == 0:
        ver_new = ver_temp
    else:
        ver_new = ans.strip()

    with open("version.py", 'w') as fpd:
        fpd.write(f'Version = "{ver_new}"\n')

    pipe = subp.Popen(["git", "commit", "-a", "-m", ver_new], 
                      stdout=subp.PIPE, stderr=subp.PIPE)

    std_err = pipe.stderr.read().decode().strip()
    std_out = pipe.stdout.read().decode().strip()

    print(f"git commit: \n {std_out}")
    if std_err:
        print(f"std_err: {std_err}")
        sys.exit()

    pipe = subp.Popen(["git", "tag", ver_new], stdout=subp.PIPE, 
                    stderr=subp.PIPE)

    pipe = subp.Popen(["git", "tag"], stdout=subp.PIPE, 
                    stderr=subp.PIPE)

    ver_tags = pipe.stdout.readlines()
    ver_tag = ver_tags[-1].decode().strip()

    print(f"tag: {ver_tag} has been set.")
    

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] in ["u", "up"]:
        update_tag()
    else:
        check_mod()
        
        
    
    
