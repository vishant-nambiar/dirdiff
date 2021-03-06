# dirdiff

-----------------------------------------------------------------

**Note**:The following is documentation on the dirdiff python **package** available [here](https://pypi.org/project/dirdiff/1.1/). If you want to know about dirdiff as a **CLI**, go to [README2](https://github.com/vishant-nambiar/dirdiff/blob/main/README2.md). 

A python utility to diff and patch directories. It's similar to the diff and patch tools in \*nix command lines, but for **directories**. I wrote it because I couldn't find a simple hassle free tool to store the differences between two directories that can be used as instructions to convert one directory to another.

## How it works

------------------------------

There are two main actions you can perform with dirdiff: **diffing** and **patching**.
If you have two directories A and B, you can diff A with respect to B. This creates a diff dictionary, which is essentially an object of instructions that can be used to convert A to B. Here, A would be called the base directory and B would be called the compare directory.
When you have generated the diffs required to convert A to B, you can use these diffs to patch A whenever you want. The instructions in the diff object would be applied to A, and after patching, A would be identical to B. This is of course valid for a series of files, i.e if you are working on a file and save it as A, then B, then C, you could diff A and B, then B and C, finally you could combine these diffs to get instructions to convert A to C.

## How to use it

------------------------------------------------

**Note**: Python3 is required to run dirdiff. dirdiff is designed to run on *nix systems with bash. It may work for Windows with WSL, but I haven't verified it.

The two major actions you can perform are directory diffing and patching. Accordingly these two functions have been exposed:
- `generate_dir_diffs`: Takes two mandatory arguments, `base_dir`, which is the path to the base directory, and `comp_dir`, which is the path to the directory with which the diffs must be generated. The paths can be relative or absolute. Returns a dictionary `diff_object`, which contains instructions to convert the base directory to the compare directory. This can be stored or passed to the `dir_patch` function to patch the base directory.
- `dir_patch`: Takes two mandatory arguments. The first is the path to the base directory to be patched, the next is the diff dictionary to be applied to the directory.
Examples:
`diff_dict = generate_dir_diffs( base_dir_path, comp_dir_path )`
`dir_patch( base_dir_path, diff_dict )`

## Reusable components

--------------------------------------------

- function `bash_execute`: Runs any number of bash commands passed as a string, each on one line, and returns the output of the last command.
- function `generate_dir_diffs`: Generates diff objects passed based on the paths of base directory and compare directory provided.
- function `generate_file_diffs`: Generates file diff objects (a subset of the diff object) which contains instructions to patch only the files in the base directory from the compare directory, ignoring the directories inside them.
- function `dir_patch`: Takes a directory path and a diff object, and patches that directory according to the instructions in the diff object.

## Dependencies
------------------------------------------------
dirdiff uses only a python standard library, specifically subprocess.

## Known issues

------------------------------------------

dirdiff currently does not work for binary files. This will be fixed soon.
If you get problems, let me know by raising an issue.

## Licensing
--------------------------------------------
This project is covered under the [GNU General Public License V3](https://www.gnu.org/licenses/gpl-3.0.en.html).
