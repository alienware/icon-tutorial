# Load our existing wallet 1
from iconsdk.wallet.wallet import KeyWallet

wallet1 = KeyWallet.load("./iconkeystore", "@icon111")
wallet2 = KeyWallet.load("./iconkeystore2", "@icon222")

# Build a transaction instance, hard-code it to send 1 ICX from wallet 1 to wallet 2
from iconsdk.builder.transaction_builder import (
    TransactionBuilder,
    DeployTransactionBuilder,
    CallTransactionBuilder,
    MessageTransactionBuilder
)
from iconsdk.signed_transaction import SignedTransaction

transaction = TransactionBuilder()\
    .from_(wallet1.get_address())\
    .to(wallet2.get_address())\
    .value(1000000000000000000)\
    .step_limit(2000000)\
    .nid(3)\
    .nonce(100)\
    .build()

from iconsdk.icon_service import IconService
from iconsdk.providers.http_provider import HTTPProvider
icon_service = IconService(HTTPProvider("https://bicon.net.solidwallet.io/api/v3"))

# Returns the signed transaction object having a signature
signed_transaction = SignedTransaction(transaction, wallet1)

# Sends the transaction
tx_hash = icon_service.send_transaction(signed_transaction)
