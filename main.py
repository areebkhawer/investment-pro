import streamlit as st
import yfinance as yf
from datetime import datetime

# 1. SETUP & SIDEBAR
st.set_page_config(page_title="InvestPro", layout="wide")

# Sidebar for navigation (matches the pro portfolio look)
st.sidebar.title("InvestPro Menu")
page = st.sidebar.radio("Go to:", ["Economic Info Hub", "Inflation Model Builder"])

# 2. PAGE 1: ECONOMIC INFO HUB
if page == "Economic Info Hub":
    st.title("Economic Info Hub")
    st.write("Real-time economic indicators and market insights")
    now = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    st.caption(f"Last updated: {now}")

    # Category Tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📊 All Indicators", "📈 Inflation", "📉 Growth", "💰 Monetary", "👥 Employment"
    ])

    with tab5: # Employment
        st.subheader("Employment")
        st.caption("Source: PBS")
        st.metric("Unemployment Rate", "6.2%", "-0.1%")
        st.progress(25)

    with tab4: # Monetary (Real-Time)
        st.subheader("Monetary Policy & Forex")
        try:
            forex = yf.Ticker("PKR=X")
            live_price = forex.history(period='1d')['Close'].iloc[-1]
            st.metric("USD / PKR (Live)", f"{live_price:.2f}", "Real-time")
        except:
            st.metric("USD / PKR", "278.50", "Offline")
        st.metric("Policy Rate (SBP)", "22%", "0%")

    with tab3: # Growth
        st.subheader("Growth")
        st.metric("GDP Growth Rate", "5.7%", "0.8%")
        st.progress(60)

    with tab1: # Summary
        c1, c2 = st.columns(2)
        c1.metric("CPI Inflation", "29.2%", "1.2%")
        c2.metric("GDP Growth", "5.7%", "0.8%")

    st.divider()
    st.header("Market Insights & Analysis")
    st.info("*AI Insight:* The current 22% rate is designed to anchor inflation expectations.")

# 3. PAGE 2: INFLATION MODEL BUILDER
elif page == "Inflation Model Builder":
    st.title("🧮 Inflation Model Builder")
    st.write("Project future inflation based on custom economic assumptions.")

    col1, col2 = st.columns(2)
    with col1:
        base_cpi = st.number_input("Current CPI (%)", value=29.2)
        money_supply = st.slider("Money Supply Growth (%)", 0, 50, 15)
    with col2:
        currency_dep = st.slider("Currency Depreciation (%)", 0, 50, 10)
        import_costs = st.slider("Global Oil Price Impact (%)", 0, 50, 5)

    # Simple Economic Formula (for demonstration)
    projected_inflation = base_cpi + (money_supply * 0.2) + (currency_dep * 0.3) + (import_costs * 0.1)

    st.divider()
    st.subheader("Model Result")
    st.metric("Projected Inflation Rate", f"{projected_inflation:.2f}%", f"{projected_inflation - base_cpi:.1f}% vs Base")
    
    if projected_inflation > 30:
        st.error("Warning: Model suggests High Inflationary pressure.")
    else:
        st.success("Model suggests Inflationary cooling.")