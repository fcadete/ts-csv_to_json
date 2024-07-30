from task_script.csv_to_json import csv_to_json
import pandas as pd

def test_csv_to_json():

    input_table = pd.read_csv("../../helloworld_tests/test-files/three_lines.csv")

    output = csv_to_json(input_table)
    
    assert output == '{\n    "0": {\n        "column1": "row1_1",\n        "column2": "row1_2"\n    },\n    "1": {\n        "column1": "row2_1",\n        "column2": "row2_2"\n    },\n    "2": {\n        "column1": "row3_1",\n        "column2": "row3_2"\n    }\n}'