import pandas as pd
import matplotlib.pyplot as plt

import base64
from io import BytesIO

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format = 'svg')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


def getbarplot(df):
    df.sort_values('count', ascending = False, inplace = True)
    plt.switch_backend('AGG')

    fig, ax = plt.subplots(figsize=(16, 10))

    ax.barh(df['enrichment'],df['count'])

    ax.autoscale(enable=True)

    bargraph = get_graph()
    return bargraph


