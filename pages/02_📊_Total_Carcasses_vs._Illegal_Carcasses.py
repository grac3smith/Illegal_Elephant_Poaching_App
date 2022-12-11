import streamlit as st
import pandas as pd
import altair as alt
st.set_page_config(layout="wide")

@st.cache(allow_output_mutation=True)
def load_data():
    mike = pd.read_excel('files/MIKE_Data.xlsx')
    return mike
mike = load_data()
mike['year'] = pd.to_datetime(mike['year'], format='%Y').dt.year

st.markdown("<h1 style='text-align: center;'>Total Carcasses vs. Illegal Carcasses</h1>", unsafe_allow_html=True)
st.write('Before discussing the visualizations from this dataset, it is important to note that the MIKE program is a site-based system. This means that the dataset does not provide a comprehensive representation of ***all*** elephant carcasses, but instead only provides data from ***specific*** MIKE sites within Africa and Asia.')
st.markdown(" ")

bar = alt.Chart(mike, title = 'Total Number of Elephant Carcasses Found vs. Number of Illegal Carcasses Found').mark_bar(size=30).encode(
    x=alt.X('year:O', axis=alt.Axis(grid=False)),
    y=alt.Y('sum(NumberOfIllegalCarcasses)', title='Number of Carcasses'),
    color=alt.condition(
    alt.datum.year == 2012,
    alt.value('darkred'),
    alt.value('#fa7373')),
    tooltip=[alt.Tooltip('sum(NumberOfIllegalCarcasses)', title='Number of Illegal Carcasses'),
            alt.Tooltip('year', title='Year')]
).properties(
    width=800, height=450
).interactive()

tick = alt.Chart(mike).mark_tick(
    thickness=10,
    size=30,
).encode(
    x=alt.X('year:O', axis=alt.Axis(grid=False)),
    y='sum(TotalNumberOfCarcasses)',
    color=alt.condition(
    alt.datum.year == 2012,
    alt.value('darkred'),
    alt.value('#858483')),
    tooltip=[alt.Tooltip('sum(TotalNumberOfCarcasses)', title='Total Number of Carcasses'),
            alt.Tooltip('year', title='Year')]
).properties(
    width=800, height=450
)

bar2= alt.Chart(mike).mark_bar(size=30, opacity=0.2, color='#ababab').encode(
    x=alt.X('year:O', title='Year', axis=alt.Axis(grid=False)),
    y='sum(TotalNumberOfCarcasses)',
    color=alt.condition(
    alt.datum.year == 2012,
    alt.value('darkred'),
    alt.value('#ababab')),
).properties(
    width=800, height=450
)

c =alt.layer(bar, tick, bar2).configure_title(
    fontSize=18
)
st.altair_chart(c, use_container_width=True)

st.write('Looking at the chart above, you will notice that the bar for the year 2012 is highlighted. In the year 2012, MIKE reported the highest number of total elephant carcasses with a total of ***2238*** carcasses, as well as illegal carcasses with a total of ***1087*** carcasses. Despite the international ivory trade ban put in place by CITES in 1990, illegal ivory trade was at an all-time high in 2011 and 2012. The total number of illegal carcasses found by MIKE sites in 2011 and 2022 accounts for ***19%*** of the total number of illegal carcasses found for the current duration of the MIKE program. This leads many to speculate whether the ban actually helped or caused more harm.')
st.markdown('However, the number of illegal carcasses appears to steadily decrease in the following years, which could be due to increased elephant conservation efforts and strict law enforcement.')
