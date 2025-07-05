def hex_to_rgb(hex_color):
    # Remove the '#' if present
    if hex_color.startswith('#'):
        hex_color = hex_color[1:]

    # Ensure the hex string has 6 characters
    if len(hex_color) != 6:
        raise ValueError("Invalid hex color format. Expected 6 characters (e.g., 'RRGGBB').")

    # Extract R, G, and B components and convert to decimal
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)

    return (r, g, b)

# Example usage:
hex_code1 = "#FFA501"
rgb_value1 = hex_to_rgb(hex_code1)
print(f"Hex '{hex_code1}' converts to RGB: {rgb_value1}")

hex_code2 = "0080FF"
rgb_value2 = hex_to_rgb(hex_code2)
print(f"Hex '{hex_code2}' converts to RGB: {rgb_value2}")