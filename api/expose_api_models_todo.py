from safrs import SAFRSAPI
import safrs
import importlib
import pathlib
import logging as logging

# use absolute path import for easier multi-{app,model,db} support
database = __import__('database')

app_logger = logging.getLogger('api_logic_server_app')
app_logger.debug("\napi/expose_api_models_todo.py - endpoint for each table")


def expose_models_on_existing_api(api):
    """
        Declare API - create SAFRSAPI 
            This exposes each model (note: end point names are table names) 
            Including get (filtering, pagination, related data access) 
            And post/patch/update (including logic enforcement) 
        You typically do not customize this file 
            See https://valhuber.github.io/ApiLogicServer/Tutorial/#customize-and-debug 
    """
    safrs_log_level = safrs.log.getEffectiveLevel()
    if True or app_logger.getEffectiveLevel() >= logging.INFO:
        safrs.log.setLevel(logging.WARN)  # log level warn is 20, info 30
    api.expose_object(database.models_todo.Todo)
    safrs.log.setLevel(safrs_log_level)
    return api
