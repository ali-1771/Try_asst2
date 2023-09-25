import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

st.title('Data on Aviation Industry')
st.write('The dataset offers comprehensive insights into global airline operations, covering passenger demographics, flight details, crew information, and flight statuses, serving as a valuable resource for optimizing travel experiences and enhancing flight operations.')
@st.cache_data
def load_data(nrows):
    data = pd.read_csv('C:/Users/User/OneDrive/Desktop/MSBA 325/Airline Dataset.csv', nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data
data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache_data)")

if st.checkbox('Show raw data'):
    st.subheader('Airlines Dataset')
    st.write(data)


st.subheader('A pie chart for flight status distribution percentage')
pie = px.pie(data, names ='flight status')
st.plotly_chart(pie)


st.subheader("Bar chart for the most popular visited countries")
country = data["country name"].value_counts().head(10)
novisitors = [22104,6370,5424,4504,4081,2779,2358,2247,1643,1486]
barchart = go.Bar(x=country.index,y=novisitors,marker = dict(color='Blue'))
layout = go.Layout(
    xaxis=dict(title = 'Country'),
    yaxis = dict(title='Number of Visitors'))
fig2= go.Figure(data=[barchart], layout=layout)
st.plotly_chart(fig2)



st.subheader("A map for  nationality distribution of passengers")

nationalitycounts = data["nationality"].value_counts().reset_index()
nationalitycounts.columns = ["nationality" , "Number of Travelers"]



fig3 = px.choropleth(nationalitycounts, locations="nationality", locationmode="country names",
                   color="Number of Travelers", hover_name="nationality")
st.plotly_chart(fig3)



st.subheader("A boxplot for age distribution by gender")
fig6 = px.box(data, x='gender', y='age')
st.plotly_chart(fig6)








