from pathlib import Path
import csv, json, numpy as np
folder = Path(__file__).resolve().parent / 'outputs/minxiong/prediction'
summary = json.loads((folder/'prediction_summary.json').read_text(encoding='utf-8'))
out = folder/'flood_prediction.csv'
with out.open('w',newline='',encoding='utf-8') as f:
    w=csv.writer(f);w.writerow(['x','y','t','h','u','v'])
    for frame in summary['frames']:
        a=np.load(folder/frame['file'])
        t=frame['time_s']
        w.writerows(zip(a['x'],a['y'],[t]*len(a['x']),a['h'],a['u'],a['v']))
print(out)
