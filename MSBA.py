import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

url = "https://raw.githubusercontent.com/ali-1771/MSBA-325_ASST2/main/Airline%20Dataset.csv"
st.title('Data on Aviation Industry')
st.write('The dataset offers comprehensive insights into global airline operations, covering passenger demographics, flight details, crew information, and flight statuses, serving as a valuable resource for optimizing travel experiences and enhancing flight operations.')
@st.cache_data
def load_data(nrows):
    data = pd.read_csv(url, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data
data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache_data)")

if st.checkbox('Show raw data'):
    st.subheader('Airlines Dataset')
    st.write(data)

selectchart = st.sidebar.selectbox("Select a Visualization", ["Boxplot","Choropleth Map","Barchart","Pie Chart"])
if selectchart == "Boxplot":
    st.subheader("A boxplot for age distribution by gender")
    st.write("This boxplot shows the age distribution by gender. For a range of 0-100,the medians for both males and females are close enough with 46.5 and 46, respectively. We can also see that both q1 and q2 are close enough which means that there is no big shif in boxes for both genders.")
    age_range = st.slider('Select age range', 0, 100, (0, 100))
    filtered_data3 = data[(data['age'] >= age_range[0]) & (data['age'] <= age_range[1])]
    fig6 = px.box(filtered_data3, x='gender', y='age')
    st.plotly_chart(fig6)

elif selectchart == "Choropleth Map":
    st.subheader("A map for  nationality distribution of passengers")
    st.write("This cholopreth map shows the nationality distribution of genders where we can see that China is the leading country with around 1853 chinese passengers. The country you search for will change color basically.")
    nationality_filter = st.selectbox('Select a Nationality', data['nationality'].unique())
    filtered_data2 = data[data['nationality'] == nationality_filter]
    nationalitycounts = filtered_data2["nationality"].value_counts().reset_index()
    nationalitycounts.columns = ["nationality" , "Number of Travelers"]
    fig3 = px.choropleth(nationalitycounts, locations="nationality", locationmode="country names",
                   color="Number of Travelers", hover_name="nationality")
    st.plotly_chart(fig3)


elif selectchart == "Barchart":
    st.subheader("Bar chart for the most popular visited countries")
    st.write("This barchart shows the top 10 visited countries with the United States leading the list with 22,104 visitors. This visualization tells you about the popularity of these countries and may hint for busy airports in these countries which may cause these delays.")

    top_countries_count = st.slider('Select the number of top visited countries to display', 1, 10, 5)
    country = data["country name"].value_counts().head(top_countries_count)
    novisitors = [22104, 6370, 5424, 4504, 4081, 2779, 2358, 2247, 1643, 1486][:top_countries_count]

    barchart = go.Bar(x=country.index, y=novisitors, marker=dict(color='Blue'))
    layout = go.Layout(
        xaxis=dict(title='Country'),
        yaxis=dict(title='Number of Visitors'))
    fig2 = go.Figure(data=[barchart], layout=layout)
    st.plotly_chart(fig2)
elif selectchart == "Pie Chart":
    

    st.subheader('A pie chart for flight status distribution percentage')
    st.write("This pie chart shows the proportions of flights status, whether it is on time, cancelled, or delayed. Slightly equal proportions.")
    pie = px.pie(data, names ='flight status')
    st.plotly_chart(pie)








