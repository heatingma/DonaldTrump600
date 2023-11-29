import json

# train/metadata.jsonl
metadata = []
for i in range(500):
    file_name = f"{str(i).zfill(3)}.png"
    additional_feature = "A photo of Donald Trump"
    entry = {
        "file_name": file_name,
        "additional_feature": additional_feature
    }
    metadata.append(entry)
with open("DonaldTrump600/train/metadata.jsonl", "w") as file:
    for entry in metadata:
        file.write(json.dumps(entry) + "\n")

# test/metadata.jsonl
metadata = []
for i in range(100):
    file_name = f"{str(i+500).zfill(3)}.png"
    additional_feature = "A photo of Donald Trump"
    entry = {
        "file_name": file_name,
        "additional_feature": additional_feature
    }
    metadata.append(entry)
with open("DonaldTrump600/test/metadata.jsonl", "w") as file:
    for entry in metadata:
        file.write(json.dumps(entry) + "\n")