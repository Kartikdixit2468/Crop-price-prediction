# import pickle

# with open('src/services/model/model.pkl', 'r') as model_file:
#     try: 
#         while True:
#             print("type:",type(pickle.load(model_file)))
        
#     except:
#         print("the end")

import joblib
import numpy as np

model = joblib.load('src\\services\\model\\model.pkl')
print(model)


test_input = np.array([[5.5, 320, 3, 5.5, 320, 3, 5.5, 320, 3, 5.5, 320, 3]])  # adjust shape and values as per your features
prediction = model.predict(test_input)

print("Predicted price:", prediction[0])
