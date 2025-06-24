# backup/self_restore.py
import os
import shutil
import datetime

def create_backup():
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = f"backup/snapshots/backup_{timestamp}"
    os.makedirs(backup_dir, exist_ok=True)
    for folder in ['codex', 'unimind', 'prometheus', 'config', 'memory_tree']:
        if os.path.exists(folder):
            shutil.copytree(folder, os.path.join(backup_dir, folder), dirs_exist_ok=True)

def restore_backup(backup_name):
    backup_dir = os.path.join("backup/snapshots", backup_name)
    for folder in os.listdir(backup_dir):
        shutil.copytree(os.path.join(backup_dir, folder), folder, dirs_exist_ok=True)

if __name__ == "__main__":
    create_backup()
