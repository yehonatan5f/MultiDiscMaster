import os
import shutil
import re
import argparse
from tqdm import tqdm

def get_game_name(filename):
    match = re.match(r'(.*?)\s*(\(.*?\))?\s*(\(Disc \d+\))', filename)
    if match:
        return match.group(1).strip() + ' ' + match.group(2)
    return None

def create_m3u_file(folder_path, game_name, disc_files):
    m3u_filename = f"{game_name}.m3u"
    m3u_path = os.path.join(folder_path, m3u_filename)
    with open(m3u_path, 'w') as m3u_file:
        for disc in sorted(disc_files):
            m3u_file.write(f"{disc}\n")
    return m3u_filename

def organize_multi_disc_games(folder_path):
    print(f"Scanning folder: {folder_path}")
    
    files = os.listdir(folder_path)
    print(f"Found {len(files)} files in the directory.")
    
    game_files = {}
    for file in tqdm(files, desc="Analyzing files"):
        if "Disc" in file:
            game_name = get_game_name(file)
            if game_name:
                if game_name not in game_files:
                    game_files[game_name] = []
                game_files[game_name].append(file)
    
    print(f"Identified {len(game_files)} potential multi-disc games.")
    
    games_processed = 0
    files_moved = 0
    created_folders = []
    for game_name, game_file_list in tqdm(game_files.items(), desc="Processing games"):
        new_dir = os.path.join(folder_path, game_name)
        print(f"\nProcessing: {game_name}")
        
        if not os.path.exists(new_dir):
            print(f"  Creating directory: {new_dir}")
            os.makedirs(new_dir)
            created_folders.append(new_dir)
            
            m3u_file = next((f for f in game_file_list if f.endswith('.m3u')), None)
            if not m3u_file:
                print(f"  Creating .m3u file for {game_name}")
                m3u_file = create_m3u_file(folder_path, game_name, game_file_list)
                game_file_list.append(m3u_file)
            
            for file in game_file_list:
                src = os.path.join(folder_path, file)
                dst = os.path.join(new_dir, file)
                print(f"  Moving: {file}")
                shutil.move(src, dst)
                files_moved += 1
            
            games_processed += 1
        else:
            print(f"  Skipping: Directory already exists")
    
    print("\nAdding .m3u extension to created folders...")
    folders_renamed = 0
    for folder in created_folders:
        if not folder.endswith('.m3u'):
            new_name = folder + '.m3u'
            try:
                os.rename(folder, new_name)
                print(f"Renamed: {os.path.basename(folder)} -> {os.path.basename(new_name)}")
                folders_renamed += 1
            except Exception as e:
                print(f"Error renaming {folder}: {e}")
    
    print("\nSummary:")
    print(f"Total multi-disc games processed: {games_processed}")
    print(f"Total files moved: {files_moved}")
    print(f"Total folders renamed: {folders_renamed}")

def main():
    parser = argparse.ArgumentParser(description="Organize multi-disc games, create .m3u files if missing, and rename folders.")
    parser.add_argument("folder_path", help="Path to the folder containing game files")
    args = parser.parse_args()

    print(f"Script started. Processing folder: {args.folder_path}")
    organize_multi_disc_games(args.folder_path)
    print("Script finished.")

if __name__ == "__main__":
    main()