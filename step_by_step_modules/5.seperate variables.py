import pandas as pd 
import matplotlib.pyplot as plt

data = pd.read_csv('dataset.csv')
X = data.drop(["label"],axis=1)
Y= data["label"]

idx = 18
img = X.loc[idx].values.reshape(28,28)
print(Y[idx])

plt.imshow(img, cmap='gray')  # Use 'cmap' to specify the color map (e.g., grayscale)
plt.title("Image Preview")  # Add a title if needed
plt.show()  # Show the image