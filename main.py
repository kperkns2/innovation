
import streamlit as st
from streamlit_labelstudio import st_labelstudio

st.set_page_config(layout='wide')

# config = """
#       <View>
#         <View style="padding: 25px; box-shadow: 2px 2px 8px #AAA;">
#           <Image name="img" value="$image" width="100%" maxWidth="100%" brightnessControl="true" contrastControl="true" zoomControl="true" rotateControl="true"></Image>
#         </View>
#         <RectangleLabels name="tag" toName="img">
#           <Label value="Hello"></Label>
#           <Label value="Moon"></Label>
#         </RectangleLabels>
#       </View>
#     """


config = """<View>

  <Header value="Select label and start to click on image"/>
  <Image name="image" value="$image"/>

  <PolygonLabels name="label" toName="image"
                 strokeWidth="3" pointSize="small"
                 opacity="0.9">
    <Label value="Airplane" background="red"/>
    <Label value="Car" background="blue"/>
  </PolygonLabels>

</View>
"""    

# interfaces = [
#   "panel",
#   "update",
#   "controls",
#   "side-column",
#   "completions:menu",
#   "completions:add-new",
#   "completions:delete",
#   "predictions:menu",
# ],


interfaces = [
  "panel",
  "update",
  "controls",
  "side-column"
],

user = {
  'pk': 1,
  'firstName': "James",
  'lastName': "Dean"
},

user={}

task = {
  'completions': [],
  'predictions': [],
  'id': 1,
  'data': {
    'image': "https://htx-misc.s3.amazonaws.com/opensource/label-studio/examples/images/nick-owuor-astro-nic-visuals-wDifg5xc9Z4-unsplash.jpg"
  }
}

results_raw = st_labelstudio(config, interfaces, user, task)
st.write(results)
# if results_raw is not None:
#   areas = [v for k, v in results_raw['areas'].items()]

#   results = []
#   for a in areas:
#     results.append({'id':a['id'], 'x':a['x'], 'y':a['y'], 'width':a['width'], 'height':a['height'], 'label':a['results'][0]['value']['rectanglelabels'][0]})

#   st.table(results)