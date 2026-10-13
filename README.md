# HPC Project Traceability — Public Demonstration

**Python · Data Engineering · Storage Analytics · Business Intelligence**

## Professional context

This portfolio demonstration is inspired by my professional experience working on HPC project lifecycle and storage traceability at TotalEnergies (2024–2026). The business challenge was to consolidate project storage snapshots and related project information to support monitoring, clean-up prioritization, and reporting.

**Confidentiality:** This is an independently written educational reconstruction, **not the original corporate project or source code**. All sample records, project identifiers, values and dates are fictional. No original corporate datasets, report files, paths, identifiers or Power BI reports are included. This repository is not affiliated with or endorsed by TotalEnergies.

## Architecture of the original business use case (conceptual)

`Storage snapshots + budget references + archive references → RAW → BRONZE → SILVER → GOLD → Power BI`

The original handover documentation describes storage snapshot history, storage trends, project clean-up comparisons, budget/TUSI traceability, and Power BI reporting. It also documents some manual execution steps and unresolved dependencies; it should **not** be described as a fully automated production pipeline.

## What this public demo implements

A small, runnable Python pipeline that reads **fictional** storage snapshots, aggregates storage per project and date, compares the latest two dates, and classifies projects as `cleaned`, `deleted`, `growing`, `stagnant`, or `new`.

This demo is intentionally narrower than the professional solution. Budget integration, archive/TUSI linkage, Parquet layers, and Power BI visuals are **not implemented in this public version**.

## Run

Requires Python 3.10+; no third-party packages.

```bash
python -m src.pipeline
python -m unittest discover -s tests -v
```

Output: `outputs/project_changes.csv` (generated locally, ignored by Git).

## Example metrics to develop next

- Storage consumption by project and date
- Total storage reduction between snapshots
- Stagnant project identification
- Budget coverage and archive-reference completeness using synthetic data
- Public Power BI report recreated from fictional datasets

## Publication boundaries

The original corporate `.pbix`, operational code, handover document, source exports, logs and state files are intentionally excluded. Do not copy them into this repository without written company authorization and a confidentiality review.
