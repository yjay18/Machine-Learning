def describe_dataset(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    words = text.split()
    vocab = set(words) #using set function to get unique words
    return {
        "File": file_path,
        "Total words": len(words),
        "Vocabulary Size": len(vocab)
    }

datasets = [
    "input_childSpeech_trainingSet.txt",
    "input_childSpeech_testSet.txt",
    "input_shakespeare.txt"
]

for dataset in datasets:
    description = describe_dataset(dataset)
    print(description)
