import subprocess
from subprocess import run


def remove_pkg(name):
    try:
        command = 'dpkg --remove --force-remove-reinstreq ' + name
        p = run(command, shell=True, capture_output=True)
        lines = p.stdout.decode() + '\n' + p.stderr.decode()
        lines = lines.split('\n')
        rerun = False
        for l in lines:
            print("ERror", l)
            if "depends on" in l:
                rerun = True
                new_name = ''
                for i in range(10):
                    new_name = l.split(' ')[i]
                    if len(new_name) > 1:
                        break
                print("REmove ", new_name)
                remove_pkg(new_name)
        if rerun:
            run(command, shell=True, capture_output=True)

    except subprocess.CalledProcessError as e:
        print("start", e.output, "end")
        lines = e.output.decode("utf-8").split('\n')
        for l in lines:
            print("ERror", l)
            if "depends on" in l:
                remove_pkg(l.split(' ')[0])
    #  subprocess.check_output(
    #      ['dpkg', '--remove', '--force-remove-reinstreq', name])


if __name__ == "__main__":
    remove_pkg("libdrm-amdgpu1")
