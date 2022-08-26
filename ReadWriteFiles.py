
def write_to_file():
    user_file = input('Enter file name: ')
    with open(user_file + '.txt', 'w') as open_file:
        user_file_text = input('What would you like to say in your file?')
        open_file.write(user_file_text)
#FIXME
def read_file():
    count = 0
    list_lines = []
    file_name = input('Enter filename')
    name_count = dict()

    with open(file_name, 'r') as open_file:

        #get list of lines in file
        list_lines = open_file.readlines()

        #seperate each line/element into multiple string to extract name to count
        for x in range(list_lines):
            list_lines[x] = list_lines[x].split("/")


        for x in range(len(list_lines)):
            line_count = 0

            #if at the last index, check if its the same name as previous. If not, make new dict entry
            #   (if it was the same, it would have accounted for it in the previous loop iteration
            if x == len(list_lines) - 1:
                if list_lines[x] != list_lines[x - 1]:
                    name_count[list_lines[x]] = 1

            #if line == next line--> count++, loop++
            else:
                while list_lines[x] == list_lines[x + 1]:
                    line_count += 1
                    x += 1

                #dict entry for name and count
                name_count[list_lines[x]] = line_count
    print(name_count)
