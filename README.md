# Marketing A/B Testing Analysis

This project analyzes the results of a marketing A/B test to derive insights and assess the performance of various test groups. The analysis includes statistical testing, data visualization, and univariate analysis.

## Dataset

The dataset contains information about:
- Test groups (control and treatment)
- Conversion status
- Most active day and hour for ads
- Total ads seen by users

## Project Structure

- **Data Preprocessing**
  - Handled missing values and removed duplicate entries.
  - Dropped unnecessary columns (`Unnamed: 0`, `user id`) for cleaner analysis.
  
- **Univariate Analysis**
  - Distribution analysis using count plots, pie charts, histograms, and boxplots.
  
- **Statistical Testing**
  - Normality test using the Shapiro-Wilk test.
  - Variance analysis using Levene's test.
  - Independent sample t-test for group comparison.
  - Chi-square test for independence of categorical variables.

- **Visualization**
  - Created insightful visualizations using `matplotlib` and `seaborn`:
    - Histograms and boxplots for numerical data.
    - Count plots and pie charts for categorical data.

## Key Functions and Scripts

- **`plot(variable)`**: A function for visualizing the distribution of categorical variables using count plots and pie charts.
- **Filtering and Visualization**: Filtered extreme values in numerical columns for better visualization of trends.
- **Statistical Tests**:
  - **Normality Test**: Determines if the data follows a normal distribution.
  - **Levene’s Test**: Assesses the equality of variances between groups.
  - **T-Test**: Compares means between control and treatment groups.
  - **Chi-Square Test**: Examines the relationship between test groups and conversion rates.

## Libraries Used

- **Core Libraries**: `numpy`, `pandas`
- **Visualization**: `matplotlib`, `seaborn`
- **Statistical Analysis**: `scipy`

