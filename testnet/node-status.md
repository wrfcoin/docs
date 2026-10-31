# Node status: what each panel means

Your node serves its own dashboard at `http://127.0.0.1:8556/dashboard`. It is
in core4 main and in the Windows node preview 3 installer (v0.3.0), which opens
it from the Start menu. A Docker node serves it once its locally built image
includes it. Open it on the computer running your node: `127.0.0.1` refers to
the computer where your browser is running.

From a terminal you can also read the local chain summary:

```bash
curl -s localhost:8556/network/info | jq
```

This command requires `curl` and `jq`. See the
[node quickstart](quickstart.md#6-running-a-node) and
[software availability](downloads.md) for setup and platform status.

## Chain panel — no operator token required

| Value | What it means |
| --- | --- |
| Height | The latest block height known to your node. Watch successive readings for progress; one height alone cannot establish that you have caught up. |
| Sync state | The node's report of whether it is catching up or synced. Check it together with height and peers. |
| Peers | Connected network peers. Zero means the node currently has no peers; a positive count alone does not prove successful synchronization. |
| Genesis | The identity of the chain's first block. Compare the full hash with the current join instructions; a shortened display is only a convenience. |
| Protocol | The protocol version reported by your node. It is distinct from the software release version. |
| Blocks per minute | The observed change in height across successive samples, expressed per minute. It needs more than one sample and can rise during catch-up; it is not a promised block-production rate. |

A blank or unavailable value is not zero. If the page cannot fetch data, check
its message and the time of the last successful update before drawing a
conclusion. A chain identity mismatch needs operator help before continuing.

## Host panel — operator token required

The host panel requires the node's **operator token**. The backing
`GET /node/metrics/host` endpoint protects host telemetry. Without authorization,
expect a **token required** state rather than CPU, memory, swap or disk values.
Public chain and node panels do not need this token.

| Value | What it means |
| --- | --- |
| CPU | Average processor use and use per logical core. A brief spike can occur during startup or catch-up; watch the trend. |
| Memory | RAM in use and available. These are host measurements, not solely the node process's memory. |
| Swap | Disk-backed memory currently in use. Sustained growth can indicate memory pressure; zero swap capacity can simply mean none is configured. |
| Disk | Capacity, use and free space for each reported mount. Check the mount that holds node data, rather than assuming every mount is the same disk. |

### Getting and protecting the operator token

The current `infra/testnet/join.sh` and `join-testnet-sync-node.sh` do **not**
print an operator token. Their final successful output is headed
**Node is up. Chain identity / sync status:**, followed by chain identity,
synchronization and log guidance. There is currently no token line in that
summary to copy; token provisioning and a safe handoff remain an operator setup
dependency. Ask the operator who configured your node for the approved private
handoff. Do not use a wallet key or recovery phrase as a substitute.

On Windows, the Start-menu entry hands the token to the page in the address-bar
fragment (after `#`), which browsers never send to the server; the page moves it
to the tab's session storage and clears the address bar. Otherwise, paste it into
the dashboard's token field. The page sends it only in an authorization header. Do not put tokens in bookmarks, commands, logs, screenshots,
public issues or shared screen recordings. Do not expose the local API publicly
to make the page accessible from another computer.

## Node panel and freshness — no operator token required

- **Version:** the software version reported by the node. Include it when asking
  for help; it is distinct from the protocol version.
- **Role:** what this node is configured to do. A sync-only node follows the
  chain and serves its local API; it does not produce blocks.
- **Uptime:** how long the current node process has been running, not the age of
  the chain or proof of uninterrupted synchronization.
- **Data as of:** when the displayed data was last refreshed successfully.
  The page refreshes every ten seconds. An old timestamp means the
  screen may be stale; it does not prove the node has stopped.

## Metrics and help

Prometheus users can scrape `GET /metrics` on their node's local API, subject to
its configured access controls. Prometheus metrics and the browser status page
are separate ways to inspect the node.

For a problem, use [testnet support](https://github.com/wrfcoin/testnet-support/issues/new/choose).
Share your OS/platform, software version, the relevant join-summary lines and
local chain-summary output **after checking and redacting private details**.
A cropped dashboard screenshot can help, but omit the token field,
private host details and personal paths. Never post configuration or environment
files. Report suspected vulnerabilities privately to **security@wrfcoin.com**.
