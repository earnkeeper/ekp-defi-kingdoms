import requests
from features.fusion_calcs.documents import documents
from features.fusion_calcs.page import page
from sdk.coingecko import latest_price
from sdk.components import  selected_currency
from sdk.sockets import emit_busy, emit_documents, emit_done, emit_menu, emit_page


def on_client_state_changed(sio, sid, event):
    emit_busy(sio, sid, "fusioncalcs")
    emit_menu(sio, sid, 'herobox', 'Fusion Costs', 'fusioncosts', 'cil-calculator')
    emit_page(sio, sid, "fusioncosts", page())

    currency = selected_currency(event)
    rate = latest_price("usd-coin", currency["id"])

    docs = documents(rate, currency["symbol"])

    emit_documents(sio, sid, "fusioncalcs", docs)
    emit_done(sio, sid, "fusioncalcs")
