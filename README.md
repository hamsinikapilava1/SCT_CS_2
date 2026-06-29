# Image Encryption Tool using Pixel Manipulation

## Overview

This project is a simple implementation of basic image encryption techniques using pixel manipulation methods in Python. It demonstrates how images can be encrypted and decrypted by applying mathematical and logical operations directly on pixel values.

The tool supports multiple image transformation techniques such as XOR encryption, pixel inversion, and pixel swapping. These methods help illustrate fundamental concepts used in image security and cybersecurity.

## Features

* XOR-based Image Encryption and Decryption
* Pixel Value Inversion
* Adjacent Pixel Swapping
* Menu-driven Command Line Interface
* Input validation for image paths and encryption keys
* Supports common image formats using the Pillow library
* Simple and user-friendly execution flow

## Cybersecurity Concepts Demonstrated

### XOR Encryption

XOR (Exclusive OR) is a widely used operation in cryptography. Each pixel channel (Red, Green, Blue) is combined with a secret key using the XOR operation.

Since XOR is symmetric, the same operation and key can be used for both encryption and decryption.

### Image Obfuscation

Pixel inversion and pixel swapping techniques modify the visual appearance of an image, making it unreadable without applying the reverse operation.

These methods demonstrate basic image obfuscation principles used in multimedia security.

### Symmetric Encryption Concept

The XOR technique demonstrates the concept of symmetric encryption, where the same key is used for both encryption and decryption.

### Input Validation

The program validates:

* Image file existence before processing
* XOR key values (must be between 0 and 255)
* User menu choices

This prevents invalid inputs and improves program reliability.

## Techniques Implemented

### 1. XOR Encrypt / Decrypt

Each RGB channel value is XORed with a user-provided key.

**Formula:**

`Encrypted Pixel = Original Pixel XOR Key`

Applying the same key again restores the original image.

### 2. Pixel Inversion

Every pixel channel value is inverted using:

`New Value = 255 - Current Value`

This produces a negative version of the image.

### 3. Pixel Swapping

Adjacent pixels in each row are swapped sequentially.

Example:

`(Pixel1, Pixel2) → (Pixel2, Pixel1)`

Applying the swap operation again restores the original arrangement.

## Requirements

* Python 3.x
* Pillow Library

Install dependencies using:

```bash
pip install pillow
```

## How to Run

```bash
python image_encryption_tool.py
```

Follow the on-screen menu to select an operation and provide the required inputs.

## Example Operations

### Encrypt an Image Using XOR

1. Select option 1
2. Enter image path
3. Enter XOR key (0–255)
4. Provide output filename

### Invert Image Colors

1. Select option 2
2. Enter image path
3. Provide output filename

### Swap Adjacent Pixels

1. Select option 3
2. Enter image path
3. Provide output filename
