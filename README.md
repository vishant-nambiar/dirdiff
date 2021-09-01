# Dirdiff

-----------------------------------------------------------------

A python script to diff and patch directories. It's similar to the diff and patch tools in \*nix command lines, but for **directories**. I wrote it because I couldn't find a simple hassle free tool to store the differences between two directories that can be used as instructions to convert one directory to another.

## How it works

------------------------------

There are two main actions you can perform with dirdiff: **diffing** and **patching**.
If you have two directories A and B, you can diff A with respect to B. This creates a diff object in Json format, which is essentially an object of instructions that can be used to convert A to B. These instructions can be printed on the terminal or stored in a file.
When you have generated the diffs required to convert A to B, you can use these diffs to patch A whenever you want. The instructions in the diff object would be applied to A, and after patching, A would be identical to B. This is of course valid for a series of files, i.e if you are working on a file and save it as A, then B, then C, you could diff A and B, then B and C, finally you could combine these diffs to get instructions to convert A to C.

## How to use it

------------------------------------------------

**Note:** Python3 is required to run dirdiff. Also I've tested it on Linux and MacOS so far, as it runs only on *nix systems. I believe it may work with WSL for Windows, but I haven't verified it.

The tool has been written as a script to be run in the terminal. Simply run the `dirdiff` script with the neccessary arguments. These are, in order:
 - `command`: The values for this are `diff` and `patch`, based on what you're trying to do.
 - `base_directory`: The relative or absolute path of the base directory we would like to diff or patch. In the example above, the base directory would've been A.
 - `compare_directory`: This must be supplied only when diffing. This is the path to the directory with respect to which we would like to generate diffs for the base directory. In the example above it would've been B.
 - `patch_file`: **If diffing**, this is the file that where the generated diffs would be stored. If not provided, the diffs would be printed in the terminal. **If patching**, this is a mandatory parameter as the patch instructions would be taken from the file provided.
 
For example, if we were diffing A with respect to B, the command would be:
`./dirdiff diff A B`
This would print the diff object onto the terminal. To store it in a file, say `file.patch`, we would have to run:
`./dirdiff diff A B file.patch`
Finally, after we've generated the diffs, we can patch the base directory (A in this case), by doing:
`./dirdiff patch A file.patch`
The result would be that A has been made identical to B.

## Reusable components

--------------------------------------------

- function `bash_execute`: Runs any number of bash commands passed as a string, each on one line, and returns the output of the last command.
- function `generate_dir_diffs`: Generates diff objects passed based on the paths of base directory and compare directory provided.
- function `generate_file_diffs`: Generates file diff objects (a subset of the diff object) which contains instructions to patch only the files in the base directory from the compare directory, ignoring the directories inside them.
- function `dir_patch`: Takes a directory path and a diff object, and patches that directory according to the instructions in the diff object.


## Known issues

------------------------------------------

Dirdiff currently does not work for binary files. This will be fixed soon.
If you get problems, let me know by raising an issue.

## Licensing
--------------------------------------------
This project is covered under the [GNU General Public License V3](https://www.gnu.org/licenses/gpl-3.0.en.html).
