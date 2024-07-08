"""
 $ system-update --please --pretty-please-with-sugar-on-top
 Error: No space left on device

 Perhaps you can delete some files to make space for the update?

 find all of the directories with a total size of at most 100000
 then calculate the sum of their total sizes.

 PART 1: Calculate the sum of total sizes of those directories.

"""

### PART 1. --------------------------------------------------------------------------------------------------

with open('day07.txt', 'rt') as myfile:
    line = myfile.read()
    #print(line) ### reading file line by line
    line = line.splitlines() ### splitting lines and storing them in a list: ['$ cd /', '$ ls', ...]
    #print(line)
    """
    ['$ cd /', '$ ls', 'dir a', '14848514 b.txt', '8504156 c.dat', 'dir d', 
    '$ cd a', '$ ls', 'dir e', '29116 f', '2557 g', '62596 h.lst', '$ cd e', 
    '$ ls', '584 i', '$ cd ..', '$ cd ..', '$ cd d', '$ ls', '4060174 j', 
    '8033020 d.log', '5626152 d.ext', '7214296 k']
    """
    
    dirs = []  ### list of directories
    dic = {'/' : 0}
    size = 0

    for l in line:
        l = l.split()
        #print(l)

        if l[1] == 'ls':  ### ls means list. ---------------------------------------------------------------
                          ### It prints out all of the files and directories --------------------------------
                          ### immediately contained by the current directory ------------------------------
            #print('its ls!')
            continue  ### therefore, we continue to next line --------------------------------------------

        elif l[1] == 'cd':  ### cd: change directory ---------------------------------------------------
            #print('its cd!')
            if l[2] != '..':  ### go to previous directory -------------------------------------------
                #print('its not cd ..')
                #size = 0
                dirs.append(l[2]) ### appending all directories into a list: for eg ['/', 'a', 'e'] -----------
                el = ('/'.join(dirs)) ### //a/e ---------------------------------------------------------
                dic[el] = 0 ### intially size of //a/e is 0 -------------------------------------------------
                #print(dirs)
                size = 0
                #print(dic)

            else:  ### if l[2] == '..' then:

                #size = 0
                #print('we are popping')
                dirs.pop()  ### pop the last element: for eg ['/', 'a', 'e'] -> ['/', 'a']
                #print(dirs)
                el = ('/'.join(dirs)) ### => //a
                #print(el)
                #print(dic['/'.join(dirs)])
                #print(in_size)
                #print(dic[el])
                if el != '/': ### adding size of //a/e in size of //a as a containes e. -----------------------
                              ### adding only if 'a' is inside home directory '/' ----------------------------
                              ### because, we are already adding size of home directoy in the else condition---
                              ### o.w. it will be added two times --------------------------------------- 
                    dic[el] += size

#                print(dic)


        else: ### taking files inside the directory -------------------------------------------------------
            #print(l[0].isdigit())
            #print('/'.join(dirs))
            if l[0].isdigit() == True:  ### condition for files of some size -------------------------------
                #print(l[0])
                #print(dic)
                dic['/'] += int(l[0]) ### incrementing size of home directory -----------------------------
                #print(dic)
                #print('yes, its true')
                size += int(l[0]) ### incrementing size of current directory ---------------------------------
                dic['/'.join(dirs)] = size ### and adding it as a value in dictionary ------------------------
                #in_size = size + int(l[0])
                #print(dic)

            else:
                continue  

        #print(dic)

tot_size = 0
for key, val in dic.items():
    #print(val)
    if val <= 100000:
        #print(val)
        tot_size += val
print(tot_size)

