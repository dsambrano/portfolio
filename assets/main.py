from PIL import Image
from pathlib import Path


def set_background(filename: Path):
    image = Image.open(filename)
    new_image = Image.new("RGBA", image.size, "WHITE")
    new_image.paste(image, (0, 0), image)
    new_image.convert("RGB").save(f"{filename.stem}.png", "PNG")


def main():
    p = Path("transparent")
    graphs = p.glob("*.png")
    for graph in graphs:
        print("Processing: ", graph)
        set_background(graph)


if __name__ == "__main__":
    main()
