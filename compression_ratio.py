import json

def make_ratios(location):
    print(location)
    with open(location, 'r') as f:
        file1 = json.load(f)
    ratios = []
    total = 0
    totaldocument = 0
    totalsummary = 0
    data = [0, 0 , 0]
    for i, obj in enumerate(file1):
            text = obj['input']
            summary = obj['output']
            text = text.split()
            summary = summary.split()
            ratio = len(text)/len(summary)
            total = total + ratio
            totaldocument = totaldocument + len(text)
            totalsummary = totalsummary + len(summary)
            averagedocument = totaldocument / (i+1)
            averagesummary = totalsummary / (i+1)
            averageratio = total / (i+1)
            ratios.append(ratio)
    data[0] = averageratio
    data[1] = averagedocument
    data[2] = averagesummary
    return data

cm_ratio = make_ratios('your_dataset_path.json')
print('your_dataset comperession ratio is %s' % cm_ratio[0])
print('your_dataset documents are %s' % cm_ratio[1])
print('your_dataset summarys are %s' % cm_ratio[2])