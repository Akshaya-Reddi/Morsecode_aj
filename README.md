# Morse Code Translator

## Overview

The Morse Code Translator is a Python script that allows you to convert text to Morse code and Morse code back to text. It also includes a feature to produce audible beeps corresponding to the Morse code signals, which can help in learning and practicing Morse code.

## Features

- **Text to Morse Code Conversion**: Convert any English text into its corresponding Morse code representation.
- **Morse Code to Text Conversion**: Decode any Morse code back into English text.
- **Audible Morse Code**: Play the Morse code as beeps using the computer's speakers.

## Requirements

- Python 3.x
- Windows OS (for `winsound` module to work)

## Installation

You can install the Morse Code Translator via pip:

\`\`\`sh
pip install morsecode_aj
\`\`\`

## Usage

1. Clone the repository:
   \`\`\`sh
   git clone https://github.com/yourusername/morsecode_aj.git
   cd morsecode_aj
   \`\`\`

2. Run the script:
   \`\`\`sh
   python MC.py
   \`\`\`

3. Follow the on-screen instructions to encode or decode Morse code.

## Example

### Encoding Text to Morse Code:
\`\`\`plaintext
Do you want to encode or decode Morse code? (e/d): e
Enter the text to encode: Hello World
Morse Code: .... . .-.. .-.. --- / .-- --- .-. .-.. -..
\`\`\`

### Decoding Morse Code to Text:
\`\`\`plaintext
Do you want to encode or decode Morse code? (e/d): d
Enter the Morse code to decode: .... . .-.. .-.. --- / .-- --- .-. .-.. -..
Decoded Text: HELLO WORLD
\`\`\`

### Playing Morse Code Beeps:
After encoding or decoding, the script will play the Morse code beeps corresponding to the text or Morse code provided.

## License

This project is licensed under the MIT License. See the ithub.com/Akshaya-Reddi/Morsecode_aj/blob/main/LICENSE file for details.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss your changes.

## Author

Akshaya Reddy Anna Reddy
https://github.com/Akshaya-Reddi/Morsecode_aj
