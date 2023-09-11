import streamlit as st
import numpy as np
import time
import altair as alt
import requests
import json
import pandas as pd
import datetime
from altair import *

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()




global_headers = {'Content-type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'}



#Schema : /histo_slippage/<string:chain>/<string:coin1>/<string:coin2>/<int:timeperiod>/<int:granularity>
coin1="So11111111111111111111111111111111111111112"

url1="http://api.fibonacci.fi/histo_slippage/SOL/"+coin1+"/EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v/5/1m"


response = requests.get(url1, headers=global_headers, timeout=60)

jjson = json.loads(response.content.decode('utf-8'))

rdata2 = pd.DataFrame.from_records(jjson["data"])
rdata2 = rdata2.sort_values('Time')

name2="Slippage in % for a sell of 500k$ (RHS)"
dd=rdata2[["-500000","Price",'Time']]
dd.columns=[name2,"Price in $ (LHS)","Time"]

tmm=dd['Time'].values.tolist()
rtt=[]
for tt in tmm:
    rtt.append(datetime.datetime.fromtimestamp(tt).strftime('%d/%m/%y'))

#dd["Time"]=rrt





df = dd

if True:
    a=alt.Chart(df, title="SOL liquidity level & price").mark_line().encode(
        x=alt.X('Time:T', axis=alt.Axis(format='%H:%M')),
        y=alt.Y('Price in $ (LHS)',
        scale=alt.Scale(domain=[np.min(dd["Price in $ (LHS)"]), np.max(dd["Price in $ (LHS)"])]),


                ),
        color=alt.value("#FFAA00"),
    )
    b=alt.Chart(df).mark_line().encode(
        x=alt.X('Time:T', axis=alt.Axis(format='%dd/%mm')),
        y=alt.Y(name2, scale=alt.Scale(domain=[np.min(dd[name2]), np.max(dd[name2])]),

                )
    )
    c = alt.layer(a, b).resolve_scale(
        y='independent'
    )
    st.altair_chart(c, use_container_width=True)

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")