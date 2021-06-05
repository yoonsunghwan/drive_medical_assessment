import plotly.graph_objects as go
import pandas as pd
import plotly.express as px


df = pd.read_excel('Drive_medical_data_JustinYoon.xlsx', sheet_name = 1)


plants = df.groupby('Plant').sum().reset_index()

fig = go.Figure([go.Bar(x=plants['Plant'], y = plants['Value'],
                hovertext= ['Total Quantity: ' + str(i) for i in plants['Quantity']])]
               )
fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5, opacity=0.6)
fig.update_yaxes(showgrid=False, title ='')
fig.update_layout(title_text='Value of Plants ($)',
                  title_x = .5,     plot_bgcolor='rgba(0,0,0,0)')


pie_data = df['ABC'].value_counts().sort_index().reset_index()
what_to_pull = 'A'
pull_abc = [0,0,0,0,0]
pull_abc[pie_data[pie_data['index'] == what_to_pull].index[0]] = .1

fig2 = go.Figure(data=[go.Pie(labels=pie_data['index'],
                            values=pie_data['ABC'],
                     pull= pull_abc)])

colors = ['rgb(158,202,225)', 'mediumturquoise', 'lightyellow', 'lightgreen','black']

fig2.update_traces(hoverinfo='value+percent', textinfo='label', textfont_size=20,
                  marker=dict(colors=colors, line=dict(color='#000000', width=2)))
fig2.update_layout(title_text="Percentage of ABCDS Distribution",
                   title_x=.5, plot_bgcolor='rgba(0,0,0,0)')


pivot_table = df.groupby('Category').count()['PO Number'].sort_values(ascending=False)

fig3 = px.bar(pivot_table, title = '# of Orders by Category')
fig3.update_layout(title_text="Number of Orders by Category",title_x=.5, showlegend=False,
                   plot_bgcolor='rgba(0,0,0,0)')
fig3.update_yaxes(showgrid=False, title ='')
fig3.update_xaxes(title = '')

fig3.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5, opacity=0.6)




abc_plant = df.groupby(['ABC','Plant']).sum()
fig4 = go.Figure(data=[
    go.Bar(name='A', x=abc_plant.loc['A'].index, y=abc_plant.loc['A']['Value']
           ,marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)'),
    go.Bar(name='B', x=abc_plant.loc['B'].index, y=abc_plant.loc['B']['Value'],
          marker_color='mediumturquoise', marker_line_color='rgb(8,48,107)'),
    go.Bar(name='C', x=abc_plant.loc['C'].index, y=abc_plant.loc['C']['Value'],
          marker_color='lightyellow', marker_line_color='rgb(8,48,107)'),
    go.Bar(name='D', x=abc_plant.loc['D'].index, y=abc_plant.loc['D']['Value'],
          marker_color='lightgreen',marker_line_color='rgb(8,48,107)'),
    go.Bar(name='S', x=abc_plant.loc['S'].index, y=abc_plant.loc['S']['Value'],
          marker_color='black', marker_line_color='rgb(8,48,107)')

])
# Change the bar mode
fig4.update_layout(barmode='group', title_text='Value of ABCS and Plants ($)'
                    , title_x=.5, plot_bgcolor='rgba(0,0,0,0)')
fig4.update_yaxes(showgrid=False, title ='')
fig4.update_xaxes(title = '')
