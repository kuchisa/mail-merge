# TODO: Create a letter using starting_letter.docx
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

def get_names():
    name_list = []
    with open("./Input/Names/invited_names.txt") as file:
        name_list = file.readlines()
        for i in range(0, len(name_list)):
            name_list[i] = name_list[i].strip("\n")
        return name_list


def create_letters():
    letters = []
    with open("./Input/Letters/letter.txt") as file:
        # get letter template
        content = file.read()
        
        # get names to replace in letter content
        names = get_names()
        for name in names:
            letter = content.replace("[name]", name)
            letters.append(letter)
            # print(letter)
        return letters


# save letters as Docx in specified directory
def save_letters_txt():
    names = get_names()
    letters = create_letters()
    for i in range(0, len(names)):
        with open(f"./Output/ReadyToSend/{names[i]}.txt", mode="w") as file:
            file.write(letters[i])


save_letters_txt()


