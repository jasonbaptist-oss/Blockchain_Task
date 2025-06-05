Minimal Blockchain created using python

Block Structure
Each block contains:
- `index`: Position in the blockchain
- `timestamp`: Creation time
- `data`: Payload (e.g. string)
- `previous_hash`: SHA-256 hash of the previous block
- `nonce`: Proof-of-Work counter
- `hash`: SHA-256 over index + timestamp + data + previous_hash + nonce

Validation Logic
The `Blockchain` class has a method `is_valid()` that checks:
- Each block's hash matches its contents (recomputed)
- Each block's `previous_hash` matches the actual hash of the previous block
- (Bonus) The hash begins with two leading zeros (`00`) to satisfy Proof-of-Work

Proof-of-Work
Implemented by:
- Incrementing the `nonce` until the hash starts with two zeros
- This prevents instant block creation and simulates consensus effort
