# from flask import Flask, render_template,request
# from tensorflow import keras
# from tensorflow.keras.preprocessing import image
# import numpy as np
# from PIL import Image

# app = Flask(__name__)
# model = keras.models.load_model('model.h5')
# @app.route('/')
# def index():
#     return render_template("imgindex.html", name="Tariq")

# @app.route('/prediction', methods=["POST"])
# def prediction():
#     img = request.files['img']
#     img.save('img.jpg')
#     img = image.load_img("img.jpg", target_size=(110,110))
#     x=image.img_to_array(img) / 255
#     resized_img_np = np.expand_dims(x,axis=0)
#     prediction = model.predict(resized_img_np) 
#     output={'oky':0,'defect':1} 
#     value=np.argmax(prediction)
#     # print(value)
#     lb=list(output.keys())
#     # print(lb)
#     # print(lb[value])
#     pre=lb[value]
#     return render_template("prediction.html", data=pre)


# @app.route('/prediction', methods=["POST"])
# def prediction():
#     img = request.files['img']
#     img.save('img.jpg')
#     img = image.load_img("img.jpg", target_size=(150,150,1))
#     # mapping_class={'ok':0,'defect':1}
#     # best_model='model.h5'
#     # true_label = mapping_class[labels[image_num]]
#     # [[pred_prob]] = best_model.predict(img.reshape(1, *IMAGE_SIZE, -1))
#     # pred_label = mapping_class[int(pred_prob >= THRESHOLD)]
#     # prob_class = 100*pred_prob if pred_label == "defect" else 100*(1-pred_prob)

#     x=image.img_to_array(img) / 150
#     resized_img_np = np.expand_dims(x,axis=0)
#     prediction = model.predict(resized_img_np) 
#     output={'ok':0,'defect':1} 
#     value=np.argmax(prediction)
#     print(value)
#     lb=list(output.keys())
#     # print(lb)
#     # print(lb[value])
#     pre=lb[value]
#     return render_template("imgprediction.html", data=pre)
    


# if __name__ =="__main__":
#     app.run(host='0.0.0.0',port=5000)


#############################################################################################


# from flask import Flask ,render_template,request
# from keras.models import load_model
# from keras.preprocessing import image

# app=Flask(__name__)
# dic={0:'o',1:'d'}
# model=load_model('model.h5')
# # model._make_predict_function()

# # def predict_label(img_Path):
# #     i=image.load_img(img_path,target_size=(100,100))
# #     i=image.img_to_array(i)
# #     i=i.reshape(1,100,100,1)
# #     p=model.predict_classes(i)
# #     return dic[p[0]]

# @app.route('/')
# def index():
#     return render_template('home.html')

# @app.route('/predict',methods=['POST'])
# def predict_label(img_Path):
#     i=image.load_img(img_path,target_size=(100,100))
#     i=image.img_to_array(i)
#     i=i.reshape(100,100,1)
#     p=model.predict_classes(i)
#     return dic[p[0]]

# def predict():
#     if request.method =='POST':
#         img=request.files['my_image']
#         img_path='statics/'+img.filename
#         img.save(img_path)
#         p=predict_label(img_path,model)
#     return render_template('home.html',prediction=p,img_path=img_path)


# if __name__=='__main__':
#     app.run(host='0.0.0.0',port=5000)

####################################################################################################################

# from flask import Flask ,render_template ,request
# import pickle

# @app.route('/predict')
# def prediction("/predict",methods=['POST']):
#     if request.methods=='POST':
#         to_predict_list=request.form.to_dict()
#         to_predict_list=list(map(int,to_predict_list))
#         if int (predict)==0:
#             prediction='okey'
#         else:
#             prediction='defect'
#         return render_template('home.html',prediction=prediction)



####################################################################################################


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






