#importing necessary libraries
import streamlit as st
from PIL import Image
import json
from pathlib import Path

# My name
name = "Georginah"

# Wishlist items and their image paths
wishlist_items = [
    {"name": "gift card", "image": "C:/Users/Georginah/Data Analytics Projects/wishlistapp/images/gift card.jpeg", "taken": False},
    {"name": "Massage", "image": "C:/Users/Georginah/Data Analytics Projects/wishlistapp/images/massage.jpeg", "taken": False},
    {"name": "Pilates", "image": "C:/Users/Georginah/Data Analytics Projects/wishlistapp/images/pilates.jpg", "taken": False},
    {"name": "Monitor", "image": "C:/Users/Georginah/Data Analytics Projects/wishlistapp/images/monitor.jpeg", "taken": False},
    {"name": "Shopping Spree", "image": "C:/Users/Georginah/Data Analytics Projects/wishlistapp/images/shopping.jpeg", "taken": False},
    {"name": "Beach Vacation", "image": "C:/Users/Georginah/Data Analytics Projects/wishlistapp/images/beach.jpeg", "taken": False},
    {"name": "Perfume", "image": "C:/Users/Georginah/Data Analytics Projects/wishlistapp/images/perfume.jpeg", "taken": False},
    {"name": "Skincare", "image": "C:/Users/Georginah/Data Analytics Projects/wishlistapp/images/skincare.jpeg", "taken": False},
]

# File path for JSON storage
file_path = Path('C:/Users/Georginah/Data Analytics Projects/wishlistapp/wishlist_items.json')

# Load items from file
def load_items():
    if file_path.exists():
        with file_path.open('r') as file:
            return json.load(file)
    else:
        return wishlist_items  # Use initial wishlist if no file exists

# Save items to file
def save_items(items):
    with file_path.open('w') as file:
        json.dump(items, file, indent=4)

# Initialize items
if 'wishlist_items' not in st.session_state:
    st.session_state.wishlist_items = load_items()

# Initialize session state for selected item and payment method
if 'selected_item_idx' not in st.session_state:
    st.session_state.selected_item_idx = None
if 'payment_method' not in st.session_state:
    st.session_state.payment_method = None

# Payment details
paypal = "georginahnjeri08@gmail.com"
mpesa = "0792301678"

# App title
st.title(f"{name}'s Wishlist 🎁")

# Splitting the items into two columns
cols = st.columns(2)

# Set fixed size for images
fixed_size = (300, 300)  # Width, Height

# Display items with images in a grid format
for idx, item in enumerate(st.session_state.wishlist_items):
    with cols[idx % 2]:
        # Open and resize the image
        image = Image.open(item['image'])
        image = image.resize(fixed_size)  # Resize image
        st.image(image, caption=item['name'], use_column_width=False)

        # Display item status
        if item['taken']:
            st.write(f"{item['name']} has already been taken.")
            # Option to reset the item status
            if st.button(f'Reset {item["name"]} status', key=f'reset_{idx}'):
                st.session_state.wishlist_items[idx]['taken'] = False
                save_items(st.session_state.wishlist_items)
                st.success(f"{item['name']} status has been reset.")
        else:
            st.write(f"{item['name']} is still available.")

            # Button to allow someone to get the item
            if st.button(f'Get Me This {item["name"]} 🤩', key=f'get_{idx}'):
                st.session_state.selected_item_idx = idx

# Show payment options if an item has been selected
if st.session_state.selected_item_idx is not None:
    selected_item = st.session_state.wishlist_items[st.session_state.selected_item_idx]
    st.write(f"Selected Item: {selected_item['name']}")
    
    st.session_state.payment_method = st.radio(
        label="Select Payment Method:",
        options=['PayPal', 'Mpesa']
    )

    if st.session_state.payment_method == 'PayPal':
        st.write("Send money via PayPal to the following email:")
        st.code(paypal)

    elif st.session_state.payment_method == 'Mpesa':
        st.write("Send money via M-Pesa to the following number 📱:")
        st.code(mpesa)

    # Update the item status to taken
    st.session_state.wishlist_items[st.session_state.selected_item_idx]['taken'] = True
    save_items(st.session_state.wishlist_items)

# Reset all items button for admin or reset purposes
if st.button('Reset All Items'):
    for item in st.session_state.wishlist_items:
        item['taken'] = False
    save_items(st.session_state.wishlist_items)
    st.success("All items have been reset to available.")

