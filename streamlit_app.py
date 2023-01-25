#Import Python Libraries
import pandas as pd
import folium #to install folium using Anaconda: conda install -c conda-forge folium
import geopandas as gpd #to install geopandas, run this code in the conda terminal: conda install geopandas
from folium.features import GeoJsonTooltip
import streamlit as st #You can follow the instructions in the beginner tutorial to install Streamlit if you don't have it
from streamlit_folium import folium_static

@st.cache
def read_csv(path):
    return pd.read_csv(path, compression='gzip', sep='\t', quotechar='"')

housing_price_df=read_csv('.../county_market_tracker.tsv000.gz') #Replace ... with your file path
housing_price_df=housing_price_df[(housing_price_df['period_begin']>='2020-10-01') & (housing_price_df['period_begin']<='2021-10-01')] #only look at past 12 months' data
county_fips=pd.read_csv('.../county_fips.csv')
county_fips['region']=county_fips["Name"] + ' County, '+ county_fips["State"] #Create a new column called 'region' which is the concatenation of county name and state. This column will be used in the next step to join housing_price_df with county_fips

housing_price_df= housing_price_df.merge(county_fips, on="region", how="left") 
housing_price_df['FIPS'] = housing_price_df['FIPS'].astype(str).replace('\.0', '', regex=True)
housing_price_df["county_fips"] = housing_price_df["FIPS"].str.zfill(5)

@st.cache
def read_file(path):
    return gpd.read_file(path)

#Read the geojson file
gdf = read_file('.../georef-united-states-of-america-county.geojson')

#Merge the housing market data and geojson file into one dataframe
df_final = gdf.merge(housing_price_df, left_on="coty_code", right_on="county_fips", how="outer") #join housing_price_df with gdf to get the geometries column from geojson file
df_final= df_final[~df_final['period_begin'].isna()]  
df_final = df_final[~df_final['geometry'].isna()]
df_final=df_final[['period_begin','period_end', 'region','parent_metro_region','state_code',"property_type",'median_sale_price','median_sale_price_yoy','homes_sold','homes_sold_yoy','new_listings',
                   'new_listings_yoy','median_dom','avg_sale_to_list',"county_fips",'geometry']]
df_final.rename({'median_sale_price': 'Median Sales Price',
                 'median_sale_price_yoy': 'Median Sales Price (YoY)',
                 'homes_sold':'Homes Sold',
                 'homes_sold_yoy':'Homes Sold (YoY)',
                 'new_listings':'New Listings',
                 'new_listings_yoy':'New Listings (YoY)',
                 'median_dom':'Median Days-on-Market',
                 'avg_sale_to_list':'Avg Sales-to-Listing Price Ratio'}, 
                 axis=1, inplace=True) 

#st.write(df_final.head())  
