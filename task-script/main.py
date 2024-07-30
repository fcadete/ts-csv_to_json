from ts_sdk.task.__task_script_runner import Context
from task_script.csv_to_json import csv_to_json
import pandas as pd
import os

def csv_to_json_main(input: dict, context: object):
    """A function to the input CSV file to a JSON file
    
    This function was written in the context of the panel interview for TetraScience.
    It is very barebones at this point. It assumes that the input will be a correctly formated CSV file.

    Logic:
    1. Read original file as CSV with Pandas
    2. Convert table to JSON
    3. Create new output filename
    4. Write JSON file to Data Lake

    Args:
        input (dict): input dict passed from master script
        context (object): context object

    Returns:
        None
    """

    print("Starting task of converting CSV to JSON")

    input_file_pointer = input["input_file_pointer"]

    input_data = context.read_file(input_file_pointer, form = "file_obj")

    input_table = pd.read_csv(input_data['file_obj'])

    input_json = csv_to_json(input_table)

    input_filename = context.get_file_name(input_file_pointer)

    output_filename = os.path.splitext(input_filename)[0] + ".json"

    print("Writing JSON output to " + output_filename)

    output_file = context.write_file(str(input_json), file_name=output_filename, file_category="PROCESSED")

    print("Task completed")
    return output_file
