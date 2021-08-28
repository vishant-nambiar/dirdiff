import subprocess

#Executes any number of bash commands, one on each line
def bash_execute(commands):
    commands = commands.split('\n')
    last_output = ''
    for command in commands:
        last_output = subprocess.run(command.split(' '), stdout=subprocess.PIPE, text=True).stdout
    return last_output




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
    files_to_add = []  #format: [[fiilename, file content], ...]
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
            files_to_add.append([file, file_content])
    for file, data in files_to_add:
        comp_dir_list.remove(file)


    #list diffs of the files which have same names
    for file in base_dir_list:
        file_diff = bash_execute(f"diff {base_dir}/{file} {comp_dir}/{file}")
        diffs_similar_files.append([file, file_diff])


    #packaging everything into a diff dictionary
    diff = {"files_to_add": files_to_add, "files_to_delete": files_to_delete, "file_diffs": diffs_similar_files}
    return diff











#generates instructions to build dir
def dir_build_instructions(dir):
    dir_file_list = generate_file_list(dir)
    dir_dir_list = generate_dir_list(dir)
