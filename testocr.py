#%%
import easyocr

#%%
reader = easyocr.Reader(['en']) # this needs to run only once to load the model into memory
result = reader.readtext('/home/OCR/examples/english.png')
result

# res = reader.


# %%
import torch
from torch2trt import torch2trt
from torchvision.models.alexnet import alexnet

# create some regular pytorch model...
model = alexnet(pretrained=True).eval().cuda()

# create example data
x = torch.ones((1, 3, 224, 224)).cuda()

# convert to TensorRT feeding sample data as input
model_trt = torch2trt(model, [x])

# %%
