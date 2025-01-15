import azure.functions as func
import logging
import json

app = func.FunctionApp()

@app.function_name(name="update_views")
@app.route(route="views")
@app.cosmos_db_input(arg_name="inputDocument", 
                     database_name="view_counter", 
                     container_name="view_container",
                     partition_key="f4d02b8e-4fdc-4c26-8434-17d984004ecb",
                     connection="CosmosDbConnectionSetting")
@app.cosmos_db_output(arg_name="outputDocument", 
                     database_name="view_counter", 
                     container_name="view_container",
                     create_if_not_exists=True,
                     connection="CosmosDbConnectionSetting")

def update_views(inputDocument: func.DocumentList,
                  outputDocument: func.Out[func.Document],
                  req: func.HttpRequest) -> func.HttpResponse:

    count = inputDocument[0]
    logging.info(inputDocument[0].to_json())

    current_count = inputDocument[0]['count']
    logging.info(f'Current count: {current_count}')

    current_count = int(current_count) + 1
    count['count'] =  current_count

    outputDocument.set(count)

    logging.info(f'New page count: {current_count}')

    return func.HttpResponse(
        str(current_count)
    )