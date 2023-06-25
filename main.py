from tkinter import *
import datetime as dt
import yfinance as yf
import plotly.graph_objects as go

#######################################################################

def graph():
    selected_share = r.get()
    myLabel = Label(window, text=selected_share)
    myLabel.pack()

    ticker = selected_share
    start = dt.datetime(2020, 1, 1)
    end = dt.datetime.now()

    try:
        data = yf.download(ticker, start=start, end=end)
        if data.empty:
            raise Exception("No data available for the selected company.")
    except Exception as e:
        myLabel.config(text=str(e))
        return

    fig = go.Figure(data=[go.Candlestick(x=data.index,
                                         open=data['Open'],
                                         high=data['High'],
                                         low=data['Low'],
                                         close=data['Close'])])

    fig.update_layout(title="Current Share Price of " + selected_share,
                      template="plotly_dark")  # Set the template to "plotly_dark" for dark mode

    fig.show()

window = Tk()
window.title("1")
window.state("zoomed")
r = StringVar()

Radiobutton(window, text="FaceBook", variable=r, value="META").pack()
Radiobutton(window, text="Apple", variable=r, value="AAPL").pack()
Radiobutton(window, text="L&T", variable=r, value="LT.NS").pack()
Radiobutton(window, text="Tesla", variable=r, value="TSLA").pack()
Radiobutton(window, text="Amazon", variable=r, value="AMZN").pack()
Radiobutton(window, text="Asian Paint", variable=r, value="ASIANPAINT.NS").pack()
Radiobutton(window, text="Britannia", variable=r, value="BRITANNIA.NS").pack()
Radiobutton(window, text="Bajaj", variable=r, value="BAJFINANCE.NS").pack()
Radiobutton(window, text="Reliance", variable=r, value="RELIANCE.NS").pack()
Radiobutton(window, text="Infosys", variable=r, value="INFY").pack()
Radiobutton(window, text="Fis", variable=r, value="FIS").pack()

my_button = Button(window, text="Graph It!!", command=graph)
my_button.pack(side=TOP, expand=YES)

window.mainloop()
