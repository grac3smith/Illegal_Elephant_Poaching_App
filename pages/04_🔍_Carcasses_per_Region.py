import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image

st.set_page_config(layout="wide")

@st.cache(allow_output_mutation=True)
def load_data():
    mike = pd.read_excel('files/MIKE_Update.xlsx')
    return mike
mike = load_data()
mike['year'] = pd.to_datetime(mike['year'], format='%Y').dt.year

@st.cache(allow_output_mutation=True)
def load_data():
    africa = pd.read_excel('files/africa.xlsx')
    return africa
africa = load_data()
africa['year'] = pd.to_datetime(africa['year'], format='%Y').dt.year

@st.cache(allow_output_mutation=True)
def load_data():
    asia=pd.read_excel('files/asia.xlsx')
    return asia
asia = load_data()
asia['year'] = pd.to_datetime(asia['year'], format='%Y').dt.year

@st.cache(allow_output_mutation=True)
def load_data():
    kenya=pd.read_excel('files/kenya.xlsx')
    return kenya
kenya = load_data()
kenya['year'] = pd.to_datetime(kenya['year'], format='%Y').dt.year

@st.cache(allow_output_mutation=True)
def load_data():
    india=pd.read_excel('files/india.xlsx')
    return india
india = load_data()
india['year'] = pd.to_datetime(india['year'], format='%Y').dt.year

button = st.sidebar.checkbox('Show Illegal Carcasses Only')
years = mike['year'].drop_duplicates()
years_low, years_high = st.sidebar.select_slider('Please Select a Year or Range of Years', options = sorted(years), value=(2000, 2021)) #How to add an empty space as default??
filtered_data = mike[(mike['year'] >= years_low)&(mike['year'] <= years_high)]
filtered_data2 = africa[(africa['year'] >= years_low)&(africa['year'] <= years_high)]
filtered_data3 = asia[(asia['year'] >= years_low)&(asia['year'] <= years_high)]


