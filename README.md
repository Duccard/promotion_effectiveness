# DS.v3.2.2.5

# Effectiveness of Promotional Strategies in Fast Food Marketing

This project analyzes an A/B test conducted by a fast food chain to evaluate the effectiveness of three promotional strategies (Promotions 1, 2, and 3) on weekly sales performance across different store segments.

---

## Objective

Determine which promotion drives the highest sales and how effectiveness varies by store age and market size.

---

## Dataset

- `WA_Marketing-Campaign.csv` – Cleaned dataset containing weekly sales, promotion type, store age, and market size.

---

## Project Files

- `data/WA_Marketing-Campaign.csv` – Cleaned input data
- `notebooks/Promotion_Effectiveness_Analysis.ipynb` – Main analysis notebook
- `src/custom_functions.py` – Modular plotting and statistical functions
- `reports/Fast_Food_Marketing_Dashboard.pdf` – Summary dashboard of results
- `README.md` – Project overview and documentation
- `requirements.txt` – Python dependencies
- `.gitignore` – Ignored files and folders

---

## Key Metrics

- **Weekly Sales** (in thousands)
- **Promotion Type**: 1, 2, 3
- **Market Size**: Small, Medium, Large
- **Store Age Group**: Young (≤5), Mid (6–10), Old (>10)

---

## Key Insights

- **Promotion 1** consistently leads to the highest weekly sales.
- **Promotion 3** performs better in older stores and smaller markets.
- **Promotion 2** underperforms across all segments.

---

## Final Recommendation

- Adopt **Promotion 1** as the default strategy.
- Use **Promotion 3** selectively for older stores or small markets.
- Discontinue **Promotion 2**.
- Customize promotions by store segment to improve return on investment (ROI).

---

## Visualizations

- Boxplots, violin plots, and point plots of sales by promotion type
- Correlation heatmaps
- Segmented visual comparisons by market size and store age
- Dashboard summary in `Fast_Food_Marketing_Dashboard.pdf`

---

## Tools Used

- Python 3.x
- pandas, NumPy – Data manipulation
- seaborn, matplotlib – Visualization
- scipy, statsmodels – Statistical testing
- Jupyter Notebook – Interactive analysis

---

## LICENSE

These projects are licensed under the MIT License.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
