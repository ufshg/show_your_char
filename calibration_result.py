import pickle

with open("data.pkl", "rb") as f:
    data = pickle.load(f)
    for key in data:
        print(f'{key} : {data[key]}')