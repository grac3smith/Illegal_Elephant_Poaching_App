import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image

st.set_page_config(layout="wide")

tab1, tab2 = st.tabs(['Introduction', 'History of Elephant Poaching'])

with tab1:
    image = Image.open('images/mike_banner_logo_long_2018.png')

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<h1 style='text-align: center;'>Data Analysis of the CITES MIKE Program Reports</h1>", unsafe_allow_html=True)
        
    with col2:
        st.image(image, caption="Monitoring the Illegal Killing of Elephants Logo")

    elephant = Image.open('images/elephant.jpg')
    elephant = elephant.resize((500,650),Image.ANTIALIAS)
    elephant.save(fp="images/newimage.png")


    col1, col2 = st.columns(2)
    with col1:
        st.image(elephant, caption = "Source: Nick Brandt, A Shadow Falls: ELEPHANT DRINKING, AMBOSELI 2007")

    with col2:
        st.markdown("<h2 style='text-align: center; color: grey;'>This application will take you through the continuing problem of elephant poaching in Africa and Asia through a series of visual representations and information.</h2>", unsafe_allow_html=True)

    st.subheader("About the Dataset")
    st.markdown('The dataset used in this analysis was obtained through The CITES Monitoring of Illegal Killing of Elephants (MIKE) Program which is designed to monitor trends in the illegal killing of elephants.')
    st.markdown('Total Number of Carcasses refers to elephants that died of both natural causes and illegal poaching.')
    st.markdown('Number of Illegal Carcasses refers to elephant that died as a result of illegal poaching only.')
    st.markdown('At the time this application was made, the only data available from CITES was from the year 2000 to 2021.')

with tab2:
    col1, col2 = st.columns(2)
    image2 = Image.open('images/tusks.jpg')
    image2 = image2.resize((500,365),Image.ANTIALIAS)
    image2.save(fp="images/tusks_re.jpg")
    image3=Image.open('images/elephant_tusk.jpg')
    with col1:
        st.image(image2)
        st.markdown(" ")
        st.markdown('Additionally, many countries still allow the domestic trade in ivory. CITES has continuously urged countries with domestic ivory markets to shut them down which prompted China to ban ivory trade. In 2017, China - a major contributor to the elephant poaching problem in Africa due to its ivory trade markets - finally implemented an ivory trade ban. The effects of this ban have been largely positive, however illegal trade is still a problem in China.')
    with col2:    
        st.markdown('For centuries, elephants have been killed mainly for the ivory that comes from their tusks. However, in recent years drastic steps have been taken to end the unnecessary killing of elephants. In 1990, The Convention on International Trade in Endangered Species of Wild Fauna and Flora (CITES) initiated a total ban on international ivory trade. Unfortunately, the ban did not help in reducing elephant poaching right away, in fact it steadily increased from 1990 to 2012 after the ban took effect. This is largely due to a significant increase in illegal elephant poaching for ivory.')
        st.image(image3)
    
    st.markdown(" ")
    st.write('Despite the previously mentioned international trade in ivory ban, it is estimated that since 1990 about ***30,000*** African elephants are killed each year by poachers out of a population of about ***400,000*** elephants in Africa. According to the CITES website, the International Union for Conservation of Nature (IUCN) estimated that the “population of African elephants declined by ***111,000*** over the past ten years”. However, in the past few years the number of elephants killed due to poaching has steadily declined thanks to increased law enforcement efforts, increased protection, and international action.')
    st.markdown('More in depth discussion will be featured throughout the application.')
