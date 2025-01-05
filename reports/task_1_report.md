## Report: Exploratory Data Analysis on Rossmann Store Data

### 1. Objective and Context

The goal of this analysis is to explore customer purchasing behavior across Rossmann stores and identify trends, patterns, and factors influencing sales. This will help answer key business questions related to promotions, holidays, store types, and competitor dynamics.

### 2. Data Cleaning and Preparation

To ensure accurate analysis, the following cleaning steps were applied:

1. **Missing Values**:

   - `CompetitionDistance`: Filled missing values with a high value (10x the maximum distance) to indicate stores with no nearby competition.
   - `CompetitionOpenSinceMonth` and `CompetitionOpenSinceYear`: Filled with 0 to represent stores with undefined competitor opening dates.
   - `Promo2SinceWeek` and `Promo2SinceYear`: Filled with 0 for stores not participating in Promo2.
   - `PromoInterval`: Filled with "None" for stores without Promo2 intervals.

2. **Date Features**:

   - Extracted `Year`, `Month`, `Day`, `Weekday`, and `IsWeekend` from the `Date` column in both `train` and `test` datasets for seasonal analysis.

3. **Outlier Detection**:
   - Addressed outliers in `Sales` and `Customers` using statistical methods to prevent skewed results.

### 3. Exploratory Data Analysis

#### 3.1 Promo Distribution in Training and Test Sets

- **Observation**:
  - Promotions (`Promo`) were distributed similarly between the training and test sets, ensuring consistency for modeling.
- **Visualization**:
  - Bar plots showed the proportion of days with and without promotions.

#### 3.2 Sales Behavior Around Holidays

- **Observation**:
  - Sales increased significantly during holidays, especially state holidays and school holidays.
  - Christmas showed the highest seasonal peak.
- **Visualization**:
  - Line plots illustrated sales trends before, during, and after holidays.

#### 3.3 Seasonal Purchase Behaviors

- **Observation**:
  - A clear seasonal trend was observed, with sales peaking in December (holiday season) and dipping in January.
- **Visualization**:
  - Monthly sales averages plotted on a line chart highlighted these trends.

#### 3.4 Correlation Between Sales and Customers

- **Observation**:
  - A strong positive correlation (R² > 0.8) was observed between `Sales` and `Customers`, indicating customer volume as a primary driver of sales.
- **Visualization**:
  - Scatter plots with regression lines emphasized this relationship.

#### 3.5 Promo Effect on Sales

- **Observation**:
  - Promotions significantly increased sales, with median sales for `Promo = 1` being nearly 50% higher than `Promo = 0`.
  - Stores with higher customer traffic benefitted more from promotions.
- **Visualization**:
  - Box plots compared sales distributions with and without promotions.

#### 3.6 Effect of StoreType and Assortment

- **Observation**:
  - `StoreType 'b'` and `Assortment 'c'` stores had the highest average sales.
- **Visualization**:
  - Box plots showed sales distribution by `StoreType` and `Assortment`.

#### 3.7 Effect of Competition Distance

- **Observation**:
  - Sales were inversely related to `CompetitionDistance`, but the effect was weaker for stores in high-density urban areas.
- **Visualization**:
  - Scatter plots with logarithmic scales illustrated the relationship.

#### 3.8 Customer Trends During Store Open/Closed Times

- **Observation**:
  - Stores open on all weekdays had consistent sales, while weekend sales dipped slightly for stores not open on weekdays.
- **Visualization**:
  - Line plots highlighted weekday vs. weekend sales trends.

### 4. Recommendations

1. **Promotions**:

   - Target stores with lower promo effectiveness to improve customer engagement.
   - Align promotions with holidays and seasonal peaks to maximize sales impact.

2. **Competitor Strategy**:

   - Focus on stores with high competition distances, as they exhibit more stable sales.

3. **Assortment Optimization**:

   - Expand `Assortment 'c'` to more stores, as it correlates with higher sales.

4. **Operational Hours**:
   - Encourage stores to remain open on all weekdays, as this positively impacts weekend sales.

### 5. Conclusion

The analysis reveals actionable insights into customer purchasing behavior, seasonality, promotions, and competitor dynamics. These findings provide a foundation for strategic decisions to optimize sales performance across Rossmann stores.

---
