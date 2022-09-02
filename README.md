# A Stunningly Shithouse DPI firewall

An quick and dirty payload-inspecting "DPI" firewall built as a demo/POC.

## Install

Create a Python 3.8.0 virtualenv (eg using pyenv).

Install system deps:
```
# eg RHEL9 and clones:
sudo dnf --enablerepo crb install libnetfilter_queue-devel
```

install Python deps:
```
pip3.8 install -r requirements.txt
```

## Usage

Setup a bog standard Linux SNAT/Masquerading gateway.

Create IPTables rule to send packets to this terrible DPI firewall:
```
iptables -I FORWARD -o <your_egress_interface> -j NFQUEUE --queue-num 1
```

Start the fiewall:
```
./dpifw.py armed
```
Omit the `armed` option to log only.

### Adding more filters:

Update the `BAD_PATTERNS` dictionary in `dpifw.py` with regex patterns matching payloads you want to block.
