# Time Series projections for Zillow Housing Data For Flatiron School Data Science Immersive (Phase 4 Project)
  
## Overview  
In this project, we examine and perform time series analysis on a dataset of housing data from [Zillow Research](https://www.zillow.com/research/data/) to determine where in Los Angeles vs San Fransciso would be best to invest in real estate.  

![california_house](images/california_housing.jpg)  
  
## Motivation  
To make informed recommendations to investment advisors, real estate brokers, and houseowners who are looking to invest in a mid-tier 2-bedroom home in the Los Angeles / San Francisco area. This captures the intent of a couple looking for their first home.  

## Data  
Our [dataset](https://files.zillowstatic.com/research/public_v2/zhvi/Zip_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_mon.csv?t=1618844874) comes from the [Research division of Zillow Group](https://www.zillow.com/research/), used with permission. The data represents the typical home values for the zip codes listed for homes falling between the 35th and 65th percentile of home values. General info on the dataset is available [here](https://www.zillow.com/research/zhvi-methodology-2019-highlights-26221), and full details are available [here](https://www.zillow.com/research/zhvi-methodology-2019-deep-26226).  
  
### Historical Data Examined  
Typical home values are published on the third Thursday of each month, and gives monthly data from 1996 to present.  

### Target Variable  
We will forecast data 12 months in the future for all relevant zip codes.  
  
## Methods  
Our methodology implements the CRISP-DM model for exploratory data analysis, cleaning, modeling, and evaluation.  
We leveraged SARIMAX modeling from [statsmodels](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.html) to analysis and forecast the home values. The quality of our modeling was determined with the (AIC value)[https://en.wikipedia.org/wiki/Akaike_information_criterion]. We also performed statistical analysis via [SciPy Stats](https://docs.scipy.org/doc/scipy/reference/stats.html) to further make inferences on the data.  
Other tools used include Python, NumPy, and Pandas. Visualizations were created with MatPlotLib and Seaborn.  
  
## Conclusion
After running SARIMAX analysis on all zip codes in Los Angeles and San Francisco, we found 3 zip codes from each that showed the greatest projected appreciation in value:  
<City>         |  Zip Codes                    | Projected </br> Home Value </br> Growth  
:--------------|:------------------------------|-----------------------------:  
Los Angeles    | 90210 </br> 90211 </br> 90355 | 14.4% </br> 13.1% </br> 11.9% 
San Francisco  | 97588 </br> 97567 </br> 97575 | 16.2% </br> 14.8% </br> 14.2% 


## Further Actions  
Using exogenous such as school district data, crime data, presence of parks/nature in vicinity, proximity to hospitals, groceries, entertainment etc., we can further refine our model as well as assign weights based on what a home buyer is looking to prioritize. We may find that growth in home value may be highly correlated to better education, lower crime rate, etc.   
We would like to further optimize our model by incorporating exogenous data on market changes, macroeconomic indicators, and other large scale fluctuations. With more data, we would be able to more accurately forecast home values into the future.  
      
## Index  
- **code/** — directory containing python code file
- **crisp_dm_process/** — directory for initial EDA and model notebook files  
  - **Initial_EDA** — notebook file that includes thorough initial data exploration, insights, and takeaways  
  - **Model_Evaluation** — notebook file that includes modeling trials and process.
- **data/** — directory of project datasets
- **images/** — directory containing the following...  
  - image exports of visualizations  
  - additional images for notebooks, README, and presentation slides
- **zillow_housing_final.ipynb** — primary project notebook  
- **Zillow_Housing_Projects_JS_WAX.pdf** - presentation slides PDF
- **README.md**  
  
## Bibliography  
1. Dataset Origin:  
  
                 Zillow Research Housing Data  
                        Zillow Group  
2. Date:    Thursday April 15, 2021
3. Web Source:  https://www.zillow.com/research/data/             
  
<div align="center";>Authors  
  <div align="center";>Jonathan Silverman & Alexander Xin  
    
[Jonathan's GitHub](https://github.com/silvermanjonathan) | [Alexander's GitHub](https://github.com/eggrollofchaos)  
[Jonathan's LinkedIn](https://www.linkedin.com/in/jonathansilverman007) | [Alexander's LinkedIn](https://www.linkedin.com/in/waximus)
