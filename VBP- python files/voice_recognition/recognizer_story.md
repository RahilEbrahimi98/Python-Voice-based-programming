##Recognizer documentation

To use the recognizer an instance is needed. The instance can be created  as followed:


####Sphinx Recognizer

```sh
recognizer = SphinxRecognizer()
```

####Google Recognizer

```sh
recognizer = GoogleRecognizer()
```

The constructor can also be passed a parameter called `noise_adjust_duration`. This parameter determines the number of 
seconds the recognizer has to wait in order to listen to the environment and recognize the surrounding noise.

<br>

To recognize from the microphone use the recognize method. This method returns the recognized text and also stores it
in the `current_result_text` property of the class so that it can be reached when ever needed.

####Sphinx Or Google Recognizer

```sh
text = recognizer.recognize()
```

The recognize method for sphinx also has an optional parameter named `no_digits_allowed` which its default value is set
to `Flase`. When set to `True` the result text will not contain numbers in digit format. Otherwise, it will. For Google
recognizer however the result always contains numbers in digit format.