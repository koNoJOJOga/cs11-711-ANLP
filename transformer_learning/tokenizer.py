from transformers import AutoTokenizer

# Load the BERT tokenizer
sentence = "Hello world!"
tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")

token_ids = tokenizer(sentence).input_ids
print(token_ids)  # Output: [101, 7592, 2088, 999, 102]

for token_id in token_ids:
    print(tokenizer.decode(token_id))  # Output: [CLS] hello world! [SEP]

# A list of colors in RGB
colors = [
    '102;194;165', '252;141;98', '141;160;203', 
    '231;138;195', '166;216;84', '255;217;47'
]

def show_tokens(sentence: str, name: str):
    """Show the tokens each separated by color."""

    # Load the tokenizer and tokenize the input
    tokenizer = AutoTokenizer.from_pretrained(
        name
    )
    token_ids = tokenizer(sentence).input_ids

    # Extract vocabulary length
    print(f"Vocab length: {len(tokenizer)}")

    # print a colored list of tokens
    for idx, t in enumerate(token_ids):
        print(
            f'\x1b[0;30;48;2;' +
            f'{colors[idx % len(colors)]}m' +
            tokenizer.decode(t) +
            '\x1b[0m',
            end=' '
        )

show_tokens("Hello world!", "bert-base-cased")
