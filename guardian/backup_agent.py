# guardian/backup_agent.py
import shutil
import os
import time

class BackupAgent:
    def __init__(self, src='.', backup_dir='backups'):
        self.src = src
        self.backup_dir = backup_dir
        os.makedirs(backup_dir, exist_ok=True)

    def create_backup(self):
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        dest = os.path.join(self.backup_dir, f"daemon_backup_{timestamp}")
        shutil.copytree(self.src, dest, dirs_exist_ok=True)
        return f"Backup created at {dest}"
