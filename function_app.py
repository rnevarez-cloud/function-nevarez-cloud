import azure.functions as func
import logging
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.function_name(name="system")
@app.route(route="system")
@app.cosmos_db_input(arg_name="documents", 
                     database_name="TablesDB",
                     container_name="page_views",
                     connection="CosmosDbConnectionSetting")
def system(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    return func.HttpResponse(
        json.dumps(documents),
        status_code=200
    )