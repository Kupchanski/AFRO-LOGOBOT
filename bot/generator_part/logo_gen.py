import torch
import numpy as np

from models import Generator, OldGenerator
from wgan import GoodGenerator

def gen_logo_color(weight_path="gen_logo_model.pt",  noise = None):
    
    """
    Принимает на вход вектор шума либо генерит случайный
    затем генерирует картинку 64х64 и возвращает ее
    
    """

    netG = GoodGenerator(dim=64, latent_dim = 128,  output_dim=3*64*64)
    netG.load_state_dict(torch.load(weight_path))

    netG.eval()
    netG.cuda()

    if not noise:
        noise = torch.randn(1, 128, device="cuda")

    with torch.no_grad():
        # Get generated image from the noise vector using
        # the trained generator.
        generated_img = netG(noise).detach().cpu()

    return generated_img[0].cpu().detach().numpy().transpose(1,2,0)


"""
Версия для чб. Просто на всякий случай.
def gen_logo_gray(weight_path="gen_logo_model_gray.pt", noise = None):
    
  

    
  

    netG = OldGenerator(img_size = (32,32,1), latent_dim=128, dim=32)
    netG.load_state_dict(torch.load(weight_path))

    netG.eval()
    netG.cuda()

    if not noise:
        noise = torch.randn(1, 128, device="cuda")

    with torch.no_grad():
        # Get generated image from the noise vector using
        # the trained generator.
        generated_img = netG(noise).detach().cpu()

    return generated_img[0].cpu().detach().numpy().squeeze()   """