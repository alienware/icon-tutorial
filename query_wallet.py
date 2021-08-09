from iconsdk.icon_service import IconService
from iconsdk.providers.http_provider import HTTPProvider

icon_service = IconService(HTTPProvider("https://bicon.net.solidwallet.io/api/v3"))
balance1 = icon_service.get_balance('hx3dc783fcd007e41ccbbe1dd9f83372a8b3e98225')
print('wallet1', balance1)
balance2 = icon_service.get_balance('hx6cb8aa49d0609e164ac7bcefc8209bdf24dd6427')
print('wallet2', balance2)
