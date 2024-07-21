import json
from rouge import Rouge
rouge = Rouge()

def make_abstract(location):
    print(location)
    with open(location, 'r') as f:
        file1 = json.load(f)
    count = 0
    abstract = 0
    average = [0, 0]
    for i, obj in enumerate(file1):
            text = obj['input']
            summary = obj['output']
            scores = rouge.get_scores(text, summary, avg=True)
            abstract = abstract + scores['rouge-2']['f']
            average = i / abstract
    return average

ab_level = make_abstract('your_dataset_path.json')
print('yourdataset abstract level is %s' % ab_level)