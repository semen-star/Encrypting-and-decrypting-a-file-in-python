import pyAesCrypt
a=int(input("Что вы хотите сделать?\n1.Зашифровать файл\n2.Расшифровать файл\nОжидается ввод:"))

def encrypt():
    infile=input("Введите где находиться файл с его именем и расширением:")
    outfile=input("Придумайте название нового файла указав расположение(расширение учитывается именем):")
    password=input("Придумайте пароль:")
    pyAesCrypt.encryptFile(infile, outfile, password)


def decrypt():
    infile = input("Введите где находиться файл с его именем и расширением:")
    outfile = input("Придумайте название нового файла указав расположение и расширение:")
    password=input("Введите пароль:")
    pyAesCrypt.decryptFile(infile, outfile, password)

if a==1:
    encrypt()
else:
    decrypt()