import random
# import json

# import torch

# from model import NeuralNet
# from nltk_utils import bag_of_words, tokenize
import time
# import pyautogui
from threading import Timer

# device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# with open('intents.json', 'r') as json_data:
#     intents = json.load(json_data)

# FILE = "data.pth"
# data = torch.load(FILE)

# input_size = data["input_size"]
# hidden_size = data["hidden_size"]
# output_size = data["output_size"]
# all_words = data['all_words']
# tags = data['tags']
# model_state = data["model_state"]

# model = NeuralNet(input_size, hidden_size, output_size).to(device)
# model.load_state_dict(model_state)
# model.eval()

bot_name = "Sam"

def get_response(msg):
    # sentence = tokenize(msg)
    # X = bag_of_words(sentence, all_words)
    # X = X.reshape(1, X.shape[0])
    # X = torch.from_numpy(X).to(device)

    # output = model(X)
    # _, predicted = torch.max(output, dim=1)

    # tag = tags[predicted.item()]

    # probs = torch.softmax(output, dim=1)
    # prob = probs[0][predicted.item()]
    # if prob.item() > 0.75:
    #     for intent in intents['intents']:
    #         if tag == intent["tag"]:
    #             return random.choice(intent['responses'])
    
    return "Response without Pytorch"


# def break_func():
#     print("Are you still there?")
    
# def break_func2():
#     global inactive
#     print("Chat session has been ended due to inactivity!")
#     inactive = True
#     pyautogui.press("enter")


if __name__ == "__main__":
    print("Let's chat! (type 'quit' to exit)")
    while True:
        # sentence = "do you use credit cards?"
        
        # t1 = Timer(120, break_func)
        # t2 = Timer(240, break_func2)
        # t1.start()
        # t2.start()
        sentence = input("You: ")
        # t1.cancel()
        # t2.cancel()
        if sentence == "quit":
            break

        # if inactive:
        #     break

        # inactive = False
        
        time.sleep(4)  #Add this


        resp = get_response(sentence)
        print(resp)

