import streamlit as st
st.write("Hello World!")

st.sidebar.write("Adjust image size here:")
img_size = st.sidebar.slider('Image Size', min_value=5, max_value=25, step=1)


import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
from bs4 import BeautifulSoup
import pathlib

#"""Add this in your streamlit app.py"""
GA_JS = """Here is some JavaScript"""

# Insert the script in the head tag of the static template inside your virtual environement
index_path = pathlib.Path(np.__file__).parent / "static" / "index.html"
#st.wrtie(str(index_path))
#soup = BeautifulSoup(index_path.read_text(), features="lxml")
# if not soup.find(id='custom-js'):
#     script_tag = soup.new_tag("script", id='custom-js')
#     script_tag.string = GA_JS
#     soup.head.append(script_tag)
#     index_path.write_text(str(soup))



# def new_img(im_file):
#     global im, fig, ax, coords, ix, iy, ax, cid
#     im = np.array(Image.open(im_file))
#     fig = plt.figure(figsize=[img_size,img_size])
#     ax = fig.add_subplot(111)
#     ax.imshow(im)
#     coords = []
#     def onclick(event):
#         global ix, iy, ax
#         ix, iy = event.xdata, event.ydata
#         global coords
#         coords.append((ix, iy))
#         point_list = ['StickerClose CableFar','StickerFar CableFar','StickerFar CableClose','StickerClose CableClose', 'Coaxial', 'Fiber']
#         ax.scatter(ix,iy, s=20, label=point_list[len(coords)-1])
#         plt.legend(bbox_to_anchor=(1.1, 1.0))
#         if len(coords) == 6:
#             fig.canvas.mpl_disconnect(cid)
#         return coords
#     cid = fig.canvas.mpl_connect('button_press_event', onclick)
#     #st.plotly_chart(fig)
#     st.write(fig)

# f = st.sidebar.file_uploader('File uploader')

#if f is not None:
#  new_img(f)