'''
Collection of helper functions used both by app.py and individual pattern generators

'''

import streamlit as st


def sync_inputs(name, driving_input):
    ''' 
    Function to keep slider and number input for a measure syncronised.
    Arguments:
    -----
    name: name of the measure to be updated
    driving: define the input which is copied to the other
    '''

    input_types = ['slider', 'number_input']

    driven_inputs = [i for i in input_types if i != driving_input]

    for i in driven_inputs:
        st.session_state[name + '_' + i] = st.session_state[name + '_' +
                                                            driving_input]
    return
