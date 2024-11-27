need steamlit app

to select features

cat_features = [
    "cap-shape",
    "cap-color",
    "does-bruise-or-bleed",
    "gill-color",
    "stem-color",
    "has-ring",
    "habitat",
    "season",
]
num_features = [
    "cap-diameter",
    "stem-height",
    "stem-width",
]

and predict the "name" of the mushroom. should have three colums. left: input fields, mid: image (src/services/Images ), right: lookup of features of fungi ([text](../data/raw/primary_data_edited.csv), [text](../data/raw/primary_data_meta.txt))