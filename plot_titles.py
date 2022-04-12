import plotly.graph_objects as go

def show_ro():
    """
    Counting the number of patents for Romania
    :return: an integer counter from the existing file ro.txt
    """
    with open("ro.txt", "r", encoding="utf-8") as text:
        count = 0
        for i in text:
            count += 1
        return count

def show_hu():
    """
    Counting the number of patents for Hungary
    :return: an integer counter from the existing file hu.txt
    """
    with open("hu.txt", "r", encoding="utf-8") as text:
        count = 0
        for i in text:
            count += 1
        return count

RO_patent = show_ro()
HU_patent = show_hu()

# Add the values
fig = go.Figure(
    data=[go.Bar(y=[RO_patent, HU_patent], x=["RO", "HU"])],
    layout_title_text="Comparison of the no.of patents between RO and HU "
)
# Plot the values
fig.show()
fig.write_image("plot.png")