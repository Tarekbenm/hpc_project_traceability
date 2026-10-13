"""Public, independently written demonstration with entirely synthetic project records."""
from pathlib import Path
import csv
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / 'data' / 'synthetic' / 'storage_snapshots.csv'
OUT = ROOT / 'outputs'

def build():
    records = list(csv.DictReader(SRC.open(encoding='utf-8', newline='')))
    snapshots = defaultdict(dict)
    for r in records:
        key = r['snapshot_date']
        pid = r['project_id']
        size = float(r['storage_tb'])
        if size < 0: raise ValueError('Storage must be nonnegative')
        snapshots[key][pid] = snapshots[key].get(pid, 0.0) + size
    dates = sorted(snapshots)
    if len(dates) < 2: raise ValueError('At least two snapshots required')
    previous, current = snapshots[dates[-2]], snapshots[dates[-1]]
    OUT.mkdir(exist_ok=True)
    with (OUT / 'project_changes.csv').open('w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['project_id','previous_tb','current_tb','delta_tb','status'])
        w.writeheader()
        for pid in sorted(previous.keys() | current.keys()):
            a, b = previous.get(pid,0), current.get(pid,0)
            status = ('new' if pid not in previous else 'deleted' if pid not in current else 'cleaned' if b<a else 'growing' if b>a else 'stagnant')
            w.writerow(dict(project_id=pid, previous_tb=a, current_tb=b, delta_tb=round(b-a,3), status=status))
    print(f'Created {OUT / "project_changes.csv"} from {dates[-2]} and {dates[-1]}')

if __name__ == '__main__': build()
