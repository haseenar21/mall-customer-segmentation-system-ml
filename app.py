import joblib
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("train.csv")
scaler = joblib.load('scaler.pkl')
model = joblib.load("model.pkl")

st.set_page_config("Mall Customer Segmentation", layout="wide")

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

.block-container {
    padding-top: 1rem;
    padding-bottom: 2rem;
}

div.stButton > button {
    width: 100%;
    height: 55px;
    font-size: 18px;
    font-weight: 700;
    border-radius: 10px;
}

.metric-card {
    padding: 1rem;
    border-radius: 12px;
    border: 1px solid #ddd;
    text-align: center;
    margin-bottom: 1rem;
}

.segment-card {
    padding: 1.5rem;
    border-radius: 15px;
    border: 1px solid #ddd;
    margin-top: 1rem;
}

.section-header {
    font-size: 24px;
    font-weight: bold;
    margin-top: 1rem;
    margin-bottom: 0.5rem;
}

</style>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col2:
    st.write("👥 Customers:200  🎯 Segments:5  🤖 Algorithm:K-Means")

st.markdown(
    "<h1 style='text-align: center;'>🛍️ Mall Customer Segmentation</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align: center;'>AI-powered customer segmentation and business insights</p>",
    unsafe_allow_html=True
)

with st.container(border=True):
    st.subheader("👤 Customer Information")

    age = st.number_input("Please Enter your Age : ",0,100)
    gender = st.radio("Gender", ["Male", "Female"])
    gender_encoded = 0 if gender == "Male" else 1
    Annual_Income = st.slider("Annual Income (k$) :",0 ,200) 
    score = st.slider("Spending Score : " ,1,100)

button = st.button("PREDICT", use_container_width=True)

if button :
    input_data = {
    "Gender": gender_encoded,
    "Age": age,
    "Annual Income (k$)": Annual_Income,
    "Spending Score (1-100)": score
    }
    input_df = pd.DataFrame([input_data])
    input_scaled = scaler.transform(input_df)
    prediction = model.predict(input_scaled)[0]

    segment_names = {
        0: "AverageCustomers", 
        1: "VIP Customers",
        2: "Potential Customers", 
        3: "Careful Customers", 
        4: "Budget Customers" 
    }

    if prediction == 0:
        st.markdown(f"""
            <div class="segment-card">
            <h1 style = "text-align: center;">Mainstream Shoppers</h1> 
            <h3 style="text-align: center;">Customer Value ⭐⭐⭐</h3>
            </div>
        """, unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("📊 Behavior")
            st.markdown("""
                - Consistent purchasing habits
                - Moderate engagement with marketing campaigns
                - Average spending patterns
            """)
        with col2:
            st.subheader("💼 Business Actions")
            st.markdown("""
                - Bundle offers to encourage more spending
                - Seasonal campaigns to maintain loyalty
                - Cross-selling opportunities to increase average order value
            """)
        st.info("💰 Revenue Impact : MEDIUM")
        
    elif prediction == 1:
        st.markdown(f"""
        <div class="segment-card">
        <h1 style = "text-align: center;">VIP Customers</h1> 
        <h3 style="text-align: center;">Customer Value ⭐⭐⭐⭐⭐</h3>
        </div>
        """, unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("📊 Behavior")
            st.markdown("""
                - High spending and frequent purchases
                - Strong brand loyalty
                - Active engagement with marketing campaigns
            """)
        with col2:
            st.subheader("💼 Business Actions")
            st.markdown("""
                - Exclusive offers and early access to new products
                - Personalized communication to maintain loyalty
                - VIP events and rewards programs to enhance customer experience
            """)
        st.success("💰 Revenue Impact : VERY HIGH")

    elif prediction == 2:
        st.markdown(f"""
        <div class="segment-card">
        <h1 style = "text-align: center;">Potential Customers</h1> 
        <h3 style="text-align: center;">Customer Value ⭐⭐⭐⭐</h3>
        </div>
        """, unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("📊 Behavior")
            st.markdown("""
                - Moderate spending with potential for growth
                - Occasional engagement with marketing campaigns
                - Interest in new products and promotions
            """)
        with col2:
            st.subheader("💼 Business Actions")
            st.markdown("""
                - Targeted promotions to encourage more frequent purchases
                - Personalized recommendations based on browsing behavior
                - Loyalty programs to incentivize repeat business
            """)
        st.success("💰 Revenue Impact : HIGH")

    elif prediction == 3:
        st.markdown(f"""
        <div class="segment-card">
        <h1 style = "text-align: center;">Careful Customers</h1> 
        <h3 style="text-align: center;">Customer Value ⭐⭐</h3>
        </div>
        """, unsafe_allow_html=True)

        col1, col2= st.columns(2)
        with col1:
            st.subheader("📊 Behavior")
            st.markdown("""
                - Price-sensitive with cautious spending habits
                - Limited engagement with marketing campaigns
                - Focus on value and discounts
            """)
        with col2:
            st.subheader("💼 Business Actions")
            st.markdown("""
                - Competitive pricing and discount offers to attract attention
                - Clear communication of value propositions to address price concerns
                - Loyalty programs that emphasize savings and rewards
            """)
        st.warning("💰 Revenue Impact : LOW")


    elif prediction == 4:
        st.markdown(f"""
        <div class="segment-card">
        <h1 style = "text-align: center;">Budget Customers</h1> 
        <h3 style="text-align: center;">Customer Value ⭐</h3>
        </div>
        """, unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("📊 Behavior")
            st.markdown("""
                - Low spending with infrequent purchases
                - Minimal engagement with marketing campaigns
                - Strong focus on discounts and promotions
            """)
        with col2:
            st.subheader("💼 Business Actions")
            st.markdown("""
                - Aggressive discounting and clearance sales to attract attention
                - Targeted promotions that emphasize affordability and value
                - Loyalty programs that offer significant savings and rewards
            """)

        st.warning("💰 Revenue Impact : VERY LOW")
    st.info("Note: The above predictions are based on the customer's behavior and spending patterns. Business actions are recommended strategies to enhance customer engagement and increase revenue based on the predicted segment.")

    st.subheader("📍 Customer Position Analysis")

    fig, ax = plt.subplots(figsize=(4,2))

    ax.scatter(
        df["Annual Income (k$)"],
        df["Spending Score (1-100)"],
        alpha=0.4,
        label="Existing Customers"
    )

    ax.scatter(
        Annual_Income,
        score,
        s=200,
        marker="*",
        label="You"
    )

    ax.set_xlabel("Annual Income (k$)")
    ax.set_ylabel("Spending Score")
    ax.set_title("Customer Position in Dataset")
    ax.legend()

    st.pyplot(fig)

    cluster_counts = pd.Series(model.labels_).value_counts().sort_index()
    st.subheader("📊 Segment Distribution")
    st.bar_chart(cluster_counts)