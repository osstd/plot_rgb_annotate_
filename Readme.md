# Image RGB Channel Component Plotter

This script is used to plot the RGB channel components of an image. It utilizes downsampling to make it easier to read
individual pixel values.

## Features

- Image RGB Channel Plotting: This script allows you to visualize the RGB channel components of an image, making it
  easier to analyze color distribution.
- Opens an image and converts it to a NumPy array.
- Downsampling for Readability: The script employs a downsampling technique to enhance the readability of individual
  pixel values, especially in larger images.
- Support for RGB and RGB + Alpha Channels: Whether your image has RGB channels only or includes an Alpha channel, the
  script can handle both cases for accurate plotting.
- Customizable Downsampling Factor: You can adjust the downsampling factor to fine-tune the level of detail in the
  plotted RGB components, ensuring optimal visualization.
- Simple Usage: With clear instructions and minimal dependencies, the script is easy to use and integrate into your
  image processing workflows.

## Requirements

- Python 3.7+
- NumPy
- PIL (Pillow)
- Matplotlib

## Installation

1. Clone the repository or download the script:

    ```bash
    git clone https://github.com/osstd/plot_rgb_annotate_.git
    cd rgb-plot-annotate
    ```

2. Install the required packages:

    ```bash
    pip install numpy pillow matplotlib
    ```

## Usage

1. Edit the local.py file to specify the path to your image:

    ```bash
    image_path = "path/to/your/image"
   ```

2. Run the script:

    ```bash
    python local.py
    ```
3. Additional Notes

   Adjust the:
   ```bash 
   downsampling_factor 
   ```
   variable for better readability of pixel values.

## Functionality

- `open_image()` opens the specified image and extracts RGB values for plotting.
- `plot()` generates scatter plots with different markers with different pixel value compositions

## Demonstration

[For demonstration](https://what-is-a-pixel-vercel.vercel.app/visualize2)

## Example

![Demonstration](https://i.imgur.com/GPp7VMw.png)

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.
