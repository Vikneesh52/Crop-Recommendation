import pickle

pkl_filename = 'Crop_Recommendation.pkl'
with open(pkl_filename, 'rb') as file:
    model = pickle.load(file)

input_values = []
num_features = 7

for i in range(num_features):
    value = input(f"Enter value for feature {i+1}: ")
    input_values.append(float(value))

X_new = [input_values]

predictions = model.predict(X_new)
print("Predicted crop:", predictions[0])
