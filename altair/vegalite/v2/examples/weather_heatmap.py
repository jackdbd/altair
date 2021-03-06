"""
Weather Heatmap
---------------
This example shows the 2010 daily max temperature (F) in Seattle, WA.
"""
# category: other charts
import altair as alt
from vega_datasets import data

df = data.seattle_temps.url

alt.Chart(df).mark_rect().encode(
    alt.X('date:O', timeUnit='date') ,
    alt.Y('date:O', timeUnit='month'), 
    alt.Color('temp:Q', aggregate='max'),
    tooltip=[alt.Tooltip('date:T', timeUnit='monthdate', title='Date'),
             alt.Tooltip('temp:Q', aggregate='max', title='Max Temp')]
)
