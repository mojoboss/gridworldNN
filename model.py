from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import RMSprop

def create_model():
	#set architecture
	model = Sequential()
	model.add(Dense(164, init = 'lecun_uniform', input_shape=(64,)))
	model.add(Activation('relu'))
	model.add(Dense(150, init='lecun_uniform'))
	model.add(Activation('relu'))
	model.add((Dense(4, init='lecun_uniform')))
	model.add(Activation('linear'))
	#compile model
	rms = RMSprop()
	model.compile(loss='mse', optimizer=rms)
	return model
