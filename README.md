# Relocation Recommender System
Recommending zip codes in a relocation city based on similarity to previous home zip code

When relocating to a new city, it is often difficult to determine where to live that will have a similar feel to home. Relocation families, know as "relos" in the real estate brokerage industry, often struggle to narrow down towns and wind up looking at homes in many very different communities. Families are often uprooted and are looking for a sense of stability and community. They often have limited time to make a decision and view homes, and end up making a hasty decision. The goal of this project is to build a recommender system that recommends a particular zip code near or in the city that the individual or family is looking to move to that will feel most like home. This tool will be helpful not only for moving families but for real estate agents looking to narrow down locations to show properties.


## Feature Selection

Data will come from the following sources:

The 5-Year American Community Survey, which includes information about people and housing characteristics (census.gov)
similarmaps.com (to map zip codes to cities).

Features were selected based on domain knowledge.

Features
Total Population
Population by age categories (5 year increments)
Education Overall (Percent with high school degree, bachelor’s degree, and graduate degree or higher)
Education by Gender (Percent with high school degree, bachelor’s degree, and graduate degree or higher)
Percent of families with children
Labor statistics (percentage of married couples with both, none, or just one spouse in the labor force, percentage of married couples with children with both, none, or just one spouse in the labor force, etc.)
Language (percent speaking just English, percent speaking Spanish, percent speaking another language)
Veterans as percentage of total population
Work transportation (Works remote, private vehicle, public transportation, walking)
Commute time
Percentage of homes that are owner occupied
Median Household Income (overall, owner occupied, and renter occupied)
Marital status (Married, never married, separated, divorced, widowed)
Home Price Index
Home Price Index % Annual Change
Population Density
Housing Type (Single Family Attached, Single Family Detached, 2-10+ unit apartments, mobile homes)
Year Homes Built
Length of tenure in current homes

## Testing Scenarios - All Features

Scenario #1: Dallas, TX, 75205 to Massachusetts

These predictions are expected; I transferred from a college in the 75205 zip code (SMU) to a college in Wellesley (Babson). There were many similarities, from the demographics to the house structures. I cannot quite speak to Andover, but I was surprised about Dover given that the density is much lower there and Westborough is much further away from the city. Chestnut Hill was an excellent match. The recommender did stick to cities that are within the Boston metropolitan area, however, which is  a positive sign.

When switching to the 75225 zip code, which borders 75205, the results are similar.I am not surprised that Weston has jumped into the number 1 position; the 75225 zip code encompasses Preston Hollow, which has slightly larger, more estate homes than the 75205 zip code.

Scenario #2: Dallas, TX 75205, 75225 to Washington state
These results are overall not surprising. Of all of the zip codes in Washington state, the majority of the zip codes the recommender selected are on the eastside of Seattle and are either part of or very close to the wealthy, cosmopolitan, highly educated city of Bellevue. The one Seattle proper zip code recommender, 98112, encompasses Madison Park and Montlake, two posh neighborhoods with tree lined streets and older mansions. It has a strong resemblance to the 75205 community in Dallas.

When switching to the 75225 community, we see Mercer Island jump to the top of the list. These results are also exactly what I would expect.

Scenario #3: 01230, Jamaica Plain, MA to Austin, TX


Jamaica Plain is a neighborhood in Boston known for its cozy shops, quirkiness, and artistic and creative vibe. While it attracts young adults, it is also family friendly. For someone moving to Austin, the 78704 zip code gives off a similar vibe. 78756 is the Brentwood neighborhood of Austin and 78757 is the Crestview neighborhood. Both are family friendly neighborhoods within the city.


Scenario #4: 01230, Jamaica Plain, MA to Seattle WA


98144 is part of the Beacon Hill neighborhood in Seattle. It is primarily residential and close to downtown, similar to Jamaica Plain. 98199 is part of the Magnolia neighborhood in Seattle, which is upscale and full of families. 98103 is the Green Lake neighborhood, which I am more familiar with. It is definitely full of active, young families and singles.

I evaluated the results based on zip codes I am personally familiar with to determine if they had a similar fit.

## Removing features

I removed one feature (or feature category) at a time to determine how the top 10 recommendations changed (if at all) for a particular zip code. I did this for several different types of zip codes (suburban, urban, in different states, etc) to be sure the recommender was working similarly across the board.

Please view this link for all outcomes: https://docs.google.com/spreadsheets/d/1RWeUA_npw3WvNmLDn2eideJk0rRiAzY1sG_v18jJFDE/edit#gid=0

I found that removing median household income, density, total population, or language had little to no effect on the top 10 recommendations. Employment characteristics had the largest effect of all features I looked at but it was still minimal.

The reason that removing one feature/feature category at a time had little impact on the recommendations is that several of these features are highly correlated with each other. For example, median household income is highly correlated with education, so if median household income is removed, it is still captured within education.

## Next steps

In the future, I would like to add school data, external location factors (such as the number of restaurants and coffee shops), and ultimately build a Flask app for public consumption.



