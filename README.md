# ECO346-A1-FA24-BED-055
Data visulization and analysis of annual earning among idividual age between 15-64 in urban balochistan using PSLM data.
Variant: 7

Project Overview
This project explores annual earnings among individuals aged 15–64 in urban Balochistan using the provided Pakistan Social and Living Standards Measurement (PSLM) subset data.

The analysis uses person-level earnings and age information joined with household-level information. Household weights are used for weighted statistics and visual summaries.

Research and Visualization Tasks
Q2: Earnings Distribution

A weighted histogram displays the distribution of positive annual earnings. The analysis reports the unweighted median, weighted median, weighted 10th and 90th percentiles, and the P90/P10 ratio.

Q3: Earnings by Age

A visualization compares individual annual earnings across five-year age bands and displays weighted mean earnings for each band. A logarithmic vertical axis helps show the wide range of earnings. Bands with fewer than 30 earners are identified as thin groups.

Q4: Default and Redesigned Visualization

The default scatterplot is saved separately before the redesigned visualization. The redesign is intended to improve readability and communicate the data more clearly.

Q5: Cross-Language Reproduction

Python independently reproduces the age-band summary table and age-profile visualization. The results are compared with the R analysis, with any differences investigated and documented.

Repository Structure
data/ — Provided person-level and household-level CSV files.

scripts/ — R and Python scripts used to reproduce the analysis and figures.

figures/ — SVG visualizations and the exported Python summary table.

notebooks/ — Optional Jupyter notebook documenting the Python analysis.

slides/ — Assignment presentation.

Data Preparation
The person-level and household-level datasets are joined using hhid.

The analytical sample is restricted to:

Province code 4 (Balochistan).

Urban/rural code 2 (urban).

Ages 15–64, inclusive.

Positive annual earnings.

Finite, positive household weights.

Age groups use five-year intervals: 15–19, 20–24, 25–29, and so on through 60–64. Weighted quantiles are calculated using sorted earnings and cumulative household-weight shares.

Reproducibility
Run the scripts from the repository root directory. The required CSV files should remain in data/, and the R and Python environments must have the packages used by the scripts installed.

The scripts save their outputs in figures/. See the individual scripts for the calculations and output filenames.

Key Results
The R analysis reports the following weighted mean annual earnings:

Age band

Weighted mean annual earnings

25–29

Rs 307,994

45–49

Rs 372,723

60–64

Rs 476,422

The highest weighted mean in the R age-band summary is for ages 60–64. This band has fewer than 30 earners, so its estimate should be interpreted cautiously.

The descriptive results show differences in earnings across age groups but do not establish that age causes earnings to increase.

Limitations
The analysis is descriptive and is limited to the selected urban Balochistan sample. Differences in education, occupation, work experience, and other factors may also contribute to observed earnings differences. Estimates from thin age bands are less stable.

Outputs
The repository contains the scripts, figures, and presentation prepared for ECO346 Assignment 1. Numerical results should be interpreted alongside the sample restrictions, weighting method, and limitations described above. above.
