def rgb_to_hex(rgb):
    hex_code = '#{:02x}{:02x}{:02x}'.format(*rgb)
    return hex_code


# Usage example
rgb = (255, 170, 80) # <-- rgb(255, 170, 80)
hex = rgb_to_hex(rgb)
print(hex)
