from sdk.components import (Badge, Button, Col, Column, Container, Datatable,
                            Div, Form, Icon, Row, Select, Span, collection,
                            commify, documents, format_currency,
                            format_template, is_busy, switch_case)


def page():
    return Container(
        children=[
            title_row(),
            Span(content="The Metabomb Initial NFT Offering event starts at 1pm UTC - 30 Apr '22. Check your total costs below before buying!"),
            table_row()
        ]
    )


def title_row():
    return Row(
        children=[
            Col(
                children=[Icon("sunset")],
                class_name='col-auto pr-0'
            ),
            Col(
                children=[
                    Span("Initial NFT Offering Event", "font-medium-3")
                ]
            )
        ],
        class_name="mb-2"
    )


def table_row():
    return Datatable(
        class_name="mt-3",
        data=documents('nft-event'),
        busy_when=is_busy(collection('nft-event')),
        pagination=False,
        show_export=False,
        columns=[
            Column(
                id="box",
                width="130px",
            ),
            Column(
                id="quantity",
                title="Qty Available",
                min_width="160px",
                right=True,
                format=commify("$.quantity")
            ),
            Column(
                id="staking",
                title="Stake MTB",
                width="160px",
                right=True,
                format=format_template("{{ mtb }} ea.", {
                    "mtb": commify("$.staking")
                })
            ),

            Column(
                id="stakeCost",
                title="Stake Cost",
                right=True,
                width="160px",
                format=format_template(
                    "{{ cost }} ea.",
                    {
                        "cost": format_currency("$.stakeCost", "$.fiatSymbol"),
                    }
                )
            ),
            Column(
                id="cost",
                title="Purchase Cost",
                right=True,
                width="160px",
                format=format_template(
                    "{{ symbol }} {{ cost }} ea.",
                    {
                        "symbol": "$.fiatSymbol", "cost": "$.cost"
                    }
                )
            ),
            Column(
                id="totalCost",
                title="Total Cost",
                right=True,
                width="160px",
                format=format_template(
                    "{{ cost }} ea.",
                    {
                        "cost": format_currency("$.totalCost", "$.fiatSymbol"),
                    }
                )
            ),
            Column(
                id="limit",
                title="Per Wallet",
                right=True,
                width="160px"
            ),

        ]
    )
