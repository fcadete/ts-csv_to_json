from ts_sdk.task.__task_script_runner import Context
import json
import pandas as pd

def csv_to_json(input_table: pd.DataFrame):

    print("CSV table uploaded is:")
    print(input_table.to_string())

    input_json_string = input_table.to_json(orient='index')

    input_json = json.loads(input_json_string)

    output_json_string = json.dumps(input_json, indent = 4)

    print("Convertion to JSON is:")
    print(output_json_string)

    return output_json_string
