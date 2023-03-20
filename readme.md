# DADS 5001 Mini Project

## Tourism in Thailand during COVID-19 Situation

### Contributors of this project
* Itthisak Pratukaew
* Karuntarat Komtongkaew

## Source
1. [Ministry of Tourism and Sport of Thailand](https://www.mots.go.th/more_news_new.php?cid=411)
2. [National Statistical Office of Thailand](http://statbbi.nso.go.th/staticreport/page/sector/en/17.aspx)
3. [The Guardian](https://www.theguardian.com/world/2023/jan/14/nearly-60000-people-have-died-of-covid-in-china-in-past-five-weeks)

## Introduction
The recent events surrounding the outbreak of COVID-19 in China have sent shockwaves throughout the global community. As reported by the Guardian on January 14th, 2023, the death toll in China has surged to almost 60,000 in a mere five-week period. However, this number only accounts for deaths recorded in hospitals, and the actual figure is feared to be even higher.  

Against this backdrop, on January 5th, 2023, the Thai government made a controversial decision to only test Chinese travelers for COVID-19. This decision has raised serious concerns among the people, who fear that it could lead to a spike in infections and deaths. Moreover, on January 8th, 2023, China opened its borders to foreign visitors, and on January 9th, 2023, the first 200 Chinese travelers arrived in Thailand.  

The potential repercussions of these developments cannot be understated. With the high number of fatalities in China, it is understandable that locals in Thailand are apprehensive about the spread of the virus. As such, it is incumbent upon governments worldwide to remain vigilant and take all necessary measures to contain the outbreak of COVID-19.  

Against this backdrop, we seek to investigate whether the Thai government's decision to not test Chinese travelers for COVID-19 was reasonable. By analyzing the available data and information, we hope to shed light on this important issue and contribute to the ongoing efforts to combat the spread of this deadly virus.  

### Timeline
* 5th of January 2023 - The Thai government has declared that Chinese travelers would on be tested for COVID-19.
* 8th of January 2023 - China opened the country on the. 
* 9th of January 2023 - The first 200 Chinese travelers entered Thailand.
* 14th of January 2023 - the Guardian reported about the increase in fatalities in China.

### Overall Tourist Arrivals in Thailand (2019 - 2022)
*	The number of international visitors increased from 35.4 million in 2017 to 38.3 million in 2018.
*	According to the **World Travel and Tourism Council (WTTC)**, travel and tourism contributed 21.6% to Thailand's GDP in 2019.
*	In 2019, tourism supported 8.9 million jobs in the country, which is around 21.5% of total employment in Thailand.
*	In 2019, tourism generated revenue of around 1.9 trillion Baht for the Thai economy.
* The COVID-19 pandemic was officially declared by the World Health Organization (WHO) on March 11, 2020.
The pandemic has significantly impacted Thailand's tourism industry, with the number of international visitors dropping by more than 80% in 2020 compared to the previous year as can be seen from the bar chart below.

![overall_tourist_arrival](https://user-images.githubusercontent.com/92035314/226192653-db63a3b1-ebe4-438e-971f-586641cedc19.png)

### Overall Tourist Arrivals in Thailand by Region (2019 - 2022)
![over_by_region](https://user-images.githubusercontent.com/92035314/226194620-b3310c80-b903-4df3-98d3-ffadc12047cf.png)

From slicing the data from pandas by region, it was revealed that the top two regions contributing to Thailand's tourism were East Asia and Europe, with 37.10 million and 11.59 million arrivals, respectively, as shown in Figure 1. These regions exerted a significant influence on Thailand's tourism industry.  

Upon further analysis, it was found that when the number of arrivals for each region was converted into proportions, as depicted in Figure 2, East Asia and Europe emerged as the major players, accounting for 63% and 20% of the total, respectively. In contrast, the other regions collectively contributed less than 10%, highlighting the significant impact of East Asia and Europe on Thailand's tourism landscape.  

From this point onwards, the focus will be on delving deeper into East Asia and Europe by selecting the top two countries from each region for further analysis. For each country, two important pieces of information are presented: the number of arrivals and expenditures. The number of arrivals is displayed on a line chart, which allows for the identification of trends over time. In contrast, expenditure is visualized using a waterfall graph, providing a clear view of the increases and decreases in expenditure for each year. Additionally, the net value after the considered period is also shown.  

## East Asia
### Proportion of Tourist Arrivals from East Asia (2019 - 2022)
![proportion_east_asia](https://user-images.githubusercontent.com/92035314/226196008-75c74e82-800d-4f61-85d2-fb00240737cc.png)

The pie graph illustrates the proportion of tourists from various East Asian countries for the period between 2019 and 2022. As per the data, the highest proportion of visitors was from China, constituting 34% of the total visitors. Following China, Malaysia was the second-highest contributor with 19%, trailed by Laos, Korea, and Japan with 7% each. Singapore accounted for 5% of the visitors, while Vietnam, Cambodia, and Hong Kong were likely to share 4% of the total each. Additionally, Indonesia and Taiwan contributed 3% each, while the Philippines and Myanmar accounted for 2% each. Lastly, Brunei represented 0% of the total East Asian tourists visiting the region during the aforementioned period.
The top 2 countries in East Asia, China, and Malaysia were selected to see the trend affected by COVID-19.  

## Chinese Tourist
### Tourist Arrivals from China (2019 - 2022)
![line_china](https://user-images.githubusercontent.com/92035314/226198158-5bdd62ce-bd77-4fe6-8928-621deafaa868.png)

The COVID-19 pandemic has had a profound impact on the number of Chinese tourists visiting Thailand, with the number of arrivals plummeting from 11 million in 2019 to 1.25 million in 2020. While the pandemic situation in Thailand has stabilized by 2022, the situation remains uncertain in China. As a result, the number of Chinese tourists visiting Thailand in 2022 has risen to 0.27 million. However, this figure falls considerably short of the pre-pandemic levels recorded in 2019.  

Unfortunately, the lack of expenditure data for the years 2021 and 2022 means that changes in spending patterns cannot be assessed for these years. Instead, we can only examine the trends in expenditure from 2018 to 2020.  

![waterfall_china](https://user-images.githubusercontent.com/92035314/226198466-41abcba3-b409-48d6-9272-f91cd30f9e6c.png)

In 2018, the expenditure of Chinese tourists in Thailand was recorded at 522,264.78 million Baht, experiencing a slight increase of 9,311.87 million Baht in 2019. However, the onset of the COVID-19 pandemic in 2020 saw a drastic decline in the spending of Chinese tourists, dropping by a staggering 461,857.04 million Baht. This led to the cumulative net expenditure of Chinese tourists over the past three years reaching 69,719.61 million Baht.   

## Malaysian Tourist
### Tourist Arrivals from Malaysia (2019 -2022)
![line_malay](https://user-images.githubusercontent.com/92035314/226203798-8c75b352-53aa-4862-8a71-f3a3916fb924.png)

Malaysia stands as the second-largest contributor of visitors to Thailand. The number of Malaysian visitors to Thailand amounted to 4.27 million in 2019. However, this figure dropped drastically to 0.62 million in 2020, due to the COVID-19 pandemic.   

![water_fall_malay_expend](https://user-images.githubusercontent.com/92035314/226199353-630fa5ff-b72b-4925-95c6-e9eba8c647ec.png)

The waterfall graph represents the expenditure of Malaysian tourists during their visits to Thailand from 2018 to 2020. It can be observed that in 2018, Malaysian tourists spent 104,525.81 million Baht, which saw a marginal increase of 2,932.16 million Baht in 2019. However, the COVID-19 pandemic's impact was visible in 2020, as the spending by Malaysian tourists saw a sharp decline of 89,964.98 million Baht. The cumulative net expenditure of Malaysian tourists during the three years from 2018 to 2020 amounted to 17,492.99 million Baht.  

## Europe
![europe_proportion](https://user-images.githubusercontent.com/92035314/226199398-889faf54-7cbc-4c0b-a6fc-b6671e1f58d1.png)

The proportion of European countries coming to Thailand during 2019 - 2022. The top 2 are Russia and the United Kingdom considered as 25% and 17% respectively.  
Unlike East Asia, The third place is Germany which has a high portion in the pie chart at 15% followed by 13% from France. The rest are below 10%.  

The focusing country will be the top 2 which are Russia and the United Kingdom.

## Russia
### Tourist Arrvials from Russia (2019 - 2022)
![line_russia](https://user-images.githubusercontent.com/92035314/226199897-f9cadd8f-1a6a-4efd-b4c0-411b49474bfa.png)

Like the other countries, the line chart has the same shape. In 2019, 1.48 million Russian visited Thailand which significantly drop to 0.03 million people when the pandemic situation is worst. The recovery number is 0.44 million people in 2022.

![water_fall_russia](https://user-images.githubusercontent.com/92035314/226200602-778d25bd-a877-47fb-9dc0-53147c65bd75.png)

The expenditure of tourists from Russia who traveled to Thailand in 2018 is 105,028.29 million Baht. In 2019 was decreased by 2,133.26 million Baht and in 2020 the spending decreased by 68,282.26 million Baht because the pandemic of COVID-19, so the total net spending of Russian tourists is 34,612.77 million Baht in the past 3 years.

## United Kingdom
### Tourist Arrivals from United Kingdom (2019 - 2022)
![uk_line](https://user-images.githubusercontent.com/92035314/226201488-05a5d65c-862d-4b12-80f4-7ca73c2f2f82.png)

UK people visited Thailand with nearly 1 million people in 2019. The number during the COVID-19 pandemic is almost identical to Russia. In 2020, the number dropped to 0.59 million people and the lowest at 0.03 million people in 2021. The recovery number is 0.44 million people like in Russia.  

![water_fall_uk](https://user-images.githubusercontent.com/92035314/226203232-e265103e-9b4f-4b4a-bc64-530f42f9e56a.png)

The expenditure of tourists from the United Kingdom traveling to Thailand in 2018-2020 shows that it amounted to 72,458.57 million Baht in 2018. Then, the expenditure decreased by 139.84 million Baht in 2019 and the next year between the pandemic of COVID-19, the expenditure decreased by 56,840.37 million Baht. The total net expenditure in this period is 15,478.36 million Baht.

## Summary
From the 4 countries selected, it can visualize the Top spender in the table below. The top spending is China which spent 1,123,561 million Baht during 2018 - 2020. The rest counties were substantially lower than China's spending. It can be concluded that China has an influence on Thai tourism.  
| Country        |   Total Spend (M. Baht) |
|:---------------|------------------------:|
| China          |             1,123,561   |
| Russia         |        242,536          |
| Malaysia       |        229,477          |
| United Kingdom |        160,256          |
 
Next, Spending per Capita per Day is considered. China was still the first place which spent 5,842 Baht per person per day. Comparing Russian and British travelers with Chinese travelers, the Chinese spent more in a twice shorter stay. This makes Chinese travelers even more attractive to the Thai tourism industry.
| Country        |   Spending per Capita (Baht/Day) |   Length of Stay (Days) |
|:---------------|---------------------------------:|------------------------:|
| China          |                          5,842   |                 8       |
| Malaysia       |                          4,529   |                 6       |
| Russia         |                          3,881   |                17       |
| United Kingdom |                          3,873   |                18       |
 

The changes in expenditure Thailand lost during the pandemic. We lost 461,857 million Baht from China alone in 2020. That is the enormous amount of income that Thailand could have gained during the normal situation.  

| Country        |   Year |   Expenditure Change (M. Baht) |
|:---------------|-------:|-------------------------------:|
| China          |   2020 |                      -461,857  |
| Malaysia       |   2020 |                       -89,965  |
| Russia         |   2020 |                       -68,282  |
| United Kingdom |   2020 |                       -56,840  |

In summary, it can be concluded that the Thai economy heavily depends on Chinese travelers. As such, it is imperative for the government to devise alternative plans or revise existing strategies to mitigate the risks of relying on a single market. By eliminating the single failure mode, the Thai economy can achieve a greater degree of stability and sustainability.  

