
import torch
from model_utils import SimpleModel, encode, pad

# Load saved artifacts
vocab = torch.load("vocab.pt")

model = SimpleModel(len(vocab) + 1, embed_dim=16)
model.load_state_dict(torch.load("model.pt", map_location="cpu"))
model.eval()


def predict(title):
    seq = encode(title, vocab)
    padded = pad(seq)
    x = torch.tensor([padded])

    with torch.no_grad():
        logits = model(x)
        prob = torch.sigmoid(logits).item()

    return prob


if __name__ == "__main__":
    title = input("Enter a title: ")
    prob = predict(title)

    print(f"\nProbability: {prob:.3f}")
    print("Prediction:", "High engagement" if prob > 0.5 else "Low engagement")
