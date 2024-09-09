#importing neccessary libraries
import streamlit as st
from PIL import Image

#my name
name = "Georginah"

#wishlist items and their image paths
wishlist_items = [
    {"name": "gift card", "image": "C:/Users/Georginah/Data Analytics Projects/wishlistapp/images/gift card.jpeg"},
    {"name": "Massage", "image": "C:/Users/Georginah/Data Analytics Projects/wishlistapp/images/massage.jpeg"},
    {"name": "Pilates", "image": "C:/Users/Georginah/Data Analytics Projects/wishlistapp/images/pilates.jpg"},
    {"name": "Monitor", "image": "C:/Users/Georginah/Data Analytics Projects/wishlistapp/images/monitor.jpeg"},
    {"name": "Shopping Spree", "image": "C:/Users/Georginah/Data Analytics Projects/wishlistapp/images/shopping.jpeg"},
    {"name": "Beach Vacation", "image": "C:/Users/Georginah/Data Analytics Projects/wishlistapp/images/beach.jpeg"},
    {"name": "Perfume", "image": "C:/Users/Georginah/Data Analytics Projects/wishlistapp/images/perfume.jpeg"},
    {"name": "skincare", "image": "C:/Users/Georginah/Data Analytics Projects/wishlistapp/images/skincare.jpeg"},
]

#payment details
paypal = "georginahnjeri08@gmail.com"  
mpesa = "0792301678"

#app title
st.title(f"{name}'s Wishlist 🎁")

#splitting the items into two columns
cols = st.columns(2)

#set fixed width for images
image_width = 300

#display items with images in a grid format
for idx, item in enumerate(wishlist_items):
    with cols[idx % 2]:
        # Display the image
        image = Image.open(item['image'])
        st.image(image, caption=item['name'], use_column_width=True)
        st.write(item['name'])

        # Button to allow someone to get the item
        if st.button(f'Get Me This {item["name"]} 🤩', key=f'get_{idx}'):
            st.success(f'Thank you for selecting to get me a {item["name"]} 🤩!')
            
            # Payment options
            st.write("Choose a payment method 💳:")

            # Payment selection dropdown
            payment_method = st.radio(
                label="Select Payment Method:",
                options=['PayPal', 'Send Money (M-Pesa)'],
                key=f'payment_method_{idx}'
            )

            if payment_method == 'PayPal':
                # Display PayPal email for manual payment
                st.write("Send money via PayPal to the following email:")
                st.code(paypal)

            elif payment_method == 'Send Money (M-Pesa)':
                # Ensure the M-Pesa number is visible
                st.write("Send money via M-Pesa to the following number 📱:")
                st.code(mpesa)