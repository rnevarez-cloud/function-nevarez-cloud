import azure.functions as func # type: ignore
import logging
import json

app = func.FunctionApp()

@app.function_name(name="HttpTrigger1")
@app.route(route="hello", auth_level=func.AuthLevel.ANONYMOUS)
@app.cosmos_db_output(arg_name="documents", database_name="TablesDB", container_name="page_views", connection="CosmosDbConnectionSetting")

def test_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    logging.info('Python Cosmos DB trigger function processed a request.')
    return func.HttpResponse (
        json.dumps(documents),
        status_code=200
    )