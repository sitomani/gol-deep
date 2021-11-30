# Deep Learning With Game Of Life

This repository was started as a personal exercise in AI to accompany **Andrew Ng**'s [Deep Learning specialization](https://www.deeplearning.ai/) courses that I was going through. Although I don't have anything specific against cats, I wanted to find my own problem domain to experiment in, and came up with the idea to study if it would be possible to teach a ML algorithm to 'play' **James Conway**'s [Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).

Before delving into deeplearning.ai exercises I had done nothing more than very basic scripting in Python, so this repository works also as a playground for me to get a bit more familiar with the language. The [deeplearning.ai](https://www.deeplearning.ai) course material was also my first encounter with [Jupyter](http://jupyter.org/) Notebooks; I enjoyed working with the notebooks during learning, so it was a natural choice for building my own exercises, too. Current version of the repository makes use of JupyterLab, but you can run the notebooks with standalone jupyter as well.

The repository contains a number of Jupyter notebooks where I've tried to apply the intuitions gained while watching **Andrew Ng**'s video lectures and completing the related assignments in [deeplearning.ai](https://www.deeplearning.ai) specialization.

### Required packages

(If you want to run these notebooks locally, the following tools/libs are needed)

- Python 3 (this project uses 3.9.4)
- JupyterLab
- Numpy
- Matplotlib
- Tensorflow
- Keras

Use `pip install -r requirements` in a python3 env to set up same library versions as were used in development of the notebooks.

### Chapters

1. [Introduction](GOL_Intro.ipynb)
2. [Logistic Regression](GOL_LR.ipynb)
3. [Multi-Layer Neural Network](GOL_NN.ipynb)
4. [Convolutional Neural Network](GOL_CNN.ipynb)
5. Recurrent Neural Network (TBD)
