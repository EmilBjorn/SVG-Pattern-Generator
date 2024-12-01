"""
Streamlit app wrapper for svg_generator.py
"""
import streamlit as st

pg = st.navigation(
    [st.Page("Fading_Hexcells.py"),
     st.Page("Fading_Hexcells copy.py")],
    expanded=True)
st.set_page_config(page_title="SVG Pattern Generator",
                   page_icon=":diamond_shape_with_a_dot_inside:")

pg.run()
