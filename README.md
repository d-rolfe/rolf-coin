# rolf-coin
a simple python implementation of a crypto-currency
==========================================================================================================================================
Implementation Notes
==========================================================================================================================================
- graph of transactions between users = ledger
- how to trust each trans? use digital signatures
- use public/secret key crypto: pk/sk
- Sign(Message, sk) = Signature
- note: Message = orig_message + message_id (so signature is unique, prevent copy fraud)
- message input means the signature changes based on message
- sk input means only sender could have sent it
- Verify(Message, Signature, pk) = T/F

- centralized vs decentralized:
- how does everyone keep track of the current ledger?
- centralized: broadcast each transaction to everyone (bad)
- decentralized: use which ever ledge has the most computational work (bitcoin)
- Proof of Work: a special number that if put in a hash, will make the first 'x' digits 0
- divide ledger into blocks, each block has a POW. (list of transactions in block (and prev hash, see below) and the POW are input to hash)
- each block contains prev hash in its header and link the blocks = block chain

- anyone can create a block, by listening to transactions, collect them into a block, and finding a POW, then broadcast out that block = mining coins
- a miner is rewarded with some coins placed as a special transaction at the top of the block
- new money added

