# DS.v3.2.2.5

# DESCRIPTION OF TWO PROJECTS BELOW 1. COOKIE CATS A/B TEST ANALYSIS 2. FAST FOOD MARKETING A/B TEST ANALYSIS

#  **Retention Effects of Level Gating in Cookie Cats**

This repository contains an analysis of an A/B test run on the mobile game **Cookie Cats**, focused on understanding how the placement of the first gate (at level 30 vs. level 40) affects user retention.

🧪 Background

In Cookie Cats, players progress through levels, occasionally encountering gates that pause progress unless certain actions are taken (e.g., in-app purchases or social sharing). This experiment tests whether moving the first gate from level 30 to level 40 leads to higher user engagement, measured by short-term and long-term retention.

📁 Files

cookie_cats.csv — Raw dataset with user-level data

cookie_cats.ipynb — Main analysis notebook

CustomFunctionsCookieCats.py — Helper functions for plotting and formatting

README.md — Project overview

🔍 Metrics Analyzed

1-Day Retention (retention_1) — Whether a user returned one day after install

7-Day Retention (retention_7) — Whether a user returned seven days after install

Total Game Rounds Played (sum_gamerounds) — Proxy for engagement

🧼 Data Cleaning

Verified no missing values

Removed extreme outliers based on abnormally high sum_gamerounds

Filtered out users unlikely to have reached level 30 (based on total rounds played)

👥 Group Sizes After Filtering
Gate 30: 44,254 users

Gate 40: 45,037 users

📈 Retention Rates (Filtered Dataset)

1-Day Retention

Gate 30: 79.63%

Gate 40: 79.69%

7-Day Retention

Gate 30: 19.02%

Gate 40: 18.20%

📐 Hypothesis Testing

1-Day Retention
Null Hypothesis (H₀): No difference in 1-day retention between gate_30 and gate_40

Result:

Chi-square p-value: 0.9007

Bootstrap 95% CI: [−0.82%, +0.95%]

Treatment effect: +0.06 percentage points

Conclusion:
The result is not statistically significant. We fail to reject H₀.
Gate 40 does not improve short-term retention.

7-Day Retention
Null Hypothesis (H₀): No difference in 7-day retention between gate_30 and gate_40

Result:

Chi-square p-value: 0.0012

Bootstrap 95% CI: [−2.04%, +0.13%]

Treatment effect: −0.82 percentage points

Conclusion:

The p-value suggests a statistically significant difference, and we reject H₀.
However, the confidence interval includes 0, so the result is not robust across methods.
The data suggests gate_40 may reduce long-term retention.

🎯 SRM Check

Chi² = 0.07, p = 0.7854 → No evidence of sample ratio mismatch.

📈 Visualizations

Boxplots of game rounds (before and after cleaning)

Bar charts showing 1-day and 7-day retention by gate version

Comparison charts for visualizing retention differences

Bootstrap confidence interval illustrations

✅ Final Recommendation

Keep the gate at level 30.

No meaningful improvement in 1-day retention

Possible negative effect on 7-day retention

No strong statistical or business case for moving the gate

🛠️ Tools Used

Python 3.x

Pandas, NumPy

Seaborn, Matplotlib

Scipy, Statsmodels

Jupyter Notebook

# **Effectiveness of Promotional Strategies in Fast Food Marketing**

This project analyzes an A/B test conducted by a fast food chain to evaluate three promotional strategies (Promotions 1, 2, and 3) and their impact on weekly sales across different store segments.

🧪 Background

The company tested 3 promotions across stores of varying market sizes and store ages, aiming to identify which promotion boosts sales the most and whether effectiveness depends on store characteristics.

📁 Project Files

WA_Marketing-Campaign.csv – Cleaned dataset

PromotionEffectivenessAnalysisInFastFoodMarketing.ipynb – Main notebook with full analysis

CustomFunctionsFastFood.py – Reusable plotting/statistical functions

FastFoodDashboard.pdf – Visual dashboard

README.md – Project summary

📐 Hypotheses 

Null Hypothesis (H₀):
There is no significant difference in average weekly sales between the different promotion types.

Alternative Hypothesis (H₁):
At least one promotion type leads to significantly different average weekly sales compared to the others.

📉 Metrics Analyzed

Weekly Sales (SalesInThousands)

Grouped comparisons by:

Promotion Type

Store Age Group: Young (≤5), Mid (6–10), Old (>10)

Market Size: Small, Medium, Large

🧼 Data Preparation

Verified data integrity (no missing or malformed entries)

Renamed columns for clarity and readability

Created age and market group labels for segmentation

🔍 Key Insights

Promotion 1 consistently delivers the highest weekly sales

Promotion 3 performs better in older stores and smaller markets

Promotion 2 underperforms in all tested conditions

📈 Statistical Tests Used

Test	Purpose	Parametric
ANOVA	Tests if mean sales differ across groups	✅ Yes
Kruskal-Wallis	Non-parametric version of ANOVA (used when data is not normal)	❌ No
Tukey HSD	Post-hoc test to identify which pairs differ after ANOVA	✅ Yes
Mann-Whitney U	Non-parametric pairwise test for two groups	❌ No
SRM Check (Chi²)	Ensures sample distribution is balanced across groups	✅ Yes
Shapiro-Wilk Test	Checks for normality in sales distributions	✅ Yes

📊 Visuals & Dashboard

Violin, box, and point plots for promotion effectiveness

Correlation heatmaps between numeric features

Segmented plots by Market Size and Store Age

FastFoodDashboard.pdf for visual insights

✅ Final Recommendation

Use Promotion 1 as the default strategy

Consider Promotion 3 for older stores and small markets

Phase out Promotion 2 due to underperformance

Customize future campaigns based on store and market context for better ROI

🛠️ Tools Used

Python 3.x

Pandas, NumPy – Data manipulation

Matplotlib, Seaborn – Visualization

Statsmodels, SciPy – Statistical testing

Jupyter Notebook – Interactive analysis

Looker Studio (Google Data Studio) – Dashboard building

## LICENSE

These projects are licensed under the MIT License.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
