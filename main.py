# mailMerge.py
#
# Python Bootcamp Day 24 - Mail Merge Program
# Usage:
#      Read from a flat file of names and merge onto letter, finally write merged letters
#      to separate files.
#
# Marceia Egler November 22, 2021


# THE HARD WAY

# names = []
# salutation = []
# letter = ""

# with open("./Input/Names/invited_names.txt") as f:
#     lines = f.readlines()
#     for name in lines:
#         names.append(name.strip())

# with open("./Input/Letters/starting_letter.txt") as f:
#     lines = f.readlines()
#     for line in lines[1:]:
#         letter += line
#     for name in names:
#         line1 = lines[0].replace("[name]", name)
#         salutation.append(line1)
#         for i, value in enumerate(salutation):
#             with open(
#                 f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w"
#             ) as f:
#                 f.write(f"{value} {letter}")

# THE MUCH EASIER WAY

with open("./Input/Names/invited_names.txt") as f:
    names = f.readlines()

with open("./Input/Letters/starting_letter.txt") as f:
    letter = f.read()
    for name in names:
        strip_name = name.strip()
        new_letter = letter.replace("[name]", strip_name)
        with open(
            f"./Output/ReadyToSend/letter_for_{strip_name}.txt", mode="w"
        ) as f:
            f.write(new_letter)
