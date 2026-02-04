import streamlit as st
import pandas as pd
import numpy as np


# Set page title
st.set_page_config(page_title="Researcher Profile and STEM Data Explorer", layout="wide")

# Sidebar Menu
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to:",
    ["Researcher Profile", "Publications", "STEM Data Explorer", "Contact"],
)

# Dummy STEM data
physics_data = pd.DataFrame({
    "Experiment": ["Alpha Decay", "Beta Decay", "Gamma Ray Analysis", "Quark Study", "Higgs Boson"],
    "Energy (MeV)": [4.2, 1.5, 2.9, 3.4, 7.1],
    "Date": pd.date_range(start="2024-01-01", periods=5),
})

astronomy_data = pd.DataFrame({
    "Celestial Object": ["Mars", "Venus", "Jupiter", "Saturn", "Moon"],
    "Brightness (Magnitude)": [-2.0, -4.6, -1.8, 0.2, -12.7],
    "Observation Date": pd.date_range(start="2024-01-01", periods=5),
})

weather_data = pd.DataFrame({
    "City": ["Cape Town", "London", "New York", "Tokyo", "Sydney"],
    "Temperature (°C)": [25, 10, -3, 15, 30],
    "Humidity (%)": [65, 70, 55, 80, 50],
    "Recorded Date": pd.date_range(start="2024-01-01", periods=5),
})

# Sections based on menu selection
if menu == "Researcher Profile":
    st.title("Researcher Profile")
    
    # Display basic profile information
    st.write("**Name:** Dr. Jane Doe")
    st.write("**Field of Research:** Astrophysics")
    st.write("**Institution:** University of Science")
    
    st.image(
        "https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg",
        caption="Nature (Pixabay)"
    )

elif menu == "Publications":
    st.title("Publications")
    
    # Upload publications file
    uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")
    if uploaded_file is not None:
        publications = pd.read_csv(uploaded_file)
        st.dataframe(publications)
        
        # Add filtering for year or keyword
        keyword = st.text_input("Filter by keyword", "")
        if keyword:
            # Simple filtering
            mask = publications.astype(str).apply(lambda x: x.str.contains(keyword, case=False)).any(axis=1)
            filtered = publications[mask]
            st.write(f"Filtered Results for '{keyword}':")
            st.dataframe(filtered)
        else:
            st.write("Showing all publications")

        # Publication trends
        if "Year" in publications.columns:
            st.subheader("Publication Trends")
            year_counts = publications["Year"].value_counts().sort_index()
            st.bar_chart(year_counts)
        else:
            st.write("The CSV does not have a 'Year' column to visualize trends.")

elif menu == "STEM Data Explorer":
    st.title("STEM Data Explorer")
    
    # Tabbed view for STEM data
    data_option = st.selectbox(
        "Choose a dataset to explore", 
        ["Physics Experiments", "Astronomy Observations", "Weather Data"]
    )

    if data_option == "Physics Experiments":
        st.write("### Physics Experiment Data")
        st.dataframe(physics_data)
        
        # Add widget to filter by Energy levels
        energy_filter = st.slider("Filter by Energy (MeV)", 0.0, 10.0, (0.0, 10.0))
        filtered_physics = physics_data[
            (physics_data["Energy (MeV)"] >= energy_filter[0]) & 
            (physics_data["Energy (MeV)"] <= energy_filter[1])
        ]
        st.write(f"Filtered Results for Energy Range {energy_filter}:")
        st.dataframe(filtered_physics)

    elif data_option == "Astronomy Observations":
        st.write("### Astronomy Observation Data")
        st.dataframe(astronomy_data)
        
        # Add widget to filter by Brightness
        brightness_filter = st.slider("Filter by Brightness (Magnitude)", -15.0, 5.0, (-15.0, 5.0))
        filtered_astronomy = astronomy_data[
            (astronomy_data["Brightness (Magnitude)"] >= brightness_filter[0]) & 
            (astronomy_data["Brightness (Magnitude)"] <= brightness_filter[1])
        ]
        st.write(f"Filtered Results for Brightness Range {brightness_filter}:")
        st.dataframe(filtered_astronomy)

    elif data_option == "Weather Data":
        st.write("### Weather Data")
        st.dataframe(weather_data)
        
        # Add widgets to filter by temperature and humidity
        col1, col2 = st.columns(2)
        with col1:
            temp_filter = st.slider("Filter by Temperature (°C)", -10.0, 40.0, (-10.0, 40.0))
        with col2:
            humidity_filter = st.slider("Filter by Humidity (%)", 0, 100, (0, 100))
        
        filtered_weather = weather_data[
            (weather_data["Temperature (°C)"] >= temp_filter[0]) & 
            (weather_data["Temperature (°C)"] <= temp_filter[1]) &
            (weather_data["Humidity (%)"] >= humidity_filter[0]) & 
            (weather_data["Humidity (%)"] <= humidity_filter[1])
        ]
        st.write(f"Filtered Results for Temperature {temp_filter} and Humidity {humidity_filter}:")
        st.dataframe(filtered_weather)

elif menu == "Contact":
    st.title("Contact Information")
    email = "jane.doe@example.com"
    st.write(f"You can reach me at {email}.")
