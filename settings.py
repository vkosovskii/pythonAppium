# coding: utf8
import os
import yaml

from helpers.logger import gen_logger

logger = gen_logger("Set config")


class Config:
    config = None

    def get_config(self):
        return self.config

    def set_config(self, test_platform, type):
        if os.path.exists(os.path.dirname(__file__) + "/yml/config.yml"):
            CONFIG = yaml.safe_load(open(os.path.dirname(__file__) + "/yml/config.yml", 'r'))
            self.config = CONFIG[test_platform]
            self.get_file_name(self.config['platformName'], type)
        else:
            raise "config.yml does not exists"

    def get_test_data(self):
        if os.path.exists(os.path.dirname(__file__) + "/yml/test_data.yml"):
            return yaml.safe_load(open(os.path.dirname(__file__) + "/yml/test_data.yml", 'r'))
        else:
            raise "config.yml does not exists"

    def get_file_name(self, test_platform, type):
        folder_path = os.path.dirname(__file__) + f"/files/{test_platform}/{type}/"

        # Get a list of all files in the folder
        files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if
                 os.path.isfile(os.path.join(folder_path, file))]

        # Sort the files based on the modification time in descending order
        sorted_files = sorted(files, key=lambda x: os.path.getmtime(x), reverse=True)

        logger.info(sorted_files[0])

        if sorted_files:
            self.config['app'] = sorted_files[0]
        else:
            self.config['app'] = "EMPTY!!!"
            raise "No files found in the folder."
