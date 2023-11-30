import os

def rename_files(folder_path):
    file_list = os.listdir(folder_path)
    for i, file_name in enumerate(file_list):
        new_file_name = f"{str(i+70).zfill(3)}.png"
        file_path = os.path.join(folder_path, file_name)
        new_file_path = os.path.join(folder_path, new_file_name)
        os.rename(file_path, new_file_path)
        print(f"rename:{file_name} -> {new_file_name}")

folder_path = 'DonaldTrump80/test'
rename_files(folder_path)