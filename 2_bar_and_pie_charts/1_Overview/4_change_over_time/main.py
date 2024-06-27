import plotly.express as px

if __name__ == "__main__":
    # Write your solution here
    px.line(x=[1, 2, 3, 4], y=[5, 6, 7, 8]).write_image('image.png', scale=4)
