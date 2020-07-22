# Network Connection Monitor
A Python program that alerts you via an LED or a status message when the connection to the Internet goes down.

## Installation
Clone this repository, then install the dependencies with `pip` or `pip3` (`pip install -r requirements.txt` or `pip3 install -r requirements.txt`).

## Configuration
In the `config.json` file, add the sites you want to be tested against in the `sites` section.

By default, the homepages of [Google](https://www.google.com), [Bing](https://www.bing.com), [GitHub](https://github.com), and [Apple](https://www.apple.com) are used to conduct the HEAD requests for testing web connectivity. The DNS servers of [Cloudflare](https://1.1.1.1/) (1.1.1.1, 1.0.0.1) and [Google](https://developers.google.com/speed/public-dns) (8.8.8.8, 8.8.4.4) are used for pings.

```json
{
    "timeout": 5, <-- The timeout in seconds
    "packet_count": 2, <-- The amount of packets to send when sending a ping request
    "public_ip": { <-- Configuration regarding the public IP
        "print": true, <-- Whether to/to not print the public IP (if possible) by using [Ipify][0]
        "server": "https://api.ipify.org?format=json", <-- The server to use to fetch the public IP, which must return a JSON response
        "json_key": "ip" <-- The root-level JSON key that the IP is stored in
    },
    "head_requests": true, <-- Whether to/to not run the HEAD requests
    "ping_requests": true, <-- Whether to/to not run the ping requests
    "sites": { <-- A list of the sites to conduct HEAD requests on
        "Apple": "https://www.apple.com",
        "Bing": "https://www.bing.com",
        "GitHub": "https://github.com",
        "Google": "https://www.google.com"
    },
    "ping_servers": { <-- A list of servers to ping
        "Cloudflare DNS A": "1.1.1.1",
        "Cloudflare DNS B": "1.0.0.1",
        "Google Public DNS A": "8.8.8.8",
        "Google Public DNS B": "8.8.4.4"
    }
}
```

<small>Please note that this program was designed for use on macOS and Linux systems and may not work out-of-the-box in Windows systems. If you make modifications that allow this to be used on any platform, please make a pull request.</small>

[0]: https://ipify.org