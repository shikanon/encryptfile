#coding:utf-8

import click
import random

@click.command()
@click.option('--background', prompt=True, help='输入用于隐藏的背景图片文件.')
@click.option('--encryptfile', prompt=True, help='输入需要加密的文件.')
def encryptfile(background, encryptfile):
    seed = random.randint(1024, 2048)
    seeds = []
    for i in range(seed):
        seeds.append(random.randint(1, 128))
    confusion = bytes(seeds)

    with open(background, 'rb') as fr_bg:
        bg_body = fr_bg.read()

    with open(encryptfile, 'rb') as fr_enc:
        enc_body = fr_enc.read()

    confusion_bytes_index = random.randint(1, len(enc_body)//2)

    objectfile = "encry_%d_%d_%d_"%(len(bg_body), len(confusion), confusion_bytes_index) + background
    data = bg_body + confusion + enc_body[confusion_bytes_index:] + confusion + enc_body[:confusion_bytes_index]

    print(len(bg_body)+len(confusion))
    print(len(enc_body[confusion_bytes_index:]))
    print(len(enc_body[:confusion_bytes_index]))
    print(len(bg_body)+2*len(confusion)+len(enc_body[confusion_bytes_index:]))
    print(len(data))

    with open(objectfile, "wb") as fw_obf:
        fw_obf.write(data)

if __name__ == "__main__":
    encryptfile()