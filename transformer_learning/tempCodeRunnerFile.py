token_ids = tokenizer(sentence).input_ids
# print(token_ids)  # Output: [101, 7592, 2088, 999, 102]

# for token_id in token_ids:
#     print(tokenizer.decode(token_id))  # Output: [CLS] hello world! [SEP]