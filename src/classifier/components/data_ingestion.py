import os
import gdown
import zipfile
from classifier import logger
from classifier.utils.common import get_size
from classifier.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self) -> str:
        try:
            dataset_url = self.config.source_url
            zip_download_dir = self.config.local_data_file
            os.makedirs(self.config.root_dir , exist_ok=True)
            logger.info(f'Downloading data from {dataset_url} into file {zip_download_dir}')

            file_id = dataset_url.split("/")[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix + file_id, zip_download_dir)

            logger.info(f"Data downloaded from {dataset_url} into file {zip_download_dir}")
        
        except Exception as e:
            raise e 
    
    def extract_zipfile(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        logger.info('Zip file extracted')