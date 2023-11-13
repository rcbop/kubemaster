""" bumps a version number based on the argument passed in """
import sys

import semver


def bump_version(part, version):
    try:
        ver = semver.Version.parse(version)
        if part == 'PATCH':
            new_version = ver.bump_patch()
        elif part == 'MINOR':
            new_version = ver.bump_minor()
        elif part == 'MAJOR':
            new_version = ver.bump_major()
        else:
            print("Invalid argument. Please use PATCH, MINOR, or MAJOR.")
            return

        print(str(new_version))
    except ValueError as e:
        print(f"Error parsing version: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./my_script.py <PART> <VERSION>")
        sys.exit(1)

    part = sys.argv[1]
    version = sys.argv[2]

    bump_version(part, version)
