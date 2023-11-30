import json

# train/metadata.jsonl
metadata = []
for i in range(70):
    file_name = f"{str(i).zfill(3)}.png"
    additional_feature = "A photo of Donald Trump"
    entry = {
        "file_name": file_name,
        "additional_feature": additional_feature
    }
    metadata.append(entry)
with open("DonaldTrump80/train/metadata.jsonl", "w") as file:
    for entry in metadata:
        file.write(json.dumps(entry) + "\n")

# test/metadata.jsonl
metadata = []
for i in range(10):
    file_name = f"{str(i+70).zfill(3)}.png"
    additional_feature = "A photo of Donald Trump"
    entry = {
        "file_name": file_name,
        "additional_feature": additional_feature
    }
    metadata.append(entry)
with open("DonaldTrump80/test/metadata.jsonl", "w") as file:
    for entry in metadata:
        file.write(json.dumps(entry) + "\n")