st.markdown("<h1 style='text-align: center;'>Carcasses per Region</h1>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(['African Countries', 'Asian Countries', 'Line Chart'])

with tab1:
    st.markdown('Below is a bar chart representing the number of elephant carcasses found per country in Africa. You can hover your mouse over the red bars to see the number of carcasses.')
    st.markdown('Select the checkbox on the left to view the number of illegal elephant carcasses found.')
    st.markdown(" ")

    if button:
        bar1 = alt.Chart(filtered_data2, title=(f'Number of Illegal Carcasses found per Country in Africa: {years_low} - {years_high}')).transform_aggregate(
        sum_ill = 'sum(NumberOfIllegalCarcasses)',
        groupby=['CountryName', 'year']
        ).mark_bar(color='#cc3406').encode(
        x = alt.X('sum(sum_ill):Q', title='Number of Illegal Carcasses'),
        y = alt.Y('CountryName', sort='-x', title=' '),
        tooltip=[alt.Tooltip('CountryName', title='Country Name'),
            alt.Tooltip('sum(sum_ill):Q', title='Number of Illegal Carcasses')]
        ).transform_filter(
        alt.datum.sum_ill > 22
        ).configure_title(
        fontSize=18)
        st.altair_chart(bar1, use_container_width=True)

        st.markdown('Looking at the bar chart above, it can be cocnluded that Kenya is the biggest hotspot in terms of illegal elephant poaching in Africa. Observe the line chart below and see how the numbers have changed over time.')
        st.write('The line chart shows a peak of ***318*** illegal carcasses found in 2012. At this time, China had not yet implemented the ivory ban, so demand for ivory was growing in the region in 2012. Because of the growing demand for ivory in China at this time, many poachers killed elephants in Africa - which is home to heavily poached African elephants - then brought the ivory to Asia for profit. As of 2022, there are about ***400,000*** African elephants remaining.')
        st.write("According to the International Union for the Conservation of Nature (IUCN), the African bush elephant species is currently ***endangered*** and the African forest elephant is ***critically endangered***.")
        st.markdown(" ")

        domain = ['Kenya']
        range_ = ['#cc3406']

        line1 = alt.Chart(kenya, title='Number of Illegal Carcasses found per Year').mark_line(point=alt.OverlayMarkDef()).encode(
        x=alt.X('year:O', title='Year'),
        y=alt.Y('sum(NumberOfIllegalCarcasses)', title='Number of Illegal Carcasses'),
        color=alt.Color('CountryName', title='Country', scale=alt.Scale(domain=domain, range=range_)),
        tooltip=[alt.Tooltip('CountryName', title='Country Name'),
            alt.Tooltip('sum(NumberOfIllegalCarcasses)', title='Number of Illegal Carcasses'),
            alt.Tooltip('year:O', title='Year')]
        ).configure_title(
        fontSize=25)
        st.altair_chart(line1, use_container_width=True)

        st.markdown('Thankfully, the surge in elephant poaching in Kenya and other African countries has been in a steady decline due to enhanced surveillance, anti-poaching units, and updated legislation. Illegal elephant poachers now face serious prison time and heavy fines if convicted of harvesting elephant ivory.')
        st.write("Click through to the **Asian Countries** tab to learn more.")

    else:    
        bar4 = alt.Chart(filtered_data2, title=(f'Total Number of Carcasses found per Country in Africa: {years_low} - {years_high}')).transform_aggregate(
        sum_tot = 'sum(TotalNumberOfCarcasses)',
        groupby=['CountryName', 'year']
        ).mark_bar(
            color='#cc3406'
            ).encode(
            x = alt.X('sum(sum_tot):Q', title='Total Number of Carcasses'),
            y = alt.Y('CountryName', sort='-x', title=' '),
            tooltip=[alt.Tooltip('CountryName', title='Country Name'),
                alt.Tooltip('sum(sum_tot):Q', title='Total Number of Carcasses')]
        ).transform_filter(
            alt.datum.sum_tot > 22
            ).configure_title(
        fontSize=18)
        st.altair_chart(bar4, use_container_width=True) 

        st.markdown('Looking at the bar chart above, it can be cocnluded that Kenya is the biggest hotspot in terms of illegal elephant poaching in Africa. Observe the line chart below and see how the numbers have changed over time.')
        st.write('The line chart shows a peak of ***318*** illegal carcasses found in 2012. At this time, China had not yet implemented the invory ban, so demand for ivory was growing in the region in 2012. Because of the growing demand for ivory in China at this time, many poachers killed elephants in Africa - which is home to heavily poached African elephants - then brought the ivory to Asia for profit. As of 2022, there are about ***400,000*** African elephants remaining.')
        st.write("According to the International Union for the Conservation of Nature (IUCN), the African bush elephant species is currently ***endangered*** and the African forest elephant is ***critically endangered***.")
        st.markdown(" ")

        domain = ['Kenya']
        range_ = ['#cc3406']

        line2 = alt.Chart(kenya, title='Total Number of Carcasses found per Year').mark_line(point=alt.OverlayMarkDef()).encode(
        x=alt.X('year:O', title='Year'),
        y=alt.Y('sum(TotalNumberOfCarcasses)', title='Total Number of Carcasses'),
        color=alt.Color('CountryName', title='Country', scale=alt.Scale(domain=domain, range=range_)),
        tooltip=[alt.Tooltip('CountryName', title='Country Name'),
            alt.Tooltip('sum(TotalNumberOfCarcasses)', title='Total Number of Carcasses'),
            alt.Tooltip('year:O', title='Year')]
        ).configure_title(
        fontSize=25)
        st.altair_chart(line2, use_container_width=True)

        st.markdown('Thankfully, the surge in elephant poaching in Kenya and other African countries has been in a steady decline due to enhanced surveillance, anti-poaching units, and updated legislation. Illegal elephant poachers now face serious prison time and heavy fines if convicted of harvesting elephant ivory.')
        st.write("Click through to the **Asian Countries** tab to learn more.")

with tab2:
    st.markdown('Below is a bar chart representing the number of elephant carcasses found per country in Asia.')
    st.markdown('Select the checkbox on the left to view the number of illegal elephant caracasses found.')
    st.markdown(" ")

    if button:
        bar2 = alt.Chart(filtered_data3, title=(f'Number of Illegal Carcasses found per Country in Asia: {years_low} - {years_high}')).transform_aggregate(
        sum_ill = 'sum(NumberOfIllegalCarcasses)',
        groupby=['CountryName', 'year']
        ).mark_bar(color='#e37500').encode(
        x = alt.X('sum(sum_ill):Q', title='Number of Illegal Carcasses'),
        y = alt.Y('CountryName', sort='-x', title=' '),
        tooltip=[alt.Tooltip('CountryName', title='Country Name'),
            alt.Tooltip('sum(sum_ill):Q', title='Number of Illegal Carcasses')]
        ).transform_filter(
        alt.datum.sum_ill > 0
        ).configure_title(
        fontSize=18)

        st.altair_chart(bar2, use_container_width=True) 

        st.write("Looking at the bar chart above, it can be concluded that India is Asia's biggest hotspot in terms of illegal elephant poaching. While MIKE has only reported ***494*** illegal elephant carcasses from 2000 to 2021 in India, these numbers still don't fully encapsulate the number of Asian elephants poached in Asia. The line chart below does reflect an overall decrease in elephant poaching since 2013.")
        st.write("While both male and female African elephants grow tusks, only male Asian elephants have tusks. The poaching problem in Asia is causing a disproportional amount of male elephants to female. However, females are also killed by poachers for their meat and skin. As of 2022, it is estimated that only about ***40,000*** Asian elephants remain.")
        st.write("According to the IUCN, Asian elephants are currently ***endangered***.")
        st.markdown(" ")

        domain = ['India']
        range_ = ['#e37500']

        line1 = alt.Chart(india, title='Number of Illegal Carcasses found per Year').mark_line(point=alt.OverlayMarkDef()).encode(
        x=alt.X('year:O', title='Year'),
        y=alt.Y('sum(NumberOfIllegalCarcasses)', title='Number of Illegal Carcasses'),
        color=alt.Color('CountryName', title='Country', scale=alt.Scale(domain=domain, range=range_)),
        tooltip=[alt.Tooltip('CountryName', title='Country Name'),
            alt.Tooltip('sum(NumberOfIllegalCarcasses)', title='Number of Illegal Carcasses'),
            alt.Tooltip('year:O', title='Year')]
        ).configure_title(
        fontSize=25)
        st.altair_chart(line1, use_container_width=True)

    else:
        bar4 = alt.Chart(filtered_data3, title=(f'Total Number of Carcasses found per Country in Asia: {years_low} - {years_high}')).transform_aggregate(
        sum_tot = 'sum(TotalNumberOfCarcasses)',
        groupby=['CountryName', 'year']
        ).mark_bar(
            color='#e37500'
            ).encode(
            x = alt.X('sum(sum_tot):Q', title='Total Number of Carcasses'),
            y = alt.Y('CountryName', sort='-x', title=' '),
            tooltip=[alt.Tooltip('CountryName', title='Country Name'),
                alt.Tooltip('sum(sum_tot):Q', title='Total Number of Carcasses')]
        ).transform_filter(
            alt.datum.sum_tot > 0
            ).configure_title(
        fontSize=18)

        st.altair_chart(bar4, use_container_width=True) 

        st.write("Looking at the bar chart above, it can be concluded that India is Asia's biggest hotspot in terms of illegal elephant poaching. While MIKE has only reported ***494*** illegal elephant carcasses from 2000 to 2021 in India, these numbers still don't fully encapsulate the number of Asian elephants poached in Asia. The line chart below does reflect an overall decrease in elephant poaching since 2013.")
        st.write("While both male and female African elephants grow tusks, only male Asian elephants have tusks. The poaching problem in Asia is causing a disproportional amount of male elephants to female. However, females are also killed by poachers for their meat and skin. As of 2022, it is estimated that only about ***40,000*** Asian elephants remain.")
        st.write("According to the IUCN, Asian elephants are currently ***endangered***.")
        st.markdown(" ")

        domain = ['India']
        range_ = ['#e37500']

        line2 = alt.Chart(india, title='Total Number of Carcasses found per Year').mark_line(point=alt.OverlayMarkDef()).encode(
        x=alt.X('year:O', title='Year'),
        y=alt.Y('sum(TotalNumberOfCarcasses)', title='Total Number of Carcasses'),
        color=alt.Color('CountryName', title='Country', scale=alt.Scale(domain=domain, range=range_)),
        tooltip=[alt.Tooltip('CountryName', title='Country Name'),
            alt.Tooltip('sum(TotalNumberOfCarcasses)', title='Total Number of Carcasses'),
            alt.Tooltip('year:O', title='Year')]
        ).configure_title(
        fontSize=25)
        st.altair_chart(line2, use_container_width=True)
    
    st.write("Click through to the **Line Chart** tab to learn more.")

with tab3:
    st.markdown('Select the checkbox on the left to view the number of illegal elephant carcasses found.')
    st.markdown('Below is a line chart that shows the number of carcasses found per selected country per year. You can use the selectbox below to add and remove any number of countries.')
    st.markdown('Kenya, the Democratic Republic of Congo, the United Republic of Tanzania, and Mozambique have all been preselected in the selectbox to visualize the top 4 countries with the most amount of carcasses found.')
    st.markdown(" ")

    options = mike['CountryName'].unique().tolist()
    selected_options = st.multiselect('Please Pick One or More Countries',options, default=['Kenya', 'Congo, Democratic Republic of the', 'Tanzania, United Republic of', 'Mozambique'])
    filtered_df = mike[mike["CountryName"].isin(selected_options)]
    filtered_df2 = filtered_df[(filtered_df['year'] >= years_low)&(filtered_df['year'] <= years_high)]
    
    if button:
        line1 = alt.Chart(filtered_df, title='Number of Illegal Carcasses found per Year').mark_line(point=alt.OverlayMarkDef()).encode(
        x=alt.X('year:O', title='Year'),
        y=alt.Y('sum(NumberOfIllegalCarcasses)', title='Number of Illegal Carcasses'),
        color=alt.Color('CountryName', title='Country', scale=alt.Scale(scheme= 'dark2')),
        tooltip=[alt.Tooltip('CountryName', title='Country Name'),
            alt.Tooltip('sum(NumberOfIllegalCarcasses)', title='Number of Illegal Carcasses'),
            alt.Tooltip('year:O', title='Year')]
        ).configure_title(
        fontSize=25)
        st.altair_chart(line1, use_container_width=True)

        st.write('The line chart above and bar chart below will allow you to research elephant poaching in specific countries of your choice. With the preselected 4 countries, it can be noted that since around 2012, illegal elephant carcasses have been steadily decreasing due to a major increase in conservation efforts.')
        st.write('It is estimated that a total of about ***415,000*** elephants remain worldwide.')
        st.markdown(" ")

        bar1 = alt.Chart(filtered_df2, title=(f'Number of Illegal Carcasses found: {years_low} - {years_high}')).mark_bar(color='#c26100').encode(
        x=alt.X('sum(NumberOfIllegalCarcasses)', title='Number of Illegal Carcasses'),
        y=alt.Y('CountryName', sort='-x', title=' '),
        color=alt.Color('CountryName', title='Country', scale=alt.Scale(scheme= 'dark2')),
        tooltip=[alt.Tooltip('CountryName', title='Country Name'),
            alt.Tooltip('sum(NumberOfIllegalCarcasses)', title='Number of Illegal Carcasses')]
        ).configure_title(
        fontSize=25)
        st.altair_chart(bar1, use_container_width=True)

    else:
        line2 = alt.Chart(filtered_df, title='Total Number of Carcasses found per Year').mark_line(point=alt.OverlayMarkDef()).encode(
        x=alt.X('year:O', title='Year'),
        y=alt.Y('sum(TotalNumberOfCarcasses)', title='Total Number of Carcasses'),
        color=alt.Color('CountryName', title='Country', scale=alt.Scale(scheme= 'dark2')),
        tooltip=[alt.Tooltip('CountryName', title='Country Name'),
            alt.Tooltip('sum(TotalNumberOfCarcasses)', title='Total Number of Carcasses'),
            alt.Tooltip('year:O', title='Year')]
        ).configure_title(
        fontSize=25)
        st.altair_chart(line2, use_container_width=True)

        st.write('The line chart above and bar chart below will allow you to research elephant poaching in specific countries of your choice. With the preselected 4 countries, it can be noted that since around 2012, illegal elephant carcasses have been steadily decreasing due to a major increase in conservation efforts.')
        st.write('It is estimated that a total of about ***415,000*** elephants remain worldwide.')
        st.markdown(" ")

        bar2 = alt.Chart(filtered_df2, title=(f'Total Number of Carcasses found: {years_low} - {years_high}')).mark_bar(color='#c26100').encode(
        x=alt.X('sum(TotalNumberOfCarcasses)', title='Total Number of Carcasses'),
        y=alt.Y('CountryName', sort='-x', title=' '),
        color=alt.Color('CountryName', title='Country', scale=alt.Scale(scheme= 'dark2')),
        tooltip=[alt.Tooltip('CountryName', title='Country Name'),
            alt.Tooltip('sum(TotalNumberOfCarcasses)', title='Total Number of Carcasses')]
        ).configure_title(
        fontSize=25)
        st.altair_chart(bar2, use_container_width=True)
    
    st.write("The next page will go more in depth on specific MIKE sites.")
