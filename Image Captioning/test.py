from get_loader import get_loader
from utils import load_checkpoint, print_examples
import torch
from model_test import CNNtoRNN
import torch.optim as optim
import torchvision.transforms as transforms


def test():
    transform = transforms.Compose(
        [
            transforms.Resize((356, 356)),
            transforms.RandomCrop((299, 299)),
            transforms.ToTensor(),
            transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
        ]
    )

    train_loader, dataset = get_loader(
        root_folder="flickr8k/images",
        annotation_file="flickr8k/captions.txt",
        transform=transform,
        num_workers=2,
    )

    torch.backends.cudnn.benchmark = True
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    # Hyperparameters
    embed_size = 256
    hidden_size = 256
    vocab_size = len(dataset.vocab)
    num_layers = 1
    learning_rate = 3e-4

    # intialise model,loss etc
    model = CNNtoRNN(embed_size, hidden_size, vocab_size, num_layers).to(device)
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)

    step = load_checkpoint(torch.load('my_checkpoint.pth.tar'), model, optimizer)
    model.eval()
    print_examples(model, device, dataset)


if __name__ == "__main__":
    test()