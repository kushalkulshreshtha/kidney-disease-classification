from classifier.config.configuration import ConfigurationManager
from classifier.components.data_ingestion import DataIngestion
from classifier import logger

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config_manager = ConfigurationManager()
        data_ingestion_config = config_manager.get_data_ingestion_config()
        data_ingestion = DataIngestion(config = data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zipfile()


if __name__ == '__main__':
    try:
        logger.info(f'>>>>> Stage {STAGE_NAME} started >>>>>')
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f'>>>>> Stage {STAGE_NAME} finished >>>>>')
    
    except Exception as e:
        logger.exception(e)
        raise e