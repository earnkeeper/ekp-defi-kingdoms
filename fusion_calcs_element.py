from components import (Col, Column, Container, Datatable, Icon, Row, Span,
                        documents)


def fusionCalcsElement():
    return Container(
        children=[
            Row([
                Col([
                    Icon("box"),
                ], 'col-auto'),
                Col([
                    Span("Hero Box", "font-medium-3")
                ])
            ]),
            Datatable(
                className="mt-1",
                data=documents('fusioncalcs'),
                columns=[
                    Column("rarity"),
                    Column("fusionMaterials"),
                    Column("commonsNeeded"),
                    Column("boxesNeeded"),
                    Column("totalCost"),
                ]
            )
        ]
    )
