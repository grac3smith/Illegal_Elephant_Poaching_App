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

st.markdown("<h1 style='text-align: center;'>Carcasses per Site</h1>", unsafe_allow_html=True)

years = mike['year'].drop_duplicates()
years_low, years_high = st.sidebar.select_slider('Please Select a Year or Range of Years', options = sorted(years), value=(2000, 2021)) #How to add an empty space as default??
filtered_data = mike[(mike['year'] >= years_low)&(mike['year'] <= years_high)]

tab1, tab2, tab3 = st.tabs(['Bar Chart', 'Line Chart', 'Samburu-Laikipia'])

with tab1:
    st.markdown('Below is a bar chart representing the number of elephant carcasses found per MIKE site. You can hover your mouse over the bars to see the number of carcasses.')
    st.markdown('Select the checkbox on the left to view the number of illegal elephant carcasses found.')
    st.markdown(" ")
    if button:
        domain = ['Africa', 'Asia']
        range_ = ['#cc3406', '#e37500']
        bar1 = alt.Chart(filtered_data, title=(f'Number of Illegal Carcasses found per Site: {years_low} - {years_high}')).transform_aggregate(
            sum_ill = 'sum(NumberOfIllegalCarcasses)',
            groupby=['MIKEsiteName', 'year', 'SubregionName', 'CountryName', 'UNRegion']
            ).mark_bar(
                ).encode(
                x = alt.X('sum(sum_ill):Q', title='Number of Illegal Carcasses'),
                y = alt.Y('MIKEsiteName', sort='-x', title=' '),
                color=alt.Color('UNRegion', title='Continent', scale=alt.Scale(domain=domain, range=range_)),
                tooltip=[alt.Tooltip('MIKEsiteName', title='MIKE Site'),
                    alt.Tooltip('SubregionName', title='Region'),
                    alt.Tooltip('CountryName', title='Country Name'),
                    alt.Tooltip('sum(sum_ill):Q', title='Number of Illegal Carcasses')]
            ).transform_filter(
                alt.datum.sum_ill > 26
                ).configure_title(
            fontSize=25)
        
        st.altair_chart(bar1, use_container_width=True) 

    else:
        domain = ['Africa', 'Asia']
        range_ = ['#cc3406', '#e37500']
        bar2 = alt.Chart(filtered_data, title=(f'Total Number of Carcasses found per Site: {years_low} - {years_high}')).transform_aggregate(
            sum_tot = 'sum(TotalNumberOfCarcasses)',
            groupby=['MIKEsiteName', 'year', 'SubregionName', 'CountryName', 'UNRegion']
            ).mark_bar(
            ).encode(
                x = alt.X('sum(sum_tot):Q', title='Total Number of Carcasses'),
                y = alt.Y('MIKEsiteName', sort='-x', title=' '),
                color=alt.Color('UNRegion', title='Continent', scale=alt.Scale(domain=domain, range=range_)),
                tooltip=[alt.Tooltip('MIKEsiteName', title='MIKE Site'),
                    alt.Tooltip('SubregionName', title='Region'),
                    alt.Tooltip('CountryName', title='Country Name'),
                    alt.Tooltip('sum(sum_tot):Q', title='Total Number of Carcasses')]
            ).transform_filter(
                alt.datum.sum_tot > 30
                ).configure_title(
            fontSize=25)
        
        st.altair_chart(bar2, use_container_width=True)
    st.markdown("Based on the bar chart above, we can see that the Samburu-Laikipia site is the biggest hotspot of illegal elephant poaching. This site accounts for ***12%*** of all illegal carcasses found by the MIKE program. Additonally, this site accounts for ***32%*** of all illegal carcasses found in Eastern Africa.")
    st.write("Click to the **Line Chart** tab to learn more.")

