def write_to_file(file_type,indx,x):
    
    if file_type == "txt":
        with open("patentTitles.txt", "a") as text_file:
            text_file.write(f"{indx}. {x}\n")
            text_file.seek(0)
    elif file_type == "csv":
        with open("patentTitles.csv", "a") as text_file:
            text_file.write(f"{indx}. {x}\n")
            text_file.seek(0)