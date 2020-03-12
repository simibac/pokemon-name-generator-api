import pandas as pd
import numpy as np
import keras
import time
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.optimizers import RMSprop
import tensorflow as tf
import random
import os
from tensorflow.keras.models import load_model

# To hide warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

class NameGenerator:
    def __init__(self, model_path, input_names_path):
        # Load names from the file
        self.input_names = load_names(input_names_path)

        # Make it them to a long string
        self.concat_names = '\n'.join(self.input_names).lower()

        # Find all unique characters by using set()
        self.chars = sorted(list(set(self.concat_names)))

        # Build translation dictionaries, 'a' -> 0, 0 -> 'a'
        self.char2idx = dict((c, i) for i, c in enumerate(self.chars))
        self.idx2char = dict((i, c) for i, c in enumerate(self.chars))

        # Count the number of unique characters
        self.num_chars = len(self.chars)

        # Use longest name length as our sequence window
        self.max_sequence_length = max([len(name) for name in self.input_names])

        self.sequence = self.concat_names[-(self.max_sequence_length - 1):] + '\n'

        # Load the model
        self.model = load_model(model_path)


    def generate_names(self, gen_amount):
        new_names = []

        print('{} new names are being generated'.format(gen_amount))

        while len(new_names) < gen_amount:
            
            # Vectorize sequence for prediction
            x = np.zeros((1, self.max_sequence_length, self.num_chars))
            for i, char in enumerate(self.sequence):
                x[0, i, self.char2idx[char]] = 1

            # Sample next char from predicted probabilities
            probs = self.model.predict(x, verbose=0)[0]
            probs /= probs.sum()
            next_idx = np.random.choice(len(probs), p=probs)   
            next_char = self.idx2char[next_idx]   
            self.sequence = self.sequence[1:] + next_char

            # New line means we have a new name
            if next_char == '\n':

                gen_name = [name for name in self.sequence.split('\n')][1]

                # Never start name with two identical chars, could probably also
                if len(gen_name) > 2 and gen_name[0] == gen_name[1]:
                    gen_name = gen_name[1:]

                # Discard all names that are too short
                if len(gen_name) > 2:
                    
                    # Only allow new and unique names
                    if gen_name not in self.input_names + new_names:
                        new_names.append(gen_name.capitalize())

        return new_names

def load_names(input_path):
    names = []
    with open(input_path) as f:
        for name in f:
            name = name.rstrip()
            names.append(name)
    return names



if __name__ == "__main__":
    model_path = os.path.realpath('../poke_gen_model.h5')
    input_names_path = os.path.realpath('../input/names.txt')
    generator = NameGenerator(model_path, input_names_path)
    print(generator.generate_names(2))
