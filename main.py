from classifier import logger
from classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

if __name__ == '__main__':
    try:
        logger.info(f'>>>>> Stage {STAGE_NAME} started >>>>>')
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f'>>>>> Stage {STAGE_NAME} finished >>>>>')
    
    except Exception as e:
        logger.exception(e)
        raise e