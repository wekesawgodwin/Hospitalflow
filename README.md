# HospitalFlow

Predictive inventory and stockout intelligence for Kenyan hospitals.

Hospitals can look adequately stocked and still run out before the next
delivery arrives. HospitalFlow reads inventory transactions, measures what is
actually being consumed, forecasts demand, and estimates the probability of a
stockout against supplier lead time — so procurement teams get warning earlier
than a low-stock threshold would give them.

The system recommends. A procurement officer decides. It never places an order
on its own.

## What it does

| Layer | Question | Output |
|---|---|---|
| Consumption | How fast are we using this? | Daily and rolling usage from transaction records |
| Forecasting | How much will we use next? | 7 / 14 / 30-day demand |
| Risk | Will we run out before resupply? | Stockout probability and risk class |
| Reorder | What should we order, and when? | Reorder point and suggested quantity |
| Disease signal | Does service activity explain demand? | Tested as a forecasting feature |

Every figure traces back to a source record, a transparent calculation, or a
documented model output.

## Status

Prototype, in development. Built on a synthetic dataset — real hospital
inventory data is sensitive and hard to obtain. Findings demonstrate method,
not measured facts about Kenyan hospitals.

## Quick start

```bash
git clone https://github.com/wekesawgodwin/hospitalflow.git
cd hospitalflow

python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pre-commit install

cp .env.example .env      # then edit it
```

Download the dataset following `data/raw/README.md` — it is not in the repo.

```bash
docker compose up
```

API docs: http://localhost:8000/docs

## Layout

```
src/hospitalflow/
  ingestion/          loading and standardisation
  validation/         data quality and reconciliation
  features/           lags, rolling stats, calendar, disease signals
  models/forecasting/ demand forecasting
  models/stockout/    stockout risk classification
  procurement/        reorder points and recommendations
  api/                FastAPI service
notebooks/            NN_owner_topic.ipynb
db/                   schema and migrations
frontend/             dashboard
tests/                pytest suite
docs/                 data dictionary, model cards, CRISP-DM
```

## Stack

Python · pandas · scikit-learn · XGBoost · PostgreSQL · FastAPI · Docker

## Working agreements

- Branch from `develop`: `feature/<initials>-<short-name>`
- Nobody pushes to `main` or `develop` directly
- Nobody merges their own PR
- PR titles carry the card ID: `[S2-04] Random Forest demand model`
- Clear notebook outputs before committing — pre-commit does it for you
- No feature may use information unavailable at prediction time
- The holdout test set is read **once**, in Sprint 3

## Team

| Role | Owner |
|---|---|
| Team lead / ML | Wekesa Godwin |
| Data engineering | Mary Gathoni |
| Feature engineering & forecasting | Mohammed Abdi |
| Evaluation &  analysis | Trevor Amayi |
| Backend | Alvin Maina |
| Frontend & DevOps | Ibrahim George |

## Limitations

Synthetic prototype data. Forecast quality depends on history length and data
quality. Outbreaks and supplier disruptions create patterns the models have not
seen. Association is not causation. Any deployment needs local validation and
ongoing monitoring.

 Full documentation in `docs/`.
