import streamlit as st
import numpy as np
import plotly.figure_factory as ff
import time
import plotly.graph_objects as go
import requests
import pandas as pd

import json
from datetime import datetime
global_headers = {'Content-type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'}

# Read data from a csv
z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')
#print("z_data",z_data)
if True:
    import numpy as np
    import time

    import time

    token_to_plot = "So11111111111111111111111111111111111111112"
    over_the_last_X_days = 30
    starting = int(time.time())
    ending = starting - over_the_last_X_days * 24 * 60 * 60

    url1 = "http://api.fibonacci.fi/onchain_histo_price/SOL/" + token_to_plot + "/EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v/5/5m"

    response = requests.get(url1, headers=global_headers, timeout=100000)
    jjson = json.loads(response.content.decode('utf-8'))
    price_data=jjson
    datae = pd.json_normalize(jjson["data"])
    print(datae["ts"][2])
    onchain_btc_datae = datae.copy()
    price_data_ts=np.array(onchain_btc_datae["ts"])
    price_data_close=np.array(onchain_btc_datae["close"])




    chain = "SOL"
    pool = "7qbRF6YsyGuLUVs6Y1q64bdVrfe4ZcUUz1JRdoVNUJnm"
    xdays = 5
    price_to_plot = 18
    amplitude = 1.3  # The higher the coef the wider the range plotted the smaller the details.


    token_to_plot = "So11111111111111111111111111111111111111112"
    over_the_last_X_days = 3
    amplitude_coef = amplitude

    starting = int(time.time())
    ending = starting - over_the_last_X_days * 24 * 60 * 60
    url1 = "http://api.fibonacci.fi/pool_composition/" + chain + "/" + pool + "/" + str(xdays) + "/15m"
    print(url1)
    headers = {'Content-type': 'application/x-www-form-urlencoded',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'}
    response = requests.get(url1, headers=headers, timeout=120)

    jjson = json.loads(response.content.decode('utf-8'))
    rdata2 = pd.DataFrame.from_records(jjson["data"])
    rdata2 = np.transpose(rdata2)
    rdata2r = rdata2.copy()
    rdata2r.columns=["Price","Liquidity","Ts"]
    rdata2r = rdata2r.sort_values("Ts", ascending=True)
    rdata2r=rdata2r[["Ts","Price","Liquidity"]]

    x = np.array(rdata2r["Ts"])
    y = np.array(rdata2r["Price"])
    z = np.array(rdata2r["Liquidity"])/10000000000000

    xi = np.linspace(x.min(), x.max(), 100)
    yi = np.linspace(y.min(), y.max(), 100)

    X, Y = np.meshgrid(xi, yi)


    xii=[]
    tss=np.array(rdata2r["Ts"])
    sizee=[]
    for d in range(len(tss)):
        sizee.append(10)
        xii.append(datetime.utcfromtimestamp(tss[d]).strftime('%m-%d %H:%M'))
    uni_date=list(set(rdata2r["Ts"]))
    max_l=np.mean(z)
    max_lc=np.min(z)
    colorz=z.copy()
    pxxs=np.array(rdata2r["Price"])
    for date in uni_date:


        current_price = 0
        for date_2 in range(1, len(price_data_ts)):

            if price_data_ts[date_2] >= date and price_data_ts[date_2 - 1] < date:
                current_price = float(price_data_close[date_2])
                xii=np.append(xii,datetime.utcfromtimestamp(date).strftime('%m-%d %H:%M'))
                pxxs=np.append(pxxs,current_price)
                z=np.append(z,max_l)
                colorz=np.append(colorz,max_lc)
                sizee.append(10)
                print("Uuuh")
                break

    sizee=np.array(sizee)
if True:
    #fig = go.Figure(data=[go.Scatter3d(x=np.array(xii),y=yi,z=Z)])
    fig = go.Figure(data=
                    [go.Scatter3d(x=np.array(xii),
                                  y=pxxs,
                                  z=z,
                                  mode='markers',
                                  marker=dict(
                                      size=np.array(sizee),
                                      color=colorz,  # set color to an array/list of desired values
                                      colorscale='Thermal',  # choose a colorscale
                                      opacity=1
                                  )
                                  )])
    fig.update_layout(margin=dict(l=65, r=50, b=65, t=90))



else:
    # Add histogram data
    x1 = np.random.randn(200) - 2
    x2 = np.random.randn(200)
    x3 = np.random.randn(200) + 2

    # Group data together
    hist_data = [x1, x2, x3]

    group_labels = ['Group 1', 'Group 2', 'Group 3']

    # Create distplot with custom bin_size
    fig = ff.create_distplot(
            hist_data, group_labels, bin_size=[.1, .25, .5])

# Plot!
st.plotly_chart(fig, use_container_width=True)