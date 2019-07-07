import matplotlib
matplotlib.use("Agg")


from pyimagesearch.minivggnet import MiniVGGNet
from sklearn.metrics import classification_report
from keras.optimizers import SGD
from keras.datasets import fashion_mnist
from keras.utils import np_utils
from imutils import build_montages
import numpy as np

NUM_EPOCHS = 25
INIT_LR = 1e-2
BS = 32

((trainX, trainY), (testX, testY)) = fashion_mnist.load_data()

if K.image_data_format() == "channels_first":
	trainX = trainX.reshape((trainX.shape[0], 1, 28, 28))
	testX = testX.reshape((testX.shape[0], 1, 28, 28))
 

else:
	trainX = trainX.reshape((trainX.shape[0], 28, 28, 1))
	testX = testX.reshape((testX.shape[0], 28, 28, 1))
 
trainX = trainX.astype("float32") / 255.0
testX = testX.astype("float32") / 255.0

trainY = np_utils.to_categorical(trainY, 10)
testY = np_utils.to_categorical(testY, 10)

labelNames = ["top", "trouser", "pullover", "dress", "coat",
	"sandal", "shirt", "sneaker", "bag", "ankle boot"]

opt = SGD(lr=INIT_LR, momentum=0.9, decay=INIT_LR / NUM_EPOCHS)
model = MiniVGGNet.build(width=28, height=28, depth=1, classes=10)
model.compile(loss="categorical_crossentropy", optimizer=opt,
	metrics=["accuracy"])

H = model.fit(trainX, trainY,
	validation_data=(testX, testY),
	batch_size=BS, epochs=NUM_EPOCHS)


preds = model.predict(testX)


print("[INFO] evaluating network...")
print(classification_report(testY.argmax(axis=1), preds.argmax(axis=1),
	target_names=labelNames))


images = []

for i in np.random.choice(np.arange(0, len(testY)), size=(16,)):
	
	probs = model.predict(testX[np.newaxis, i])
	prediction = probs.argmax(axis=1)
	label = labelNames[prediction[0]]
 

	if K.image_data_format() == "channels_first":
		image = (testX[i][0] * 255).astype("uint8")
 
	else:
		image = (testX[i] * 255).astype("uint8")


	color = (0, 255, 0)

	
	if prediction[0] != np.argmax(testY[i]):
		color = (0, 0, 255)
 
	