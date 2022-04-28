from sdk.components import (Badge, Button, Col, Column, Container, Datatable, Div, Form,
                            Icon, Row, Select, Span, collection, commify, documents,
                            format_currency, format_template, is_busy, switch_case)


def page():
    return Container(
        children=[
            title_row(),
            table_row()
        ]
    )


def title_row():
    return Row(
        children=[
            Col(
                children=[Icon("box")],
                class_name='col-auto pr-0'
            ),
            Col(
                children=[
                    Span("Fusion Cost Calculator", "font-medium-3")
                ]
            )
        ],
        class_name="mb-2"
    )


def table_row():
    return Datatable(
        class_name="mt-1",
        data=documents('fusioncalcs'),
        busy_when=is_busy(collection('fusioncalcs')),
        show_export=False,
        columns=[
            Column(
                id="rarity",
                width="130px",
                cell=rarity_cell(),
            ),
            Column(
                id="fusionMaterials",
                cell=materials_cell(),
                min_width="160px"
            ),
            Column(
                id="normal",
                value='$.calcs.normal.total_cost',
                title="Normal Box",
                cell=cost_cell("normal"),
                right=True,
                width="160px"
            ),
            Column(
                id="premium",
                value='$.calcs.premium.total_cost',
                title="Premium Box",
                cell=cost_cell("premium"),
                right=True,
                width="160px"
            ),
            Column(
                id="ultra",
                value='$.calcs.ultra.total_cost',
                title="Ultra Box",
                cell=cost_cell("ultra"),
                right=True,
                width="160px"
            ),
            Column(
                id="spacer",
                title="",
                width="10px"
            )
        ]
    )


def rarity_cell():
    return Row(
        children=[
            Col(
                class_name="col-auto px-0",
                children=[
                    Div(
                        [],
                        style={
                            "backgroundColor": switch_case('$.rarity', {
                                'Rare': '#D1CCCC',
                                'Epic': '#65F44E',
                                'Legend': '#C13EFA',
                                'Mythic': '#EB9A29',
                                'Meta': '#E8483A',
                            }),
                            "width": 6,
                            "height": '100%',
                            "marginRight": '0.6rem',
                        }
                    )
                ],
            ),
            Col(
                class_name="col-auto px-0",
                children=[
                    Span("$.rarity", "font-small-5 font-weight-bold")
                ],
            ),
        ],
        class_name="mx-0")


def materials_cell():
    return Row(
        children=[
            Col(
                class_name="col-12 font-small-5 font-weight-bold",
                children=[Span("$.fusionMaterials")],
            ),
            Col(
                class_name="col-12 font-small-1",
                children=[
                    Span(
                        format_template(
                            "({{ commonsNeeded }} x Commons @ Lv 1)",
                            {
                                "commonsNeeded": commify("$.commonsNeeded")
                            }
                        )
                    )
                ],

            ),
        ])


def cost_cell(boxType):
    return Row([
        Col(
            class_name="col-12",
            children=[
                Badge(
                    f"$.calcs.{boxType}.color",
                    [
                        Span(
                            format_currency(
                                f"$.calcs.{boxType}.total_cost",
                                "$.fiatSymbol"
                            ),
                        )
                    ],
                    class_name="float-right"
                ),
            ],
        ),
        Col([
            Span(
                format_template(
                    "{{ boxes }} boxes @ {{ boxCost }}",
                    {
                        "boxes": commify(f"$.calcs.{boxType}.boxes"),
                        "boxCost": format_currency(f"$.calcs.{boxType}.cost", "$.fiatSymbol")
                    }
                ),
                "float-right font-small-2"
            )
        ], "col-12")
    ])


def box_type_form():
    return Form(
        name='fusionbox',
        schema={
            "type": "object",
            "properties": {
                "boxType": "string"
            },
            "default": {
                "boxType": "Normal"
            }
        },
        children=[
            Row(
                class_name="mt-2",
                children=[
                    Col(
                        class_name="col-12 col-md-auto",
                        children=[
                            Select(
                                label="Box Type",
                                name="boxType",
                                options=["Normal", "Premium", "Ultra"],
                                min_width=160
                            )
                        ]),
                    Col(
                        class_name="col-12 col-md-auto my-auto",
                        children=[
                            Button(
                                label="Update",
                                is_submit=True,
                                busyWhen=is_busy(
                                    collection('fusioncalcs')
                                ),
                            )
                        ])
                ])
        ]
    )
