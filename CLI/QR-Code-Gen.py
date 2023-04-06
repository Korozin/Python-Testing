import requests, qrcode, urllib, time, sys

def format_link(link):
    # check if link starts with http:// or https://
    parsed = urllib.parse.urlparse(link)
    if parsed.scheme == "":
        # Determine the URL scheme by making a request to the URL
        try:
            response = requests.get("https://" + link)
            if response.status_code == 200:
                link = "https://" + link
            else:
                link = "http://" + link
        except requests.exceptions.RequestException:
            link = "http://" + link
    return link

def main(link):
    # Format link if necessary
    link = format_link(link)

    # Generate QR code image
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Save QR code as PNG file with timestamp
    timestamp = int(time.time())
    filename = f"qr_code_{timestamp}.png"
    img.save(filename)
    print(f"QR Code for {link} generated successfully as {filename}.")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(f"Usage: {sys.argv[0]} <link>")
        sys.exit(1)
    else:
        main(sys.argv[1])
