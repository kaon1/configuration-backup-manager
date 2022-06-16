import os
import datetime as dt
import re

backup_state_file_path = '/root/configuration-backup-manager/backup_state.txt'


def is_file_current(filename):
    try:
        today = dt.datetime.now().date()
        filetime = dt.datetime.fromtimestamp(os.path.getmtime(filename))
        if filetime.date() == today:
            return True
        else:
            return False

    except Exception as e:
        return False


def is_no_errors_count(filename):
    try:
        pattern = re.compile("Errored Backups: (\\d)")
        for line in open(filename):
            for match in re.finditer(pattern, line):
                if match.group(1) == '0':
                    return True
                else:
                    return False
        return False

    except Exception as e:
        return False

def is_no_s3_errors(filename):
    try:
        pattern = re.compile("(S3 SYNC SUCCESSFUL)")
        for line in open(filename):
            for match in re.finditer(pattern, line):
                if match.group(1) == 'S3 SYNC SUCCESSFUL':
                    return True
                else:
                    return False
        return False

    except Exception as e:
        return False

def is_total_match(filename):
    try:
        pattern1 = re.compile("Errored Backups: (\\d)")
        for line in open(filename):
            for match in re.finditer(pattern1, line):
                total_errors = match.group(1)

        pattern2 = re.compile("Successful Backups: (\\d)")
        for line in open(filename):
            for match in re.finditer(pattern2, line):
                total_success = match.group(1)

        pattern3 = re.compile("Total Devices Tagged for Backup: (\\d)")
        for line in open(filename):
            for match in re.finditer(pattern3, line):
                total_hosts = match.group(1)

        if int(total_errors) + int(total_hosts) == int(total_success):
            return True
        else:
            return False

    except Exception as e:
        return False

def main():
    backup_status = is_file_current(backup_state_file_path) and is_no_errors_count(backup_state_file_path) and is_no_s3_errors(backup_state_file_path) and is_total_match(backup_state_file_path)

    if os.path.exists("/usr/share/nginx/html/backup_status.txt"):
        os.remove("/usr/share/nginx/html/backup_status.txt")

    f = open("/usr/share/nginx/html/backup_status.txt", "a")
    f.write(str(backup_status))
    f.close()


if __name__ == "__main__":
    main()