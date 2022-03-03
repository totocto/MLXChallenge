# MLXChallenge

### 1 - Which consommation for a training ?

The aim of this part, is to measure environment impact during algorithm training

- First you'll need to install necessary depedencies `pip install -r requirements.txt`

- We will work on mnist dataset that you can load with

`(x_train, y_train), (x_test, y_test) = mnist.load_data()`

- Choose an algithm to predict correctly digits

- Now estimate the emission of your training (add the fit between `tracker.start()` and `tracker.stop`)

- Do the same thing with a neural network to compare:

```
model = tf.keras.models.Sequential(
    [
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation="relu"),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10),
    ]
)

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
model.compile(optimizer="adam", loss=loss_fn, metrics=["accuracy"])
```

- You can observe a new file emissions.csv. Observe all information they give you

- To visualize it with the codecarbon interface, you can use command: `carbonboard --filepath=emissions.csv --port=3000

#### 2- Is this front is eco-friendly or greenwashing?

- Create a new profile into your chrome

- Install chrome extension "GreenIT"

- Go to the website you want to analyze

- into the inspector, go to the GreenIT tab

- clear cache, press CMD-R, check 'Activer l'analyse des bonnes pratiques' and click on 'Lancer l'analyse

