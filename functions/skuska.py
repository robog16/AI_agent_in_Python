import os

working_directory = "/home/bear/agent"
directory = "../../etc"

# Vyrobíme absolutní cestu k directory
relative_path = os.path.join(working_directory, directory)
full_path = os.path.abspath(relative_path)
full_path_WD = os.path.abspath(working_directory)

print(relative_path)
print(full_path)
print(full_path_WD)

# Zjistíme, jestli full_path opravdu začíná (leží) uvnitř working_directory
if full_path.startswith(os.path.abspath(working_directory)):
    print("Leží uvnitř working_directory!")
else:
    print("MIMO povolený adresář!")