import os
import subprocess
import sys

from helpers.logger import gen_logger

logger = gen_logger("Files")
download_folder = './sdcard/Download'


def android_check_folder_empty():
    try:
        adb_command = f'adb shell ls {download_folder}'
        output = subprocess.check_output(adb_command, shell=True).decode().strip()

        if not output:
            logger.info("The 'Download' folder is empty.")
        else:
            logger.info("The 'Download' folder is not empty.")
            sys.exit(1)
    except subprocess.CalledProcessError as e:
        logger.error("Error occurred while listing files:", e)
        sys.exit(1)
    except Exception as e:
        logger.error("Error occurred while listing files:", str(e))
        sys.exit(1)



def android_clear_downloads():
    try:
        adb_command = f'adb shell rm {download_folder}/*'
        logger.info(f"run: ${adb_command}")
        subprocess.check_output(adb_command, shell=True)
        logger.info("All files removed from the 'Download' folder.")
    except Exception:
        logger.info("Folder already clean.")
        pass


def android_push_file(driver, file_name):
    try:
        file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + f'/files/malware/{file_name}'
        driver.push_file(destination_path=f'{download_folder}/{file_name}', source_path=file_path)
        logger.info(f"File '{file_name}' is pushed into the 'Download' folder.")
    except FileNotFoundError as e:
        logger.error("Error occurred while pushing the file:", str(e))
        sys.exit(1)


def android_is_file_exist(file_name):
    output = subprocess.check_output(f'adb shell ls {download_folder}', shell=True).decode().strip()
    return file_name in output.split()


def android_install_apk(driver, file_name):
    try:
        file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + f'/files/malware/{file_name}'
        driver.push_file(download_folder, file_path)
        driver.install_app(file_path)
        logger.info("File has been successfully pushed to the device's internal storage.")
    except FileNotFoundError as e:
        logger.error("Error occurred while pushing the file:", str(e))
