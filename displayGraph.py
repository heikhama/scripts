# # scripts/plot.py

# import matplotlib.pyplot as plt
# import io
# import base64
# from js import document

# # Sample data
# x = [0, 1, 2, 3, 4, 5]
# y = [0, 1, 4, 9, 16, 25]

# # Create a plot
# plt.figure(figsize=(6, 4))
# plt.plot(x, y, marker='o', linestyle='-', color='b', label='y = x²')
# plt.title('Sample Matplotlib Plot')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.legend()
# plt.grid(True)

# # Save the plot to a PNG image in memory
# buf = io.BytesIO()
# plt.savefig(buf, format='png')
# buf.seek(0)
# img_data = buf.read()

# # Encode the image to base64 to embed in HTML
# img_base64 = base64.b64encode(img_data).decode('utf-8')
# img_src = f"data:image/png;base64,{img_base64}"

# # Inject the image into the HTML
# plot_div = document.getElementById("plot-output")
# plot_div.innerHTML = f'<img src="{img_src}" alt="Matplotlib Plot">'
import numpy as np
import IPython.display as display
from matplotlib import pyplot as plt
import io
import base64

ys = 200 + np.random.randn(100)
x = [x for x in range(len(ys))]

fig = plt.figure(figsize=(4, 3), facecolor='w')
plt.plot(x, ys, '-')
plt.fill_between(x, ys, 195, where=(ys > 195), facecolor='g', alpha=0.6)
plt.title("Sample Visualization", fontsize=10)

data = io.BytesIO()
plt.savefig(data)
image = F"data:image/png;base64,{base64.b64encode(data.getvalue()).decode()}"
alt = "Sample Visualization"
display.display(display.Markdown(F"""![{alt}]({image})"""))
plt.close(fig)