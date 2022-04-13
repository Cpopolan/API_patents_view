import plotly.graph_objects as go

class Show:
    def __init__(self, file):
        self.file = file

    def show_chart(self):
        """
        Counting the number of patents for Romania
        :return: an integer counter from the existing file ro.txt
        """
        with open(f"{self.file}", "r", encoding="utf-8", errors="ignore") as text:
            number = len(text.readlines())
        return number


def create_plot():
    ro_patent = Show("ro.txt")
    ro = ro_patent.show_chart()
    ua_patent = Show("ua.txt")
    ua = ua_patent.show_chart()

    # Add the values
    fig = go.Figure(
        data=[go.Bar(y=[ro, ua], x=["RO", "UA"])],
        layout_title_text="Comparison of the no.of patents between RO and UA "
                    )
    # Plot the values
    fig.show()
    fig.write_image("plot.png")
