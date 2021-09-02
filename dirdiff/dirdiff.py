#!/usr/bin/env python3


import subprocess



#Executes any number of bash commands, one on each line
def bash_execute(commands):
    commands = commands.split('\n')
    last_output = ''
    for command in commands:
        last_output = subprocess.run(command.split(' '), stdout=subprocess.PIPE, text=True).stdout
    return last_output





#Diffing supporting functions



#generates array of files
def generate_file_list(dir):
    dir_data = bash_execute(f'ls -pa {dir}/').split('\n')[:-1]
    dir_list = []
    for name in dir_data:
        if not name[-1] == '/':
            dir_list.append(name)
    return dir_list



#generates array of directories
def generate_dir_list(dir):
    data = bash_execute(f'ls -pa {dir}/').split('\n')[2:-1]
    dir_list = []
    for name in data:
        if name[-1] == '/':
            dir_list.append(name[:-1])
    return dir_list



def generate_file_diffs( base_dir, comp_dir ):
    
    base_dir_list = generate_file_list(base_dir)
    comp_dir_list = generate_file_list(comp_dir)

    

    files_to_delete = []
    files_to_add = []  #format: array of build objects
    diffs_similar_files = [] #format: [[fiilename, diff info], ...]

    
    #When basefile has an additional file
    for file in base_dir_list:
        if file not in comp_dir_list:
            files_to_delete.append(file)
    for file in files_to_delete:
        base_dir_list.remove(file)

    #when compfile has an additional file
    for file in comp_dir_list:
        if file not in base_dir_list:
            file_content = bash_execute(f"cat {comp_dir}/{file}")
            files_to_add.append( {"name": file, "category": "file", "content": file_content})
    for build_objects in files_to_add:
        comp_dir_list.remove(build_objects["name"])


    #list diffs of the files which have same names
    for file in base_dir_list:
        file_diff = bash_execute(f"diff {base_dir}/{file} {comp_dir}/{file}")
        diffs_similar_files.append([file, file_diff])


    #packaging everything into a diff dictionary
    diff = {"files_to_add": files_to_add, "files_to_delete": files_to_delete, "file_diffs": diffs_similar_files}
    return diff




#generates instructions to build dir from scratch
#returns an array of build objects
def dir_build_instructions(dir):
    dir_file_list = generate_file_list(dir)
    dir_dir_list = generate_dir_list(dir)

    store = []
    
    for file in dir_file_list:
        name = file
        category = "file"
        content = bash_execute(f"cat {dir}/{file}")
        store.append( {"name": name, "category": category, "content": content} )
    
    for inner_dir in dir_dir_list:
        name = inner_dir
        category = "directory"
        content = dir_build_instructions(f"{dir}/{inner_dir}")
        store.append( {"name": name, "category": category, "content": content} )
    return store



def generate_dir_diffs(base_dir, comp_dir):

    file_diff_object = generate_file_diffs( base_dir, comp_dir )

    base_dir_dirs = generate_dir_list(base_dir)
    comp_dir_dirs = generate_dir_list(comp_dir)

    dirs_to_delete = []
    dirs_to_build = [] #format:  array of build objects
    same_dir_diffs = [] #format: [ [dir, dir_diff_object] ]

    #list dirs in base dir not in comp dir
    for dir in base_dir_dirs:
        if dir not in comp_dir_dirs:
            dirs_to_delete.append(dir)

    for dir in dirs_to_delete:
        base_dir_dirs.remove(dir)

    #list dirs to build along with build instructions for dirs in comp dir not in base dir
    for dir in comp_dir_dirs:
        if dir not in base_dir_dirs:
            build_instructions = dir_build_instructions(f"{comp_dir}/{dir}")
            build_object = {"name": dir, "category": "directory", "content": build_instructions}
            dirs_to_build.append(build_object)

    for build_object in dirs_to_build:
        comp_dir_dirs.remove(build_object["name"])


    #diffs of dirs that are the same in both dirs
    for dir in base_dir_dirs:
        base_dir_dir = f"{base_dir}/{dir}"
        comp_dir_dir = f"{comp_dir}/{dir}"
        dir_diff_object = generate_dir_diffs( base_dir_dir, comp_dir_dir)
        same_dir_diffs.append( [dir, dir_diff_object] )

    dir_diff_object = {"dirs_to_build": dirs_to_build, "dirs_to_delete": dirs_to_delete, "dir_diffs": same_dir_diffs}

    return {"files": file_diff_object, "dirs": dir_diff_object}





#Patching supporting functions


def build(dir, build_objects):
    for build_object in build_objects:
        if build_object["category"] == "file":
            name = build_object['name']
            bash_execute(f"touch {dir}/{name}")
            file = open(f"{dir}/{name}", "w")
            file.write( build_object["content"] )
            file.close()
        
        if build_object["category"] == "directory":
            name = build_object["name"]
            bash_execute(f"mkdir {dir}/{name}")
            build( f"{dir}/{name}", build_object["content"] )



def dir_patch(dir, dir_diff_object):
        
        file_object = dir_diff_object["files"]
        
        for file in file_object["files_to_delete"]:
            bash_execute(f"rm {dir}/{file}")
        
        build(dir, file_object["files_to_add"])

        bash_execute(f"touch {dir}/temppatch8132")
        for file, diff in file_object["file_diffs"]:
            temp_patch_file = open(f"{dir}/temppatch8132", "w")
            temp_patch_file.write(diff)
            temp_patch_file.close()
            bash_execute(f"patch {dir}/{file} {dir}/temppatch8132")
        bash_execute(f"rm {dir}/temppatch8132")


        
        dir_object = dir_diff_object["dirs"]

        for directory in dir_object["dirs_to_delete"]:
            bash_execute(f"rm -r {dir}/{directory}")
        
        build( dir, dir_object["dirs_to_build"] )

        for directory, directory_diff_object in dir_object["dir_diffs"]:
            dir_patch( f"{dir}/{directory}", directory_diff_object )

