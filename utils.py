import json
from pathlib import Path


def read_json(json_path):
    with open(json_path) as json_file:
        json_data = json.load(json_file)
    return json_data



if __name__ == '__main__':
    for i in range(1,11):
        json_path = f'/root/hand/detectron2/datasets/inter/annotations/{i}th_train.json'
        data = read_json(json_path)
        print(f'{i}')