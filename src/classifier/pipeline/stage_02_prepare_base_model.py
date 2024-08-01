from classifier.config.configuration import ConfigurationManager
from classifier.components.prepare_base_model import PrepareBaseModel
from classifier import logger

STAGE_NAME = "Prepare Base Model Stage"

class PrepareBaseModelPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config_manager = ConfigurationManager()
        prepare_model_config = config_manager.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(prepare_model_config)
        prepare_base_model.get_base_model()
                
if __name__ == '__main__':
    try:
        logger.info(f'>>>>> Stage {STAGE_NAME} started >>>>>')
        obj = PrepareBaseModelPipeline()
        obj.main()
        logger.info(f'>>>>> Stage {STAGE_NAME} finished >>>>>')
    
    except Exception as e:
        logger.exception(e)
        raise e