# scripts/utils.py

import matplotlib.pyplot as plt
import io
import base64

def generate_quadratic_plot(a=1):
    """
    Generates a quadratic plot for the equation y = a * x^2
    """
    x = list(range(-10, 11))
    y = [a * (i ** 2) for i in x]

    plt.figure(figsize=(6, 4))
    plt.plot(x, y, marker='o', linestyle='-', color='g', label=f'y = {a}x²')
    plt.title('Interactive Quadratic Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.grid(True)

    # Save the plot to a PNG image in memory
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img_data = buf.read()

    # Encode the image to base64
    img_base64 = base64.b64encode(img_data).decode('utf-8')
    img_src = f"data:image/png;base64,{img_base64}"

    return img_src
