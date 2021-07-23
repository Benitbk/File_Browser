import os
import File


class Directory:
    def __init__(self, path):
        self.path = path
        self.name = os.path.basename(path[:-2:]) # CR: try to improve this line
        self.creation_date = os.path.getctime(path)

    def __str__(self):
        return f"Name: {self.name}, creation date: {self.creation_date}"

    def print_items(self) -> str:
        folder_names = []
        file_names = []
        all_files_names = os.listdir(self.path)
        for file_name in all_files_names:
            file_path = os.path.join(self.path, file_name)
            if os.path.isdir(file_path):
                folder_names.append(file_name)
            else:
                f1 = File.File(file_path)
                file_names.append(str(f1))

        return f'Files:\n{[str(file) for file in file_names]}\nFolders:\n{[folder for folder in folder_names]}\n', folder_names
