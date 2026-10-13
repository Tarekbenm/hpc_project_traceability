import csv
import unittest
from pathlib import Path
from src.pipeline import build, OUT

class PipelineTest(unittest.TestCase):
    def test_statuses(self):
        build()
        with (OUT / 'project_changes.csv').open(newline='',encoding='utf-8') as f:
            rows = {r['project_id']:r for r in csv.DictReader(f)}
        self.assertEqual(rows['DEMO-001']['status'],'cleaned')
        self.assertEqual(rows['DEMO-002']['status'],'growing')
        self.assertEqual(rows['DEMO-003']['status'],'deleted')
        self.assertEqual(rows['DEMO-004']['status'],'stagnant')
        self.assertEqual(rows['DEMO-005']['status'],'new')

if __name__ == '__main__':unittest.main()
