#coding:utf-8

import click

@click.command()
@click.option('--inputfile', prompt=True, help='输入文件名及路径.')
@click.option('--outputfile', prompt=True, help='输出文件名及路径.')
def decryptFile(inputfile, outputfile):
    decryptfile = outputfile
    encryptfile = inputfile

    encrypt = encryptfile.split("_")
    bg_length, confuse_length, confusion_bytes_index = int(encrypt[1]), int(encrypt[2]), int(encrypt[3])
    headerindex = bg_length + confuse_length

    with open(decryptfile, "wb") as fw:
        with open(encryptfile, "rb") as fr:
            data = fr.read()
            frist_data_num = len(data)-(headerindex + confusion_bytes_index + confuse_length)
            frist_data = data[-confusion_bytes_index:]
            second_data = data[headerindex:headerindex+frist_data_num]
            print(headerindex + confusion_bytes_index + confuse_length)
            print(len(frist_data),len(second_data))
            fw.write(frist_data+second_data)

if __name__ == "__main__":
    decryptFile()