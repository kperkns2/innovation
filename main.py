
import streamlit as st
from streamlit_labelstudio import st_labelstudio

st.set_page_config(layout='wide')


def polygon_segmentation():
  config = """<View>
    <Header value="Select label and start to click on image"/>
    <Image name="image" value="$image" zoomControl="true" rotateControl="true"/>

    <PolygonLabels name="label" toName="image"
                  strokeWidth="3" pointSize="small"
                  opacity="0.9">
      <Label value="Normal" background="green"/>
      <Label value="Defective" background="red"/>
    </PolygonLabels>
  </View>
  """    
  interfaces = [
    "panel",
    "update",
    "controls",
    "side-column"
  ],
  user={}
  results_raw = st_labelstudio(config, interfaces, user, task)
  if results_raw is not None:
    areas = [v for k, v in results_raw['areas'].items()]
    results = []
    for a in areas:
      results.append({'id':a['id'], 'x':[p['x']  for p in  a['points']], 'y':[p['y']  for p in  a['points']],  'label':a['results'][0]['value']['polygonlabels'][0]})
    st.table(results)



def bounding_box():
  config = """
        <View>
          <View style="padding: 25px; box-shadow: 2px 2px 8px #AAA;">
            <Image name="img" value="$image" width="100%" maxWidth="100%" brightnessControl="true" contrastControl="true" zoomControl="true" rotateControl="true"></Image>
          </View>
          <RectangleLabels name="tag" toName="img">
            <Label value="Hello"></Label>
            <Label value="Moon"></Label>
          </RectangleLabels>
        </View>
      """

  interfaces = [
    "panel",
    "update",
    "controls",
    "side-column",
    #"completions:menu",
    #"completions:add-new",
    #"completions:delete",
    #"predictions:menu",
  ],

  user = {
    #'pk': 1,
    #'firstName': "James",
    #'lastName': "Dean"
  },

  task = {
    'completions': [],
    'predictions': [],
    'id': 1,
    'data': {
      'image': "https://www.lenovo.com/medias/lenovo-data-center-server-rack-thinksystem-sr665-subseries-gallery-4.jpg?context=bWFzdGVyfHJvb3R8MTQyMzQ5fGltYWdlL2pwZWd8aDA3L2gwNi8xMDg3OTYxNDY0ODM1MC5qcGd8NTEwZDAxNWI1ODYyOGNkZDE1OTEzZGNkNDI2YTk2OTJkNWY4NzNjYzMwMjc0YTg3MDEwNmE0ZDM3YWY1MzJhZg"
    }
  }

  results_raw = st_labelstudio(config, interfaces, user, task)

  if results_raw is not None:
    areas = [v for k, v in results_raw['areas'].items()]

    results = []
    for a in areas:
      results.append({'id':a['id'], 'x':a['x'], 'y':a['y'], 'width':a['width'], 'height':a['height'], 'label':a['results'][0]['value']['rectanglelabels'][0]})

    st.table(results)  

task = {
  'completions': [],
  'predictions': [],
  'id': 1,
  'data': {
    'image': "https://www.lenovo.com/medias/lenovo-data-center-server-rack-thinksystem-sr665-subseries-gallery-4.jpg?context=bWFzdGVyfHJvb3R8MTQyMzQ5fGltYWdlL2pwZWd8aDA3L2gwNi8xMDg3OTYxNDY0ODM1MC5qcGd8NTEwZDAxNWI1ODYyOGNkZDE1OTEzZGNkNDI2YTk2OTJkNWY4NzNjYzMwMjc0YTg3MDEwNmE0ZDM3YWY1MzJhZg"
  }
}



if st.sidebar.radio("Label Type", ["Bounding Box", "Polygon Segmentation"]) == "Bounding Box":
  bounding_box()
else:
  polygon_segmentation()