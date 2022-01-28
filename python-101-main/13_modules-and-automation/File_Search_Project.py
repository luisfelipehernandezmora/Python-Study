import pathlib

folder=pathlib.Path("D:\Luis Felipe\Fotos\Coming from India 2021")
for file in folder.iterdir():
    print(file.name)
    if file.is_dir():
        for file2 in file.iterdir():
            if file2.suffix==".jpg":
                print(file2)    