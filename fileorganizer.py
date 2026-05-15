import os
import shutil
from pathlib import Path


source_folder = Path(".")


text_folder = Path("Text_Files")

image_folder = Path("Image_Files")

pdf_folder = Path("PDF_Files")


text_folder.mkdir(exist_ok=True)

image_folder.mkdir(exist_ok=True)

pdf_folder.mkdir(exist_ok=True)


for file in source_folder.iterdir():

    if file.is_file():

        if file.suffix == ".txt":

            shutil.move(
                str(file),
                text_folder / file.name
            )

            print(
                file.name,
                "moved to Text_Files"
            )


        elif file.suffix == ".jpg":

            shutil.move(
                str(file),
                image_folder / file.name
            )

            print(
                file.name,
                "moved to Image_Files"
            )


        elif file.suffix == ".pdf":

            shutil.move(
                str(file),
                pdf_folder / file.name
            )

            print(
                file.name,
                "moved to PDF_Files"
            )