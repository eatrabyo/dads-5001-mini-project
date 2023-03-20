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
On January 14th, 2023, the Guardian reported that the death toll from COVID-19 in China had surged, with almost 60,000 deaths recorded in a five-week period. It is important to note that this figure only includes those who died in hospitals, and the actual number is expected to be higher.  

Earlier, on January 5th, 2023, the Thai government declared that Chinese travelers would only be tested for COVID-19. Shortly thereafter, on January 8th, 2023, China opened its borders to foreign visitors. On January 9th, 2023, the first 200 Chinese travelers arrived in Thailand.  

These events have sparked concern among public health officials regarding the potential spread of the virus, particularly given the high number of fatalities in China. As such, it is imperative that governments worldwide continue to monitor the situation closely and take all necessary measures to contain the spread of COVID-19.  

### Timeline
* 5th of January 2023 - The Thai government has declared that Chinese travelers would on be tested for COVID-19.
* 8th of January 2023 - China opened the country on the. 
* 9th of January 2023 - The first 200 Chinese travelers entered Thailand.
* 14th of January 2023 - the Guardian reported about the increase in fatalities in China.

### Overall Tourist Arrivals in Thailand (2019 - 2022)
* According to the **World Travel and Tourism Council (WTTC)**, travel and tourism contributed 21.6% to Thailand's GDP in 2019.
* In 2019, tourism supported 8.9 million jobs in the country, which is around 21.5% of total employment in Thailand.
* The number of international visitors increased from 35.4 million in 2017 to 38.3 million in 2018.
* In 2019, tourism generated revenue of around 1.9 trillion Baht for the Thai economy.
* The COVID-19 pandemic was officially declared by the World Health Organization (WHO) on March 11, 2020.  
The pandemic has significantly impacted Thailand's tourism industry, with the number of international visitors dropping by more than 80% in 2020 compared to the previous year as can be seen from the bar chart below.  
![overall_tourist_arrival](https://user-images.githubusercontent.com/92035314/226192653-db63a3b1-ebe4-438e-971f-586641cedc19.png)

### Overall Tourist Arrivals in Thailand by Region (2019 - 2022)
![over_by_region](https://user-images.githubusercontent.com/92035314/226194620-b3310c80-b903-4df3-98d3-ffadc12047cf.png)

From the source, we slice data from pandas by region to see the top region coming to Thailand.
The top 2 are East Asia and Europe which has 37.10 million and 11.59 million arrivals respectively in fig.1. East Asia and Europe have a huge impact on Thailand's tourism.  
When we convert the number of arrivals into proportions represented in fig. 2. East Asia and Europe have 63% and 20% respectively while other regions are not nearly 10 %.

## East Asia
### Proportion of Tourist Arrivals from East Asia (2019 - 2022)
![proportion_east_asia](https://user-images.githubusercontent.com/92035314/226196008-75c74e82-800d-4f61-85d2-fb00240737cc.png)

The graph shows the proportion of tourists from different countries in East Asia during 2019 - 2022. It can be seen that in this period, most tourists will come from China, which accounts for 34% of the total. In second place is Malaysia with 19%, followed by Laos, Korea, and Japan with 7%, Singapore with 5%, Vietnam, Cambodia, and Hong Kong with 4%, Indonesia and Taiwan with 3%, the Philippines and Myanmar with 2% and finally Brunei with 0%.  

We select the top 2 countries in East Asia to see the trend affected by COVID-19.
## Chinese Tourist
### Tourist Arrivals from China (2019 - 2022)
![line_china](https://user-images.githubusercontent.com/92035314/226198158-5bdd62ce-bd77-4fe6-8928-621deafaa868.png)

Chinese tourist have decrease due to COVID-19 situation. The number of arrivals drop from 11 million people in 2019 to 1.25 million in 2020. 
Eventhough, the pandemic situation in 2022 is calm in Thailand but not in China. The 2022's number, 0.27 million people, has increased but not nearly half of the number of people coming during 2019.

Due to lack of expenditure data in 2021 - 2022. We can only plot the changes in expenditure from 2018 to 2020.
![waterfall_china](https://user-images.githubusercontent.com/92035314/226198466-41abcba3-b409-48d6-9272-f91cd30f9e6c.png)

The expenditure from Chinese tourists in 2018 is 522,264.78 million Baht which increase a little in 2019 by 9,311.87 million Baht. And in 2020, during the outbreak of COVID-19, the spending of Chinese tourists decreased by 461,857.04 million Baht, resulting in the total net spending of Chinese tourists in the past 3 years at 69,719.61 million Baht.  

## Malaysian Tourist
### Tourist Arrivals from Malaysia (2019 -2022)
![line_malay](https://user-images.githubusercontent.com/92035314/226203798-8c75b352-53aa-4862-8a71-f3a3916fb924.png)

Malaysia is the 2nd country that likes to travel to Thailand. In 2019, 4.27 million Malaysian are coming to Thailand, and drop to 0.62 million people in 2020. The pandemic situation in Malaysia is less severe than in China. Therefore, we can see a good recovery from Malaysian people which is 1.95 million people visiting Thailand.  

![water_fall_malay_expend](https://user-images.githubusercontent.com/92035314/226199353-630fa5ff-b72b-4925-95c6-e9eba8c647ec.png)

The graph shows the expenditure of Malaysian tourists traveling to Thailand during 2018-2020. It can be seen that in 2018, Malaysian tourists spent 104,525.81 million Baht.
In 2019, the spending of tourists increased by 2,932.16 million Baht, and in 2020, during the pandemic of COVID-19, the spending decreased by 89,964.98 million Baht. Resulting in the total net spending of Malaysian tourists in the past 3 years at 17,492.99 million Baht.

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

The expenditure of tourists from the United Kingdom traveling to Thailand in 2018-2020 shows that it amounted to 72,458.57 million Baht in 2018. Then, the expenditure decreased by 139.84 million Baht in 2019 and the next year between the pandemic of COVID -19, the expenditure decreased by 56,840.37 million Baht. The total net expenditure in this period is 15,478.36 million Baht.

## Summary
From 4 countries we've analyzed, we can visualize the Top spending.
| Country        |   Total Spend (M. Baht) |
|:---------------|------------------------:|
| China          |             1123561.04 |
| Russia         |        242536           |
| Malaysia       |        229477           |
| United Kingdom |        160256           |

The top spending is China which spend 1,123,561.04 million Baht during 2018 - 2020. The rest are way too far from China spending.  
We can say that China have the most impact in Thailand's tourism.  

| Country        |   Spending per Capita (Baht/Day) |   Length of Stay (Days) |
|:---------------|---------------------------------:|------------------------:|
| China          |                          5842    |                 8.47333 |
| Malaysia       |                          4528.53 |                 5.93333 |
| Russia         |                          3880.56 |                16.7467  |
| United Kingdom |                          3873.17 |                18.11    |

Looking into Spending per Capita per Day, China still the first place which spend 5842 Baht per people per day.  
However, two countries from Europe are stay in Thailand longer than East Asia but spend less.  

| Country        |   Year |   Expenditure Change (M. Baht) |
|:---------------|-------:|-------------------------------:|
| China          |   2020 |                      -461857   |
| Malaysia       |   2020 |                       -89965   |
| Russia         |   2020 |                       -68282.3 |
| United Kingdom |   2020 |                       -56840.4 |

The changes in expenditure. We lost 461857 million Baht from China in 2020. That is the hughe amount of income we lost during the pandemic.
