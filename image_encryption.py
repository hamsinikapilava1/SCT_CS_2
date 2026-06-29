"""
Image Encryption Tool using Pixel Manipulation
SkillCraft Technology - Cybersecurity Internship - Task 2

Supports:
  - XOR encryption/decryption (key-based)
  - Pixel value inversion
  - Pixel swapping (row-by-row shuffle)

Author: Hamsini
"""

from PIL import Image
import os


def xor_encrypt_decrypt(image_path, key, output_path):
    """
    Applies XOR operation on every pixel channel using the given key.
    Same function works for both encryption and decryption (XOR is symmetric).

    Args:
        image_path (str): Path to the input image file.
        key (int): Integer key in range 0-255 for XOR operation.
        output_path (str): Where to save the output image.
    """
    img = Image.open(image_path).convert("RGB")
    pixels = img.load()
    width, height = img.size

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            pixels[x, y] = (r ^ key, g ^ key, b ^ key)

    img.save(output_path)
    print(f"[+] XOR operation done. Output saved to: {output_path}")


def invert_pixels(image_path, output_path):
    """
    Inverts each pixel channel value (255 - value).
    This is a basic mathematical operation on pixels.

    Args:
        image_path (str): Input image path.
        output_path (str): Output image path.
    """
    img = Image.open(image_path).convert("RGB")
    pixels = img.load()
    width, height = img.size

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            pixels[x, y] = (255 - r, 255 - g, 255 - b)

    img.save(output_path)
    print(f"[+] Pixel inversion done. Output saved to: {output_path}")


def swap_pixels(image_path, output_path):
    """
    Swaps adjacent pixels across each row.
    Pixel at position (x, y) is swapped with (x+1, y).

    Args:
        image_path (str): Input image path.
        output_path (str): Output image path.
    """
    img = Image.open(image_path).convert("RGB")
    pixels = img.load()
    width, height = img.size

    for y in range(height):
        for x in range(0, width - 1, 2):
            # swap pixel at (x, y) with pixel at (x+1, y)
            pixels[x, y], pixels[x + 1, y] = pixels[x + 1, y], pixels[x, y]

    img.save(output_path)
    print(f"[+] Pixel swap done. Output saved to: {output_path}")


def menu():
    print("\n" + "=" * 50)
    print("   IMAGE ENCRYPTION TOOL - SCT_CS_2")
    print("   SkillCraft Cybersecurity Internship")
    print("=" * 50)
    print("1. XOR Encrypt / Decrypt (key-based)")
    print("2. Invert Pixels")
    print("3. Swap Adjacent Pixels")
    print("4. Exit")
    print("-" * 50)


def get_image_path(prompt="Enter image path: "):
    path = input(prompt).strip()
    if not os.path.exists(path):
        print(f"[!] File not found: {path}")
        return None
    return path


def main():
    while True:
        menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            img = get_image_path("Enter image to encrypt/decrypt: ")
            if not img:
                continue
            try:
                key = int(input("Enter XOR key (0-255): ").strip())
                if not 0 <= key <= 255:
                    print("[!] Key must be between 0 and 255.")
                    continue
            except ValueError:
                print("[!] Invalid key. Enter a number.")
                continue
            out = input("Enter output filename (e.g. encrypted.png): ").strip()
            xor_encrypt_decrypt(img, key, out)

        elif choice == "2":
            img = get_image_path()
            if not img:
                continue
            out = input("Enter output filename: ").strip()
            invert_pixels(img, out)

        elif choice == "3":
            img = get_image_path()
            if not img:
                continue
            out = input("Enter output filename: ").strip()
            swap_pixels(img, out)

        elif choice == "4":
            print("\nExiting Image Encryption Tool. Goodbye!")
            break

        else:
            print("[!] Invalid option. Try again.")


if __name__ == "__main__":
    main()
