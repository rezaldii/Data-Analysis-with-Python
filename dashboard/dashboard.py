import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
day_df = pd.read_csv("day.csv")
hour_df = pd.read_csv("hour.csv")

# Set page title
st.title("Bike Sharing Analysis Dashboard")

# Sidebar for user input
data_choice = st.sidebar.selectbox("Select Data", ("Day Data", "Hour Data"))

if data_choice == "Day Data":
    data = day_df
else:
    data = hour_df

analysis_choice = st.sidebar.selectbox("Select Analysis", ("Temperature vs Rentals", "Season & Weather vs Rentals"))

# Main content
if analysis_choice == "Temperature vs Rentals":
    st.header("Temperature vs Bike Rentals")
    
    # Line plot for Temperature vs Average Rentals
    avg_cnt_by_temp = data.groupby('temp')['cnt'].mean()
    plt.figure(figsize=(10, 6))
    plt.plot(avg_cnt_by_temp.index, avg_cnt_by_temp.values)
    plt.title("Average Bike Rentals by Temperature")
    plt.xlabel("Temperature")
    plt.ylabel("Average Bike Rentals")
    st.pyplot(plt)
    
elif analysis_choice == "Season & Weather vs Rentals":
    st.header("Season & Weather vs Bike Rentals")
    
    # Bar plot for Season & Weather vs Average Rentals
    avg_cnt_by_season_weathersit = data.groupby(['season', 'weathersit'])['cnt'].mean().unstack()
    plt.figure(figsize=(10, 6))
    avg_cnt_by_season_weathersit.plot(kind='bar')
    plt.title("Average Bike Rentals by Season and Weather Situation")
    plt.xlabel("Season")
    plt.ylabel("Average Bike Rentals")
    st.pyplot(plt)
    
# Add more sections as needed for other analyses

# Footer
st.sidebar.text("Made with ❤️ by Rezaldi")
