"""Demo showing how to use style.py — copy the pattern into your own app.py."""
import streamlit as st
from style import apply_theme, hero, product_card

st.set_page_config(page_title="Blush Boutique", page_icon="👗", layout="wide")
apply_theme()

with st.sidebar:
    st.markdown("## 👗 Blush Boutique")
    st.caption("Style that speaks for you")
    st.divider()
    st.selectbox("Category", ["All", "Dresses", "Tops", "Bottoms", "Accessories"])
    st.slider("Price range (Rs)", 0, 20000, (1000, 8000))

home, shop, cart, orders, account = st.tabs(["Home", "Shop", "Cart", "Orders", "Account"])

with home:
    hero("New Season Arrivals", "Fresh pinks, soft fabrics and statement pieces, just in.")
    c1, c2, c3 = st.columns(3)
    c1.metric("Products", "248", "+12 this week")
    c2.metric("Happy customers", "3.4k", "+8%")
    c3.metric("Avg. rating", "4.8 ★")
    st.subheader("Trending now")
    cols = st.columns(4)
    items = [("Rose Wrap Dress", "Rs 4,500", "Dresses", "New", "👗"),
             ("Silk Blouse", "Rs 2,800", "Tops", "Hot", "👚"),
             ("Wide-Leg Trousers", "Rs 3,200", "Bottoms", "", "👖"),
             ("Leather Tote", "Rs 5,900", "Accessories", "Sale", "👜")]
    for col, (n, p, c, t, e) in zip(cols, items):
        with col:
            product_card(n, p, c, tag=t, emoji=e)
            st.button("Add to cart", key=f"h_{n}", width="stretch")

with shop:
    hero("Shop the Collection", "Filter by category and price from the sidebar.")
    st.text_input("Search products", placeholder="e.g. summer dress")
    cols = st.columns(3)
    for i, (n, p, c, t, e) in enumerate(items * 2):
        with cols[i % 3]:
            product_card(n, p, c, tag=t, emoji=e)

with cart:
    hero("Your Cart", "Review your picks before checkout.")
    st.dataframe({"Item": ["Rose Wrap Dress", "Silk Blouse"], "Qty": [1, 2], "Price": ["Rs 4,500", "Rs 5,600"]},
                 width="stretch", hide_index=True)
    st.metric("Total", "Rs 10,100")
    st.button("Proceed to checkout")

with orders:
    hero("Your Orders", "Track deliveries and past purchases.")
    with st.expander("Order #1042 · Shipped", expanded=True):
        st.write("Rose Wrap Dress × 1 — arriving Friday")
        st.progress(70)
    with st.expander("Order #1031 · Delivered"):
        st.write("Leather Tote × 1")

with account:
    hero("My Account", "Manage your profile and preferences.")
    with st.form("profile"):
        st.text_input("Full name")
        st.text_input("Email")
        st.text_area("Delivery address")
        st.form_submit_button("Save changes")
