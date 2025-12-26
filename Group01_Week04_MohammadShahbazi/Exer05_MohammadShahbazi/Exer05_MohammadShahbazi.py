files = ["report.pdf", "image.png", "data.csv", "logo.png", "notes.txt", 
         "thesis.pdf"]

files_by_extension = {}

for file in files:
    if '.' in file:
        extension = file.split('.')[-1]
    else:
        extension = "no_extension"  
    
    if extension in files_by_extension:
        files_by_extension[extension].append(file)
    else:
        files_by_extension[extension] = [file]

for extension in sorted(files_by_extension.keys()):
    file_list = files_by_extension[extension]
    print(f"\n{extension} ({len(file_list)}):")
    for file in file_list:
        print(f"{file}")