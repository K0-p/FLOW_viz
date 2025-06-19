import random
import math
import numpy as np
from layer1 import l1_collect
from mp3_convert import decode_output

print("This is a test file for the rs_test.py script.")

def test_seed():
    random.seed(42)
    assert random.random() == 0.6394267984578837
    print("Seed test passed.")

    output_file = 'backend/output.mp3'
    audio_data = decode_output(output_file)
    frames = l1_collect(audio_data)

    # Test scatter seeding algo based on left_right
    print("Testing scatter seeding based on left_right attribute of " + str(len(frames)) + " frames:")
    for frame in frames:
        random.seed(frame.left_right)
        unique_values = random.sample(range(1, 248), 57)
        print("random seed: " + str(random.random()))
        print(unique_values)

        # Create pairings by matching vals 1-10 with 11-18
        pairs = []
        for i in range(25):
            x = unique_values[i]
            for z in range(25, 57):
                y = unique_values[z]
                pairs.append((x, y))

        print(len(pairs), " pairs created.")
        print("set length: " + str(len(set(pairs))))

test_seed()