import requests

def checkServerStatus(options):
    website_address = options["-site"]
    website_port = options["-port"]
    try:
        reply = requests.head(
            f"http://{website_address}:{website_port}"
        )
        print("res=" + str(reply.status_code))

    except requests.RequestException:
        print('Communication error')
        exit(3)

    else:
        print("Connection=" + reply.headers.get("Connection", "unknown"))
        print(f"HTTP/{reply.raw.version / 10:.1f} {reply.status_code} {reply.reason}")
        if reply.status_code == requests.codes.not_found:
            print("Resource not found")
        elif reply.status_code >= 500:
            print("Server error")
