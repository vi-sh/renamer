import os
import argparse

def rename_files(foldername: str, new_name: str):
    if not os.path.exists(foldername):
        print("Folder does not exist.")
        return

    for i, filename in enumerate(os.listdir(foldername)):
        ext = os.path.splitext(filename)[1]
        new_filename = os.path.join(foldername, f"{new_name}_{i+1}{ext}")
        os.rename(os.path.join(foldername, filename), new_filename)
        print(f"Renamed {filename} to {os.path.basename(new_filename)}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Rename files in a folder.')
    parser.add_argument('foldername', type=str, help='The name of the folder containing the files to be renamed.')
    parser.add_argument('new_name', type=str, help='The new name to be given to the files.')
    args = parser.parse_args()

    rename_files(args.foldername, args.new_name)