#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

letter_tex = []
name_list = []
with open("Input/Letters/starting_letter.txt", mode="r") as letter:
    for x in letter.readlines():
        letter_tex.append(x)
print(letter_tex)
with open("Input/Names/invited_names.txt", mode="r") as name:
    for x in name.readlines():
        name_list.append(x[:-2])
print(name_list)
for x in name_list:
    letter_tex[0] = x
    with open(f"Output/ReadyToSend/invited_{x}.txt", mode="w") as new_file:
        for x in letter_tex:
            new_file.write(x)