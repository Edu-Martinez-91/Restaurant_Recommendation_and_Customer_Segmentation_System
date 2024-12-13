import streamlit as st
import os
import pandas as pd
import numpy as np
from math import pi
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from wordcloud import WordCloud
import warnings
from matplotlib.colors import LinearSegmentedColormap
from PIL import Image

st.set_page_config(layout="wide")
warnings.filterwarnings('ignore')
plt.rcParams['axes.prop_cycle'] = plt.cycler(color=['#FF7F7F', '#FFF9C4', '#A5D6A7', '#81D4FA', '#F1F1F1'])
mexican_palette = ['#FF7F7F', '#FFF9C4', '#A5D6A7', '#81D4FA', '#F1F1F1']
pd.set_option('display.max_columns', None)


df_user = pd.read_csv("../data/df_user.csv")
df_location = pd.read_csv("../data/df_location.csv")
df_usloc = pd.read_csv("../data/df_usloc.csv")
df_filter_collapsed=pd.read_csv("../data/df_filter_collapsed.csv")
df_filter=pd.read_csv("../data/df_filter.csv")


st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto+Condensed:wght@400;700&display=swap');
    html, body, [class*="css"]  {
        font-family: 'Roboto Condensed', sans-serif;
    }
        .centered-header {
        text-align: center;
        font-size: 32px;
        font-weight: bold;
        color: #006341; /* Verde mexicano */
    }
    .centered-header span:nth-child(1) { color: #006341; } /* Verde */
    .centered-header span:nth-child(2) { color: #ffffff; } /* Blanco */
    .centered-header span:nth-child(3) { color: #ce1126; } /* Rojo */
    .centered-header {
        text-align: center; /* Centra el título horizontalmente */
    }
    .right-aligned-header {
        text-align: right; /* Alinea a la derecha */
        margin-right: 160px; /* Margen ajustable */
    }
    </style>
    """, 
    unsafe_allow_html=True
)

image = Image.open("Heading1.png")
width, height = image.size
new_height = height // 5
resized_image = image.resize((width, new_height))

st.image(resized_image, caption="", use_column_width=True)

st.title("Welcome to Dishcovery")

opcion = st.selectbox("Tell us about you:", ["I'm a Dishcoverer", "I'm a Dishtributor"])

if opcion == "I'm a Dishcoverer":
    sub_opcion = st.sidebar.radio("Select an option:", ["Dishcard Lite","Dishcard"])

    if sub_opcion == "Dishcard Lite":
        st.markdown('<br><br>', unsafe_allow_html=True)
        st.markdown('<br><br>', unsafe_allow_html=True)

        st.title("Dishcard")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            filter1 = st.selectbox("Select a city", ['-'] + df_filter_collapsed['City'].unique().tolist(), index=0)
            filter2 = st.selectbox("Select an alcohol availability", ['-'] + df_filter_collapsed['Alcohol Availability'].unique().tolist(), index=0)
            filter3 = st.selectbox("Select Smoking Policies", ['-'] + df_filter_collapsed['Smoking Area'].unique().tolist(), index=0)

        with col2:
            filter4 = st.selectbox("Select Dress Code", ['-'] + df_filter_collapsed['Dress Code'].unique().tolist(), index=0)
            filter5 = st.selectbox("Select Accessibility", ['-'] + df_filter_collapsed['Accessibility'].unique().tolist(), index=0)
            filter6 = st.selectbox("Select Price Range", ['-'] + df_filter_collapsed['Price Range'].unique().tolist(), index=0)

        with col3:
            filter7 = st.selectbox("Select Ambience", ['-'] + df_filter_collapsed['Ambience'].unique().tolist(), index=0)
            filter8 = st.selectbox("Select Area", ['-'] + df_filter_collapsed['Area'].unique().tolist(), index=0)
            filter9 = st.selectbox("Select Cuisine Type", ['-'] + df_filter_collapsed['Cuisine Type'].unique().tolist(), index=0)

        with col4:
            filter10 = st.selectbox("Select Parking Availability", ['-'] + df_filter_collapsed['Parking Availability'].unique().tolist(), index=0)
            filter11 = st.selectbox("Select Payment Methods", ['-'] + df_filter_collapsed['Payment Methods'].unique().tolist(), index=0)
            filter12 = st.selectbox("Select Operating Days", ['-'] + df_filter_collapsed['Operating Days'].unique().tolist(), index=0)

        if st.button("Show recommendations"):
            if filter1 == '-' and filter2 == '-' and filter3 == '-' and filter4 == '-' and filter5 == '-' and filter6 == '-' and filter7 == '-' and filter8 == '-' and filter9 == '-' and filter10 == '-' and filter11 == '-' and filter12 == '-':
                st.write("Please select at least one filter.")
            else:
                df_filtered = df_filter_collapsed[
                    (filter1 == '-' or df_filter_collapsed['City'] == filter1) &
                    (filter2 == '-' or df_filter_collapsed['Alcohol Availability'] == filter2) &
                    (filter3 == '-' or df_filter_collapsed['Smoking Area'] == filter3) &
                    (filter4 == '-' or df_filter_collapsed['Dress Code'] == filter4) &
                    (filter5 == '-' or df_filter_collapsed['Accessibility'] == filter5) &
                    (filter6 == '-' or df_filter_collapsed['Price Range'] == filter6) &
                    (filter7 == '-' or df_filter_collapsed['Ambience'] == filter7) &
                    (filter8 == '-' or df_filter_collapsed['Area'] == filter8) &
                    (filter9 == '-' or df_filter_collapsed['Cuisine Type'] == filter9) &
                    (filter10 == '-' or df_filter_collapsed['Parking Availability'] == filter10) &
                    (filter11 == '-' or df_filter_collapsed['Payment Methods'] == filter11) &
                    (filter12 == '-' or df_filter_collapsed['Operating Days'] == filter12)
                ].drop_duplicates(subset='Restaurant Name')

                st.markdown('<br><br>', unsafe_allow_html=True)
                st.markdown('<br><br>', unsafe_allow_html=True)

                st.markdown('<div class="centered-header">Our recommendation:</div>', unsafe_allow_html=True)

                col1, col2 = st.columns(2)

                with col1:
                    st.markdown('<br><br>', unsafe_allow_html=True)
                    st.markdown(
                        f"""
                        <div style="max-height: 500px; overflow-y: scroll;">
                            <style>
                                table {{
                                    width: 100%;
                                    border-collapse: collapse;
                                    border-radius: 10px;
                                    overflow: hidden; 
                                    border: 1px solid #ddd;
                                }}
                                th {{
                                    position: sticky;
                                    top: 0;
                                    background-color: #A5D6A7;
                                    text-align: center;
                                    font-weight: bold;
                                    padding: 10px;
                                    z-index: 1; 
                                    color: black; 
                                    border-bottom: 2px solid #ddd;
                                }}
                                td {{
                                    text-align: center;
                                    padding: 10px;
                                    border: 1px solid #ddd;
                                }}
                            </style>
                            {df_filtered[["Restaurant Name", "City"]].to_html(index=False)}
                        </div>
                        """, unsafe_allow_html=True)

                with col2:
                    fig = px.scatter_mapbox(df_filtered, 
                                            lat="latitude", 
                                            lon="longitude", 
                                            hover_name="Restaurant Name", 
                                            hover_data=["Address", "City"], 
                                            zoom=10)

                    fig.update_layout(
                        mapbox_style="carto-positron",
                        height=650
                    )

                    st.plotly_chart(fig)

    
    elif sub_opcion == "Dishcard":
        st.markdown('<br><br>', unsafe_allow_html=True)
        st.markdown('<br><br>', unsafe_allow_html=True)

        st.markdown(
            """
            <h1 style="text-align: center; font-size: 2.5em;">Dishcard+</h1>
            """, 
            unsafe_allow_html=True
        )
        
        st.markdown('<br><br>', unsafe_allow_html=True)
        st.header("What you want:")
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            filter1 = st.selectbox("Select a city", ['-'] + df_filter['City'].unique().tolist(), index=0)
            filter2 = st.selectbox("Select an alcohol availability", ['-'] + df_filter['Alcohol Availability'].unique().tolist(), index=0)
            filter3 = st.selectbox("Select Smoking Policies", ['-'] + df_filter['Smoking Area'].unique().tolist(), index=0)

        with col2:
            filter4 = st.selectbox("Select Dress Code", ['-'] + df_filter['Dress Code'].unique().tolist(), index=0)
            filter5 = st.selectbox("Select Accessibility", ['-'] + df_filter['Accessibility'].unique().tolist(), index=0)
            filter6 = st.selectbox("Select Price Range", ['-'] + df_filter['Price Range'].unique().tolist(), index=0)

        with col3:
            filter7 = st.selectbox("Select Ambience", ['-'] + df_filter['Ambience'].unique().tolist(), index=0)
            filter8 = st.selectbox("Select Area", ['-'] + df_filter['Area'].unique().tolist(), index=0)
            filter9 = st.selectbox("Select Cuisine Type", ['-'] + df_filter['Cuisine Type'].unique().tolist(), index=0)

        with col4:
            filter10 = st.selectbox("Select Parking Availability", ['-'] + df_filter['Parking Availability'].unique().tolist(), index=0)
            filter11 = st.selectbox("Select Payment Methods", ['-'] + df_filter['Payment Methods'].unique().tolist(), index=0)
            filter12 = st.selectbox("Select Operating Days", ['-'] + df_filter['Operating Days'].unique().tolist(), index=0)

        st.header("What you are:")

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            filter13 = st.selectbox("Select Smoking Habit", ['-'] + df_filter['Smoking Habit'].unique().tolist(), index=0)
            filter14 = st.selectbox("Select Drinking Habit", ['-'] + df_filter['Drinking Habit'].unique().tolist(), index=0)
            filter15 = st.selectbox("Select Dress Preference", ['-'] + df_filter['Dress Preference'].unique().tolist(), index=0)

        with col2:
            filter16 = st.selectbox("Select Preferred Ambience", ['-'] + df_filter['Preferred Ambience'].unique().tolist(), index=0)
            filter17 = st.selectbox("Select Transport Mode", ['-'] + df_filter['Transport Mode'].unique().tolist(), index=0)
            filter18 = st.selectbox("Select Marital Status", ['-'] + df_filter['Marital Status'].unique().tolist(), index=0)

        with col3:
            filter19 = st.selectbox("Select People Under Charge", ['-'] + df_filter['People Under Charge'].unique().tolist(), index=0)
            filter20 = st.selectbox("Select Interest", ['-'] + df_filter['Interest'].unique().tolist(), index=0)
            filter21 = st.selectbox("Select Personality", ['-'] + df_filter['Personality'].unique().tolist(), index=0)

        with col4:
            filter22 = st.selectbox("Select Religion", ['-'] + df_filter['Religion'].unique().tolist(), index=0)
            filter23 = st.selectbox("Select Activity Level", ['-'] + df_filter['Activity Level'].unique().tolist(), index=0)
            filter24 = st.selectbox("Select Favorite Color", ['-'] + df_filter['Favorite Color'].unique().tolist(), index=0)
        
        with col5:
            filter25 = st.selectbox("Select Budget", ['-'] + df_filter['Budget'].unique().tolist(), index=0)
            filter26 = st.selectbox("Preferred Payment Method", ['-'] + df_filter['Preferred Payment Method'].unique().tolist(), index=0)
            filter27 = st.selectbox("Select User Preference", ['-'] + df_filter['User Preference'].unique().tolist(), index=0)

        if st.button("Show recommendations"):
            if (filter1 == '-' and filter2 == '-' and filter3 == '-' and filter4 == '-' and filter5 == '-' and filter6 == '-' and
                filter7 == '-' and filter8 == '-' and filter9 == '-' and filter10 == '-' and filter11 == '-' and filter12 == '-' and
                filter13 == '-' and filter14 == '-' and filter15 == '-' and filter16 == '-' and filter17 == '-' and filter18 == '-' and
                filter19 == '-' and filter20 == '-' and filter21 == '-' and filter22 == '-' and filter23 == '-' and filter24 == '-' and
                filter25 == '-' and filter26 == '-' and filter27 == '-'):
                st.write("Please select at least one filter.")
                
            else:
                df_filtered = df_filter[
                    (filter1 == '-' or df_filter['City'] == filter1) &
                    (filter2 == '-' or df_filter['Alcohol Availability'] == filter2) &
                    (filter3 == '-' or df_filter['Smoking Area'] == filter3) &
                    (filter4 == '-' or df_filter['Dress Code'] == filter4) &
                    (filter5 == '-' or df_filter['Accessibility'] == filter5) &
                    (filter6 == '-' or df_filter['Price Range'] == filter6) &
                    (filter7 == '-' or df_filter['Ambience'] == filter7) &
                    (filter8 == '-' or df_filter['Area'] == filter8) &
                    (filter9 == '-' or df_filter['Cuisine Type'] == filter9) &
                    (filter10 == '-' or df_filter['Parking Availability'] == filter10) &
                    (filter11 == '-' or df_filter['Payment Methods'] == filter11) &
                    (filter12 == '-' or df_filter['Operating Days'] == filter12) &
                    (filter13 == '-' or df_filter['Smoking Habit'] == filter13) &
                    (filter14 == '-' or df_filter['Drinking Habit'] == filter14) &
                    (filter15 == '-' or df_filter['Dress Preference'] == filter15) &
                    (filter16 == '-' or df_filter['Preferred Ambience'] == filter16) &
                    (filter17 == '-' or df_filter['Transport Mode'] == filter17) &
                    (filter18 == '-' or df_filter['Marital Status'] == filter18) &
                    (filter19 == '-' or df_filter['People Under Charge'] == filter19) &
                    (filter20 == '-' or df_filter['Interest'] == filter20) &
                    (filter21 == '-' or df_filter['Personality'] == filter21) &
                    (filter22 == '-' or df_filter['Religion'] == filter22) &
                    (filter23 == '-' or df_filter['Activity Level'] == filter23) &
                    (filter24 == '-' or df_filter['Favorite Color'] == filter24) &
                    (filter25 == '-' or df_filter['Budget'] == filter25) &
                    (filter26 == '-' or df_filter['Preferred Payment Method'] == filter26) &
                    (filter27 == '-' or df_filter['User Preference'] == filter27)
                ].drop_duplicates(subset='Restaurant Name')

                st.markdown('<br><br>', unsafe_allow_html=True)
                st.markdown('<br><br>', unsafe_allow_html=True)

                st.markdown('<div class="centered-header">Our recommendation:</div>', unsafe_allow_html=True)

                col1, col2 = st.columns(2)

                with col1:
                    st.markdown('<br><br>', unsafe_allow_html=True)
                    st.markdown(
                        f"""
                        <div style="max-height: 500px; overflow-y: scroll;">
                            <style>
                                table {{
                                    width: 100%;
                                    border-collapse: collapse;
                                    border-radius: 10px;
                                    overflow: hidden; 
                                    border: 1px solid #ddd;
                                }}
                                th {{
                                    position: sticky;
                                    top: 0;
                                    background-color: #A5D6A7;
                                    text-align: center;
                                    font-weight: bold;
                                    padding: 10px;
                                    z-index: 1; 
                                    color: black; 
                                    border-bottom: 2px solid #ddd;
                                }}
                                td {{
                                    text-align: center;
                                    padding: 10px;
                                    border: 1px solid #ddd;
                                }}
                            </style>
                            {df_filtered[["Restaurant Name", "City","Rating","Food Rating","Service Rating"]].to_html(index=False)}
                        </div>
                        """, unsafe_allow_html=True
                    )

                with col2:
                    fig = px.scatter_mapbox(df_filtered, 
                                            lat="latitude", 
                                            lon="longitude", 
                                            hover_name="Restaurant Name", 
                                            hover_data=["Address", "City"], 
                                            zoom=10)

                    fig.update_layout(
                        mapbox_style="carto-positron",
                        height=650
                    )

                    st.plotly_chart(fig)



elif opcion == "I'm a Dishtributor":

    sub_opcion = st.sidebar.radio("Select an option:", ["Join our network of restaurants","Segmentoid"])
    
    if sub_opcion == "Join our network of restaurants":
        st.markdown('<br><br>', unsafe_allow_html=True)
        st.markdown('<br><br>', unsafe_allow_html=True)
        st.markdown('<h2 class="centered-header">Regarding the restaurants</h2>', unsafe_allow_html=True)
        st.map(df_location)
        text = ' '.join(df_location['Rcuisine'].dropna().astype(str))


        st.markdown('<br><br>', unsafe_allow_html=True)
        st.markdown('<br><br>', unsafe_allow_html=True)

        
        custom_cmap = LinearSegmentedColormap.from_list('mexican_cmap', mexican_palette)

        wordcloud = WordCloud(width=800, height=400, background_color="#f6c643", colormap=custom_cmap).generate(text)

        st.markdown('<h2 class="centered-header">Different flavours</h2>', unsafe_allow_html=True)
        plt.figure(figsize=(50, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        st.pyplot()

    elif sub_opcion == "Segmentoid":
        st.markdown('<br><br>', unsafe_allow_html=True)
        st.markdown('<br><br>', unsafe_allow_html=True)
        st.markdown('<h2 class="centered-header">Segmentoid</h2>', unsafe_allow_html=True)

        st.subheader("What you offer:")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            filter1 = st.selectbox("Select an alcohol availability", ['-'] + df_filter['Alcohol Availability'].unique().tolist(), index=0)
            filter2 = st.selectbox("Select Smoking Policies", ['-'] + df_filter['Smoking Area'].unique().tolist(), index=0)
            filter3 = st.selectbox("Select Dress Code", ['-'] + df_filter['Dress Code'].unique().tolist(), index=0)

        with col2:
            filter4 = st.selectbox("Select Accessibility", ['-'] + df_filter['Accessibility'].unique().tolist(), index=0)
            filter5 = st.selectbox("Select Price Range", ['-'] + df_filter['Price Range'].unique().tolist(), index=0)
            filter6 = st.selectbox("Select Ambience", ['-'] + df_filter['Ambience'].unique().tolist(), index=0)

        with col3:
            filter7 = st.selectbox("Select Area", ['-'] + df_filter['Area'].unique().tolist(), index=0)
            filter8 = st.selectbox("Select Cuisine Type", ['-'] + df_filter['Cuisine Type'].unique().tolist(), index=0)
            filter9 = st.selectbox("Select Parking Availability", ['-'] + df_filter['Parking Availability'].unique().tolist(), index=0)

        with col4:
            filter10 = st.selectbox("Select Payment Methods", ['-'] + df_filter['Payment Methods'].unique().tolist(), index=0)
            filter11 = st.selectbox("Select Operating Days", ['-'] + df_filter['Operating Days'].unique().tolist(), index=0)

        st.subheader("Your Target")

        col1, col2, col3 = st.columns([0.3, 0.3, 0.3])

        mode = None
        with col1:
            if st.button("Strict Mode"):
                mode = "Strict Mode"
        with col2:
            if st.button("Relaxed Mode"):
                mode = "Relaxed Mode"
        with col3:
            if st.button("Avoidance Mode"):
                mode = "Avoidance Mode"

        if mode:
            if mode == "Strict Mode":
                df_filtered = df_filter[df_filter["Rating"] == "Satisfied"]
            elif mode == "Relaxed Mode":
                df_filtered = df_filter[df_filter["Rating"].isin(["Neutral", "Satisfied"])]
            else:
                df_filtered = df_filter[df_filter["Rating"] == "Dissatisfied"]

            df_filtered = df_filtered.drop_duplicates(subset='User ID')

            st.markdown("### Filtered Data")
            st.markdown(
                f"""
                <div style="max-height: 500px; overflow-y: scroll;">
                    <style>
                        table {{
                            width: 100%;
                            border-collapse: collapse;
                            border-radius: 10px;
                            overflow: hidden; 
                            border: 1px solid #ddd;
                        }}
                        th {{
                            position: sticky;
                            top: 0;
                            background-color: #A5D6A7;
                            text-align: center;
                            font-weight: bold;
                            padding: 10px;
                            z-index: 1; 
                            color: black; 
                            border-bottom: 2px solid #ddd;
                        }}
                        td {{
                            text-align: center;
                            padding: 10px;
                            border: 1px solid #ddd;
                        }}
                    </style>
                    {df_filtered[
                        ["Smoking Habit", "Drinking Habit", "Dress Preference", "Preferred Ambience", 
                        "Transport Mode", "Marital Status", "People Under Charge", "Birth Year", 
                        "Interest", "Personality", "Religion", "Activity Level", 
                        "Favorite Color", "Weight (kg)", "Budget", "Height (cm)", 
                        "Preferred Payment Method", "User Preference"]
                    ].to_html(index=False)}
                </div>
                """, unsafe_allow_html=True
            )

            csv = df_filtered.to_csv(index=False)
            st.download_button(
                label="Download .csv",
                data=csv,
                file_name="filtered_data.csv",
                mime="text/csv"
            )
        else:
            st.write("Please select a mode to filter the data.")
