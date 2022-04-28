from sdk.components import (Badge, Button, Col, Column, Container, Datatable, Form,
                            Icon, Row, Select, Span, collection, commify, documents,
                            format_currency, format_template, is_busy)


def page():
    return Container(
        children=[
            Row(
                [
                    Col([
                        Icon("box"),
                    ], 'col-auto pr-0'),
                    Col([
                        Span("Fusion Cost Calculator", "font-medium-3")
                    ])
                ],
                "mb-2"
            ),
            Datatable(
                class_name="mt-1",
                data=documents('fusioncalcs'),
                busy_when=is_busy(collection('fusioncalcs')),
                show_export=False,
                columns=[
                    Column(
                        id="rarity",
                        width="160px",
                        cell=Row([
                            Col(
                                [
                                    Span("$.rarity")
                                ],
                                "col-12"
                            ),
                            Col(
                                [
                                    Span(" ")
                                ],
                                "col-12"
                            )
                        ])
                    ),
                    Column(
                        id="fusionMaterials",
                        cell=Row([
                            Col(
                                [Span("$.fusionMaterials")],
                                "col-12"
                            ),
                            Col(
                                [Span(
                                    format_template(
                                        "({{ commonsNeeded }} x Common @ Lv 1)",
                                        {
                                            "commonsNeeded": commify("$.commonsNeeded")
                                        }
                                    )
                                )],
                                "col-12 font-small-2"
                            ),

                        ])
                    ),
                    Column(
                        id="normalTotalCost",
                        title="Normal Box",
                        cell=box_cost_cell("normal"),
                        right=True,
                        width="160px"
                    ),
                    Column(
                        id="premiumTotalCost",
                        title="Premium Box",
                        cell=box_cost_cell("premium"),
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
        ]
    )


def box_cost_cell(boxType):
    return Row([
        Col([
            Badge(
                f"$.{boxType}Color",
                [
                    Span(
                        format_currency(
                            f"$.{boxType}TotalCost",
                            "$.fiatSymbol"
                        ),
                    )
                ],
                class_name="float-right"
            ),
        ], "col-12"),
        Col([
            Span(
                format_template(
                    "{{ boxes }} boxes @ {{ boxCost }}",
                    {
                        "boxes": commify(f"$.{boxType}Boxes"),
                        "boxCost": format_currency(f"$.{boxType}Cost", "$.fiatSymbol")
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
