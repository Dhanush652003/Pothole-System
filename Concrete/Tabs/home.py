import streamlit as st

def app():
    st.title("Concrete Strength Estimation System")
    st.image("./images/concrete.jpg")

    st.markdown(
    """<p style="font-size:20px;">
            Estimating concrete strength using machine learning involves leveraging various parameters such as the amount of cement, slag, water, and more to predict the final strength of the concrete mixture. Machine learning models play a crucial role in this process, offering a data-driven approach for optimizing concrete formulations.The amount of cement in the mix is a fundamental parameter that significantly influences concrete strength. Machine learning models can analyze historical data on various cement quantities and their corresponding concrete strengths to identify trends and correlations. By doing so, these models can help find the optimal cement amount for achieving the desired concrete strength.<br>Slag, a supplementary cementitious material, is often used to enhance concrete performance. Machine learning can assist in determining the most effective slag content to boost strength. It considers factors like slag type, proportion, and curing conditions to provide insights into its impact on strength.<br>Water content is another critical factor in concrete mix design. Machine learning can analyze historical data on water-to-cement ratios and their outcomes on concrete strength. This allows for precise adjustments to ensure the right level of workability and hydration without compromising strength.<br>In addition to these parameters, machine learning models can incorporate a wide range of other variables, such as aggregate types, curing methods, and environmental conditions, to refine the concrete strength prediction. By learning from historical data and adapting to various inputs, machine learning offers a powerful tool for optimizing concrete formulations and ensuring the desired strength is consistently achieved.
        </p>
    """, unsafe_allow_html=True)
