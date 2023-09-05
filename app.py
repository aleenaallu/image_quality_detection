from flask import Flask ,request,render_template
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
from PIL import Image

app = Flask(__name__)
model = keras.models.load_model('model.h5')

@app.route('/')
def index():
    return render_template("imgindex.html", name="Tariq")


@app.route('predication',method=['POST'])
def predication():
    img=request.files['img']
    img.save('img.jpg')
    img=image.load_img('img.jpg',target_size=(300,300))
    x=image.img_to_array(img)/255
    resized_img_np=np.expand_dims(x,axis=0)
    predication=model.predict(resized_img_np)
    output={'def':0,'oky':1}
    value=np.argmax(predication)
    lb=list(output.keys())
    pre=lb[value]
    return render_template('prediction.html',data=pre)

if __name__=='__main__':
    app.run(port='0.0.0.0',host='5000')