with tab2:
    st.markdown('Below is a line chart representing the number of elephant carcasses found per MIKE site.')
    st.markdown('Select the checkbox on the left to view the number of illegal elephant carcasses found.')
    st.markdown('The following MIKE sites have been preselected to show change over time in the top 3 sites with the most amount of carcasses found: Samburu-Laikipia, Garamba, and Niassa ')
    st.markdown(" ")

    options = mike['MIKEsiteName'].unique().tolist()
    selected_options = st.multiselect('Please Pick One or More MIKE Sites',options, default=['Samburu Laikipia', 'Garamba', 'Niassa'])
    filtered_df = mike[mike["MIKEsiteName"].isin(selected_options)]
    filtered_df2 = filtered_df[(filtered_df['year'] >= years_low)&(filtered_df['year'] <= years_high)]
    
    if button:
        line1 = alt.Chart(filtered_df, title='Number of Illegal Carcasses found per Year').mark_line(point=alt.OverlayMarkDef()).transform_aggregate(
            sum_ill = 'sum(NumberOfIllegalCarcasses)',
            groupby=['MIKEsiteName', 'year', 'SubregionName', 'CountryName', 'UNRegion']
            ).encode(
            x=alt.X('year:O', title='Year'),
            y=alt.Y('sum(sum_ill):Q', title='Number of Illegal Carcasses'),
            color=alt.Color('MIKEsiteName', title='MIKE Site', scale=alt.Scale(scheme= 'dark2')),
            tooltip=[alt.Tooltip('MIKEsiteName', title='MIKE Site'),
            alt.Tooltip('year:O', title='Year'),
            alt.Tooltip('SubregionName', title='Region'),
            alt.Tooltip('CountryName', title='Country Name'),
            alt.Tooltip('sum(sum_ill):Q', title='Number of Illegal Carcasses')]
            ).configure_title(
            fontSize=25)
    
        st.altair_chart(line1, use_container_width=True)

        st.write("The line chart above shows us that even out of the top 3 biggest hotspots for illegal elephant poaching, the Samburu-Laikipia site remains the most dangerous area for elephants.")
        st.markdown(" ")

        bar1 = alt.Chart(filtered_df2, title=(f'Number of Illegal Carcasses found: {years_low} - {years_high}')).transform_aggregate(
            sum_ill = 'sum(NumberOfIllegalCarcasses)',
            groupby=['MIKEsiteName', 'year', 'SubregionName', 'CountryName', 'UNRegion']
            ).mark_bar(
            ).encode(
                x=alt.X('sum(sum_ill):Q', title='Number of Illegal Carcasses'),
                y=alt.Y('MIKEsiteName', sort='-x', title=' '),
                color=alt.Color('MIKEsiteName', title='MIKE Site', scale=alt.Scale(scheme= 'dark2')),
            tooltip=[alt.Tooltip('MIKEsiteName', title='MIKE Site'),
                alt.Tooltip('SubregionName', title='Region'),
                alt.Tooltip('CountryName', title='Country Name'),
                alt.Tooltip('sum(sum_ill):Q', title='Number of Illegal Carcasses')]
            ).configure_title(
            fontSize=25)
        st.altair_chart(bar1, use_container_width=True)

    else:
        line2 = alt.Chart(filtered_df, title='Total Number of Carcasses found per Year').mark_line(point=alt.OverlayMarkDef()).transform_aggregate(
            sum_tot = 'sum(TotalNumberOfCarcasses)',
            groupby=['MIKEsiteName', 'year', 'SubregionName', 'CountryName', 'UNRegion']
            ).encode(
                x=alt.X('year:O', title='Year'),
                y=alt.Y('sum(sum_tot):Q', title='Total Number of Carcasses'),
                color=alt.Color('MIKEsiteName', title='MIKE Site', scale=alt.Scale(scheme= 'dark2')),
            tooltip=[alt.Tooltip('MIKEsiteName', title='MIKE Site'),
                alt.Tooltip('year:O', title='Year'),
                alt.Tooltip('SubregionName', title='Region'),
                alt.Tooltip('CountryName', title='Country Name'),
                alt.Tooltip('sum(sum_tot):Q', title='Total Number of Carcasses')]
            ).configure_title(
            fontSize=25)
        
        st.altair_chart(line2, use_container_width=True)

        st.write("The line chart above shows us that even out of the top 3 biggest hotspots for illegal elephant poaching, the Samburu-Laikipia site remains the most dangerous area for elephants.")
        st.markdown(" ")

        bar2 = alt.Chart(filtered_df2, title=(f'Total Number of Carcasses found: {years_low} - {years_high}')).transform_aggregate(
            sum_tot = 'sum(TotalNumberOfCarcasses)',
            groupby=['MIKEsiteName', 'year', 'SubregionName', 'CountryName', 'UNRegion']
            ).mark_bar(
            ).encode(
                x=alt.X('sum(sum_tot):Q', title='Total Number of Carcasses'),
                y=alt.Y('MIKEsiteName', sort='-x', title=' '),
                color=alt.Color('MIKEsiteName', title='MIKE Site', scale=alt.Scale(scheme= 'dark2')),
            tooltip=[alt.Tooltip('MIKEsiteName', title='MIKE Site'),
                alt.Tooltip('SubregionName', title='Region'),
                alt.Tooltip('CountryName', title='Country Name'),
                alt.Tooltip('sum(sum_tot):Q', title='Total Number of Carcasses')]
            ).configure_title(
            fontSize=25)
        st.altair_chart(bar2, use_container_width=True)
    
    st.write("Click through to the **Samburu-Laikipia** tab to learn more about MIKE's most complex site.")

with tab3:
    map = Image.open('images/MIKE-Map-2022.png')
    st.image(map)
    st.write("Above is a graph generated by **Save The Elephants**, a close affiliate of MIKE. The data used in this graph is not accessible to the public, therefore an image had to be used here. The graph demonstrates the percentage of illegal elephant killing that can be attributed to human-elephant conflict in the Samburu-Laikipia MIKE site.")
    st.write("The Samburu-Laikipia site contains national reserves, forest reserves, private ranches, community conservation areas, trust land, group ranches, farms, and urban settlements. ")
    st.write("The graph tells us that as of 2021, almost ***100%*** of the illegal carcasses found are a result of human-elephant conflict. While increased elephant conservation efforts seem to be effective at this site in recent years, it is clear that there is still a serious issue with human-elephant conflict in this area.")
    st.write("Human-elephant conflict entails a number of things such as crop raiding and elephants harming humans causing injury or death. This conflict is directly tied to elephant habitat loss as humans continue to take over their homes. While the ivory trade is certainly a large contributor to elephant endangerment, habitat loss is also a massive issue.")
    st.write("Furthermore, looking at the graph, it can also be observed that in 2012, elephant death due to conflict was at an all-time low at this site while the percentage of elephants poached was at an all-time high. Based on this, we can see that spike in illegal elephant poaching for ivory that we have seen throughout the application so far. In 2012, ivory was in very high demand, therefore the percentage of poached elephants was much higher and percentage of conflict killing was much lower because a higher ratio of elephants were killed for their tusks than conflict.")
