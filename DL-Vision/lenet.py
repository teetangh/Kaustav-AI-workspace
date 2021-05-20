import numpy as np
import matplotlib.pyplot as plt

import torch
import torch.nn as nn
import torchvision
from torchvision.utils import make_grid, save_image


def lenetModel():

    def __init__(self):
        pass

    def forward():
        pass


def imshow(img):
    img = img/2 + 0.5
    npimg = img.numpy()
    plt.imshow(np.transpose(npimg, axes=(1, 2, 0)))
    plt.show()


def main():

    batch_size = 4
    transform = torchvision.transforms.Compose(
        [
            torchvision.transforms.ToTensor(),
            torchvision.transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
        ]
    )

    train_set = torchvision.datasets.CIFAR10(
        root="./data/", train=True, transform=transform, download=True)
    train_loader = torch.utils.data.DataLoader(
        dataset=train_set, batch_size=batch_size,  shuffle=True, num_workers=2)

    test_set = torchvision.datasets.CIFAR10(
        root="./data/", train=False, transform=transform, download=True)
    test_loader = torch.utils.data.DataLoader(
        dataset=test_set, batch_size=batch_size,  shuffle=True, num_workers=2)

    # classes = ('plane', 'car', 'bird', 'cat',
    #            'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

    # imshow(train_set[0])

    classes = train_set.classes
    print("classes: ", classes)

    class_count = {}
    for _, index in train_set:
        # print("temp, index ", temp, index)
        label = classes[index]
        if label not in class_count:
            class_count[label] = 0
        class_count[label] += 1
    print("class_count: ", class_count)

    dataiter = iter(train_loader)
    images, labels = dataiter.next()

    imshow(torchvision.utils.make_grid(images))
    print(' '.join('%5s' % classes[labels[j]] for j in range(batch_size)))


if __name__ == "__main__":
    main()
