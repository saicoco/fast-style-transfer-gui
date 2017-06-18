# coding=utf-8
__author__ = 'JiaGeng'
import make_image
import scipy.misc, numpy as np

def save_img(out_path, img):
    img = np.clip(img, 0, 255).astype(np.uint8)
    scipy.misc.imsave(out_path, img)

def save_mask_style(output_path, img, mask, content):
    mask = np.stack([mask, mask, mask], axis=2).astype(np.float32)
    print mask.dtype, content.shape
    mask_content = content * (1 - mask/255)
    print mask_content.shape
    mask_style = img * (mask/255)
    mask_result = mask_content + mask_style
    save_img(output_path, mask_result)
    return mask_result

def ffwd(maker, content,  outpath, mask):
    im, content_img = maker.generate(outpath, content)
    if mask is not None:
        im = save_mask_style(output_path=outpath, content=content_img, mask=mask, img=im)
    else:
        save_img(outpath, im)
    del maker
    return im