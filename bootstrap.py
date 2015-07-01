#!/usr/bin/python
#
# TODO:
# In /CMakeLists.txt
# - replace "github_user" with your github's user name
import sys
import subprocess
import argparse

# List of files in which the project name should be replaced as is and in
# capitalized form
replace_project_name_files = ['CMakeLists.txt',
                              'test/CMakeLists.txt',
                              'example/CMakeLists.txt',
                              'include/project_name/project_name.hpp',
                              'include/project_name/test_header.hpp',
                              'include/project_name/component/component_header.hpp',
                              'test/test_b.cpp',
                              'test/component/test_a.cpp',
                              '.travis.yml']

# Replaced `project_name` and `PROJECT_NAME` by the desired project_name
# in the files specified in `replace_project_name_files`
def apply_project_name(project_name):
    for file_path in replace_project_name_files:
        print("reading " + file_path)
        fstr = open(file_path).read()
        fstr = fstr.replace('project_name', project_name)
        fstr = fstr.replace('project_name'.upper(), project_name.upper())
        fstr = fstr.replace('cpp_skeleton', project_name)
        f = open(file_path, 'w')
        f.write(fstr)
        f.flush()
        f.close()

    subprocess.call(["git", "mv", 'include/project_name', 'include/' + project_name])


def main(argv=None):
    parser = argparse.ArgumentParser(description='Bootstrap a new C++ project.')
    parser.add_argument('project_name', help='The name of the project')

    args = parser.parse_args()
    apply_project_name(args.project_name)

if __name__ == "__main__":
    sys.exit(main())
