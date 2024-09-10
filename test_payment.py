import streamlit as st

# Payment details
paypal = "georginahnjeri08@gmail.com"
mpesa = "0792301678"

# App title
st.title("Wishlist App")

# Display payment method selection
payment_method = st.radio(
    label="Select Payment Method:",
    options=['PayPal', 'Mpesa']
)

if payment_method == 'PayPal':
    st.write("Send money via PayPal to the following email:")
    st.code(paypal)

elif payment_method == 'Mpesa':
    st.write("Send money via M-Pesa to the following number 📱:")
    st.code(mpesa)

