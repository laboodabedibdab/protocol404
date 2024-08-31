import tensorflow as tf
from tensorflow.keras.layers import Conv1D, MaxPooling1D, Flatten, Dense, Dropout
from tensorflow.keras.models import Sequential
from keras.optimizers import Adam
from to_train_data import load_data

# Загрузка и подготовка данных (пример)
X_train, Y_train, X_test, Y_test = load_data()

# Создание модели
model = Sequential()
model.add(Conv1D(32, 3, activation='relu', input_shape=(5*8000, 1)))
model.add(MaxPooling1D(2))
model.add(Conv1D(64, 3, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.001)))
model.add(MaxPooling1D(2))
model.add(Flatten())
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.2))  # Добавили слой Dropout с вероятностью отключения 20%
model.add(Dense(1, activation='sigmoid'))

# Компиляция модели
model.compile(loss='binary_crossentropy', optimizer=Adam(learning_rate=0.001), metrics=['accuracy'])
print(X_train.shape)
print(Y_train.shape)
print(X_test.shape)
print(Y_test.shape)

# Обучение модели
model.fit(X_train, Y_train, epochs=10, validation_data=(X_test, Y_test))
print(model.predict(X_test))
print(Y_test)