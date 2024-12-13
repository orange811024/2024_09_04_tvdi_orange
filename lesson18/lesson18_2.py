from dash import Dash,html,dcc,callback,Input, Output,dash_table,_dash_renderer
import pandas as pd
import plotly.express as px
import dash_mantine_components as dmc
_dash_renderer._set_react_version("18.2.0")

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

app = Dash(__name__,external_stylesheets=dmc.styles.ALL)

#radio button要顯示的資料
radio_data = [['pop','人口'],['lifeExp','平均壽命'],['gdpPercap','人均gdp']]

#selected要的資料
selected_data = [{'value':value,'label':value} for value in df.country.unique()]

app.layout = dmc.MantineProvider(
    [
    
        dmc.Container(        
            dmc.Title(f"世界各國人口,壽命,gdp統計數字", order=2),
            fluid=True,
            ta='center',
            my=30  
        )
    ,
        dmc.Flex(
            [
                dmc.Stack(
                    [
                        #dcc.RadioItems(['pop','lifeExp','gdpPercap'],value='pop',inline=True,id='radio_item')
                        dmc.RadioGroup(
                            children=dmc.Group([dmc.Radio(l, value=k) for k, l in radio_data], my=10),
                            id="radio_item",
                            value="pop",
                            label="請選擇查詢的種類",
                            size="md",
                            mb=10,
                        )
        
                    , 
                        #dcc.Dropdown(df.country.unique(),value='Taiwan',id='dropdown-selection')
                        dmc.Select(
                            label="請選擇國家",
                            placeholder="請選擇1個",
                            id="dropdown-selection",
                            value="Taiwan",
                            data=selected_data,
                            w=200,
                            mb=10,
                        )
                    ],
                    
                )
            ,
                
                #dash_table.DataTable(data=[],page_size=10,id='datatable',columns=[])
                dmc.ScrollArea(
                    children=[],
                    h=300,
                    w='50%',
                    id='scrollarea'
                )

                
                

            ],
            direction={"base": "column", "sm": "row"},
            gap={"base": "sm", "sm": "lg"},
            justify={"base": "center"},
            

        )
    ,
    #dcc.Graph(id='graph-content')
        dmc.Container(
           dcc.Graph(id='graph-content') 
        )
    ]
)

#圖表顯示的事件
@callback(    
    Output('graph-content','figure'),
    Input('dropdown-selection','value'),
    Input('radio_item','value')
    
)
def update_graph(country_value,radio_value):
    dff = df[df.country == country_value]
    if radio_value == "pop":
        title = f'{country_value}:人口成長圖表'
    elif radio_value == "lifeExp":
        title = f'{country_value}:預期壽命'
    elif radio_value == 'gdpPercap':
        title = f'{country_value}:人均GDP'

    return px.line(dff,x='year',y=radio_value,title=title)

#表格顯示的事件
@callback(    
    Output('scrollarea','children'),    
    Input('dropdown-selection','value'),
    Input('radio_item','value') 
)
def update_table(country_value,radio_value):
    #只顯示台灣的資料,table所需要的資料
    dff = df[df.country == country_value]
    pop_diff = dff[['country', 'year', radio_value]]
    elements = pop_diff.to_dict('records')

    rows = [
        dmc.TableTr(
            [
                dmc.TableTd(element["country"]),
                dmc.TableTd(element["year"]),
                dmc.TableTd(element[radio_value]),
            ]
        )
        for element in elements
    ]

    if radio_value == 'pop':
        head_name = '人口'
    elif radio_value == 'lifeExp':
        head_name = '平均壽命'
    elif radio_value == 'gdpPercap':
        head_name = '人均GDP'

    head = dmc.TableThead(
        dmc.TableTr(
            [
                dmc.TableTh("國家"),
                dmc.TableTh("年份"),
                dmc.TableTh(head_name),
            ]
        )
    )

    body = dmc.TableTbody(rows)
    caption = dmc.TableCaption(f"Taiwan 年份,{head_name}")
    return dmc.Table([head, body, caption])

    

if __name__ == '__main__':
    app.run(debug=True)