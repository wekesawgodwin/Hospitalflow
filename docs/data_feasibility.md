After doing a data feasibility audit of hospital hmis dataset for healthcare analytics dataset from Kaggle, I propose we go with a **synthetic data approach** for the inventory details.

The only inventory-leaning data in the Kaggle dataset is on drugs. Data for non-drug consumables like syringes and diagnostic kits is unavailable.

## Data gap assessment

### Data present in the current dataset
* Clinical demand drivers: Prescriptions (dosage, frequency, duration_days), admissions (admission_date, ward/department), and diagnosis classifications.

* Data: Drug catalog (drug_id, unit cost, categories) and stock snapshots (current_stock, reorder_level).

### Missing data
* Daily transaction logs: No historical time-series of opening_stock, quantity_received, quantity_used, or closing_stock.  
* Non-drug medical consumables: High-turnover items (e.g., syringes, gloves, IV cannulas, gauze) are absent from the drug-focused schema

* Supplier details: Absence of supplier delivery histories, lead times (supplier_lead_time_days), and delivery variance.  