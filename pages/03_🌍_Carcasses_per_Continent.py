import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image

st.set_page_config(layout="wide")

@st.cache(allow_output_mutation=True)
def load_data():
    mike = pd.read_excel('files/MIKE_Data.xlsx')
    return mike
mike = load_data()
mike['year'] = pd.to_datetime(mike['year'], format='%Y').dt.year

button = st.sidebar.checkbox('Show Illegal Carcasses Only')

years = mike['year'].drop_duplicates()
years_low, years_high = st.sidebar.select_slider('Please Select a Year or Range of Years', options = sorted(years), value=(2000, 2021)) #How to add an empty space as default??
filtered_data = mike[(mike['year'] >= years_low)&(mike['year'] <= years_high)]

st.markdown("<h1 style='text-align: center;'>Carcasses per Continent</h1>", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(['Bar Chart', 'Line Chart', 'Regions', 'Per Year'])

with tab1:
    st.markdown('Below is a bar chart demonstrating the number of elephant carcasses found by MIKE. You can hover your mouse over the red bars to see the number of carcasses.')
    st.markdown('On the left side of your screen is a checkbox that will allow you to view the number of illegal carcasses found in Africa and Asia.')
    st.markdown('There is also a slider with a range of years from 2000 to 2021. You can move this slider in any way you choose to view the counts of carcasses in Africa and Asia.')
    st.markdown(" ")

    if button:
        bar1 = alt.Chart(filtered_data, title=(f'Number of Illegal Carcasses found in Africa and Asia: {years_low} - {years_high}')).mark_bar(color='#bf0404').encode(
        x=alt.X('sum(NumberOfIllegalCarcasses)', title='Number of Illegal Carcasses'),
        y=alt.Y('UNRegion', sort='-x', title=' '),
        tooltip=[alt.Tooltip('UNRegion', title = 'Continent'),
        alt.Tooltip('sum(NumberOfIllegalCarcasses)', title='Number of Illegal Carcasses')]
        ).configure_title(
        fontSize=22)
        st.altair_chart(bar1, use_container_width=True)

    else:
        bar3 = alt.Chart(filtered_data, title=(f'Total Number of Carcasses found in Africa and Asia: {years_low} - {years_high}')).mark_bar(color='#bf0404').encode(
        x=alt.X('sum(TotalNumberOfCarcasses)', title='Total Number of Carcasses'),
        y=alt.Y('UNRegion', sort='-x', title=' '),
        tooltip=[alt.Tooltip('UNRegion', title = 'Continent'),
        alt.Tooltip('sum(TotalNumberOfCarcasses)', title='Total Number of Carcasses')]
        ).configure_title(
        fontSize=22)
        st.altair_chart(bar3, use_container_width=True)
    st.write('The chart above allows us to visualize the unequal proportions of elephant poaching in Africa versus Asia. There were ***10642*** illegal elephant carcasses found in MIKE sites through 2000 to 2021 in Africa. This means that ***94%*** of all illegal carcasses found come from Africa. This data clearly reflects the continuing problem of elephant poaching specifically in Africa.')
    st.write('Click through to the **Line Chart** tab to learn more.')

with tab2:
    st.markdown('Below is a line chart demonstrating the number of carcasses found in Africa and Asia from 2000 to 2021.')
    st.markdown('On the left side of your screen is a checkbox that will allow you to view the number of illegal carcasses found in Africa and Asia.')
    st.markdown(" ")

    if button:      
        line1 = alt.Chart(mike, title='Number of Illegal Carcasses found per Year in Africa and Asia').mark_line(point=alt.OverlayMarkDef()).encode(
        x=alt.X('year:O', title='Year', axis=alt.Axis(grid=True)),
        y=alt.Y('sum(NumberOfIllegalCarcasses)', title='Number of Illegal Carcasses'),
        color=alt.Color('UNRegion', title='Continent', scale=alt.Scale(scheme= 'dark2')),
        tooltip=[alt.Tooltip('UNRegion', title='Continent'),
            alt.Tooltip('sum(NumberOfIllegalCarcasses)', title='Number of Illegal Carcasses'),
            alt.Tooltip('year:O', title='Year')],
        ).configure_title(
        fontSize=25)
        st.altair_chart(line1, use_container_width=True)

    else:
        line2 = alt.Chart(mike, title='Total Number of Carcasses found per Year in Africa and Asia').mark_line(point=alt.OverlayMarkDef()).encode(
        x=alt.X('year:O', title='Year', axis=alt.Axis(grid=True)),
        y=alt.Y('sum(TotalNumberOfCarcasses)', title='Total Number of Carcasses'),
        color=alt.Color('UNRegion', title='Continent', scale=alt.Scale(scheme= 'dark2')),
        tooltip=[alt.Tooltip('UNRegion', title='Continent'),
            alt.Tooltip('sum(TotalNumberOfCarcasses)', title='Total Number of Carcasses'),
            alt.Tooltip('year:O', title='Year')]
        ).configure_title(
        fontSize=25)
        st.altair_chart(line2, use_container_width=True)
    st.write('The line chart above further demostrates the unequal proportions of elephant poaching in Africa versus Asia. The 2011 through 2012 spike in illegal elephant poaching is also further reflected here.')
    st.write("Click through to the **Regions** tab to learn more.")

with tab3:
    st.markdown('Below is a bar chart representing the number of elephant carcasses found per region. You can hover your mouse over the orange bars to see the number of carcasses.')
    st.markdown('The checkbox on the left allows you to view the number of illegal elephant carcasses found.')
    st.markdown('You can adjust the slider on the left side of your screen to view the number of carcasses found for a specific year or range of years.')
    
    if button:
        bar1 = alt.Chart(filtered_data, title=(f'Number of Illegal Carcasses found per Region: {years_low} - {years_high}')).mark_bar(color='#c26100').encode(
        x=alt.X('sum(NumberOfIllegalCarcasses)', title='Number of Illegal Carcasses'),
        y=alt.Y('SubregionName', sort='-x', title=' '),
        tooltip=[alt.Tooltip('SubregionName', title='Region'),
            alt.Tooltip('sum(NumberOfIllegalCarcasses)', title='Number of Illegal Carcasses')]
        ).configure_title(
        fontSize=22)
        st.altair_chart(bar1, use_container_width=True)
    else:
        bar3 = alt.Chart(filtered_data, title=(f'Total Number of Carcasses found per Region: {years_low} - {years_high}')).mark_bar(color='#c26100').encode(
        x=alt.X('sum(TotalNumberOfCarcasses)', title='Total Number of Carcasses'),
        y=alt.Y('SubregionName', sort='-x', title=' '),
        tooltip=[alt.Tooltip('SubregionName', title='Region'),
            alt.Tooltip('sum(TotalNumberOfCarcasses)', title='Total Number of Carcasses')]
        ).configure_title(
        fontSize=22)
        st.altair_chart(bar3, use_container_width=True)
    st.markdown('Looking at the chart above, after selecting the checkbox on the left, it can be concluded that Eastern, Central, and Southern Africa reported the largest amount of illegal carcasses.')
    st.write('Eastern Africa consists of countries such as **Kenya** and **United Republic of Tanzania**. Central Africa includes the **Democratic Republic of Congo**. Southern Africa includes **Mozambique**, **Zambia**, and **Zimbabwe**. These countries have the most prevalant illegal elephant poaching problems with their total number of illegal carcasses being ***7358*** which is ***65%*** of the total count of illegal carcasses found.')
    st.write("Click through to the **Per Year** tab to learn more.")

with tab4:
    st.markdown('Below is a line chart representing the number of elephant carcasses found per region per year.')
    st.markdown('The checkbox on the left allows you to view the number of illegal elephant carcasses found.')
    st.markdown(" ")

    if button:
        line1 = alt.Chart(mike, title='Number of Illegal Carcasses found per Region per Year').mark_line(point=alt.OverlayMarkDef()).encode(
        x=alt.X('year:O', title='Year'),
        y=alt.Y('sum(NumberOfIllegalCarcasses)', title='Number of Illegal Carcasses'),
        color=alt.Color('SubregionName', title='Region', scale=alt.Scale(scheme= 'dark2')),
        tooltip=[alt.Tooltip('SubregionName', title='Subregion Name'),
            alt.Tooltip('sum(NumberOfIllegalCarcasses)', title='Number of Illegal Carcasses'),
            alt.Tooltip('year:O', title='Year')]
        ).configure_title(
        fontSize=25)
        st.altair_chart(line1, use_container_width=True)

    else:
        line2 = alt.Chart(mike, title='Total Number of Carcasses found per Region per Year').mark_line(point=alt.OverlayMarkDef()).encode(
        x=alt.X('year:O', title='Year'),
        y=alt.Y('sum(TotalNumberOfCarcasses)', title='Total Number of Carcasses'),
        color=alt.Color('SubregionName', title='Region', scale=alt.Scale(scheme= 'dark2')),
        tooltip=[alt.Tooltip('SubregionName', title='Subregion Name'),
            alt.Tooltip('sum(NumberOfIllegalCarcasses)', title='Total Number of Carcasses'),
            alt.Tooltip('year:O', title='Year'),]
        ).configure_title(
        fontSize=25)
        st.altair_chart(line2, use_container_width=True)
    
    st.write("This line chart further reflects the huge spike in illegal elephant poaching around 2012, specifically in Eastern Africa.")
    st.markdown("The next page will go more in depth on specific countries within these regions.")
