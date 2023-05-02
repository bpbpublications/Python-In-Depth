
import subprocess
from pprint import pprint

def exec_command(cmd, output_option=False):
    if output_option:
        out = subprocess.check_output(cmd, shell=True)
        return out
    else:
        code = subprocess.call(cmd, shell=True)
        return code


if __name__ == '__main__':
    print("Exemple 1:")
    print()
    code = exec_command("ls -l")
    print(f"Return code: {code}")

    print()

    print("Exemple 2:")
    print()
    out = exec_command("ls", output_option=True)
    pprint(out.decode("utf-8").split("\n"))
