from colored import fg, attr
import time
import signal
import sys

# Hex colors in order
colors = ['#00a7de', '#01a5dd', '#02a3dc', '#03a1db', '#049fda', '#059dd8', '#059bd7', '#0699d6', '#0798d5', '#0896d3', '#0994d2', '#0a92d1', '#0a90d0', '#0b8ecf', '#0c8ccd', '#0d8acc', '#0e88cb', '#0f86ca', '#0f84c8', '#1082c7', '#1180c6', '#127ec5', '#137cc4', '#147bc2', '#1479c1', '#1577c0', '#1675bf', '#1773be', '#1871bc', '#196fbb', '#196dba', '#1a6bb9', '#1b69b7', '#1c67b6', '#1d65b5', '#1e63b4', '#1e61b3', '#1f5fb1', '#205eb0', '#215caf', '#225aae', '#2358ad', '#2356ab', '#2454aa', '#2552a9', '#2650a8', '#274ea6', '#284ca5', '#284aa4', '#2948a3', '#2a46a2', '#2b44a0', '#2c429f', '#2d419e', '#2d3f9d', '#2e3d9b', '#2f3b9a', '#303999', '#313798', '#323597', '#333496', '#363396', '#383395', '#3b3295', '#3d3295', '#403195', '#423194', '#453094', '#483094', '#4a2f94', '#4d2f94', '#4f2e93', '#522e93', '#542d93', '#572d93', '#592c92', '#5c2c92', '#5e2b92', '#612b92', '#632a91', '#662a91', '#682991', '#6b2991', '#6e2891', '#702890', '#732790', '#752790', '#782690', '#7a268f', '#7d258f', '#7f258f', '#82248f', '#84248e', '#87238e', '#89238e', '#8c228e', '#8e228d', '#91218d', '#94218d', '#96208d', '#99208d', '#9b1f8c', '#9e1f8c', '#a01e8c', '#a31e8c', '#a51d8b', '#a81d8b', '#aa1c8b', '#ad1c8b', '#af1b8a', '#b21b8a', '#b41a8a', '#b71a8a', '#ba198a', '#bc1989', '#bf1889', '#c11889', '#c41789', '#c61788', '#c91688', '#ca1687', '#cb1786', '#cb1784', '#cc1783', '#cc1881', '#cd1880', '#ce197e', '#ce197d', '#cf197b', '#cf1a7a', '#d01a78', '#d01b77', '#d11b75', '#d11b74', '#d21c72', '#d31c71', '#d31d6f', '#d41d6e', '#d41d6c', '#d51e6b', '#d51e69', '#d61f68', '#d61f66', '#d71f65', '#d72063', '#d82062', '#d92160', '#d9215f', '#da215d', '#da225c', '#db225a', '#db2359', '#dc2357', '#dc2356', '#dd2454', '#de2453', '#de2551', '#df2550', '#df254e', '#e0264d', '#e0264b', '#e1274a', '#e12748', '#e22747', '#e22845', '#e32844', '#e42942', '#e42941', '#e5293f', '#e52a3e', '#e62a3c', '#e62b3b', '#e72b39', '#e72b38', '#e82c36', '#e92c35', '#e92d33', '#ea2d32', '#ea2d30', '#eb2e2f', '#eb302e', '#eb332e', '#ec362e', '#ec392e', '#ec3c2e', '#ed3f2e', '#ed422e', '#ed452e', '#ee482e', '#ee4c2e', '#ee4f2e', '#ee522e', '#ef552e', '#ef582e', '#ef5b2e', '#f05e2e', '#f0612e', '#f0652e', '#f1682e', '#f16b2e', '#f16e2e', '#f1712e', '#f2742e', '#f2772e', '#f27a2e', '#f37d2e', '#f3812e', '#f3842e', '#f4872e', '#f48a2e', '#f48d2d', '#f4902d', '#f5932d', '#f5962d', '#f59a2d', '#f69d2d', '#f6a02d', '#f6a32d', '#f7a62d', '#f7a92d', '#f7ac2d', '#f7af2d', '#f8b22d', '#f8b62d', '#f8b92d', '#f9bc2d', '#f9bf2d', '#f9c22d', '#fac52d', '#fac82d', '#facb2d', '#facf2d', '#fbd22d', '#fbd52d', '#fbd82d', '#fcdb2d', '#fcde2d', '#fce12d', '#fde42d', '#fde72d', '#fbe82d', '#f7e72e', '#f2e62f', '#eee52f', '#eae330', '#e6e231', '#e2e131', '#dde032', '#d9de33', '#d5dd33', '#d1dc34', '#cddb34', '#c8d935', '#c4d836', '#c0d736', '#bcd637', '#b7d438', '#b3d338', '#afd239', '#abd13a', '#a7cf3a', '#a2ce3b', '#9ecd3c', '#9acc3c', '#96ca3d', '#91c93e', '#8dc83e', '#89c73f', '#85c540', '#81c440', '#7cc341', '#78c241', '#74c042', '#70bf43', '#6cbe43', '#67bd44', '#63bb45', '#5fba45', '#5bb946', '#56b847', '#52b647', '#4eb548', '#4ab449', '#46b349', '#41b14a', '#3db04b', '#39af4b', '#35ae4c', '#30ac4d', '#2cab4d', '#28aa4e', '#24a94e', '#20a74f', '#1ba650', '#17a550', '#13a451', '#0fa252', '#0ba152', '#06a053', '#029f54']

# Convert hex codes to colored text
colored_text = [fg(color) for color in colors]

# Set initial color index and direction
color_index = 0
direction = 1

# Define signal handler for Ctrl+C
def signal_handler(sig, frame):
    print("\r" + "Exited", end="", flush=True)
    sys.exit(0)

# Set signal handler for Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

# Loop infinitely
while True:
    # Create empty string for rainbow text
    rainbow_text = ""
    
    # Text set to be rainbow-ified
    rainbow_set_text = "Hello! UwU"
    
    # Loop through each letter in rainbow_set_text
    for i in range(len(rainbow_set_text)):
        # Calculate color index based on position and direction
        color_index_offset = i * direction
        color_index_actual = (color_index + color_index_offset) % len(colors)
        
        # Add colored letter to rainbow text
        rainbow_text += colored_text[color_index_actual] + rainbow_set_text[i] + attr('reset')
    
    # Print rainbow text without newline character
    print("\r" + rainbow_text, end="", flush=True)
    
    # Increment color index and direction
    color_index = (color_index + 1) % len(colors)
    if color_index == 0:
        direction = -1
    
    # Wait for a short time before printing next iteration
    time.sleep(0.01)
