from classifier import logger
from classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from classifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline

STAGE_NAME = "Data Ingestion Stage"

print("\n*******************************************************\n")

try:
    logger.info(f'>>>>> Stage {STAGE_NAME} started >>>>>')
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f'>>>>> Stage {STAGE_NAME} finished >>>>>')

except Exception as e:
    logger.exception(e)
    raise e
    
print("\n*******************************************************\n")

STAGE_NAME = "Prepare Base Model Stage"
try:
    logger.info(f'>>>>> Stage {STAGE_NAME} started >>>>>')
    obj = PrepareBaseModelPipeline()
    obj.main()
    logger.info(f'>>>>> Stage {STAGE_NAME} finished >>>>>')

except Exception as e:
    logger.exception(e)
    raise e

print("\n*******************************************************\n")