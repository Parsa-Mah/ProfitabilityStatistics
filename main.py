from csv import reader

### The Google Play data set ###
opened_file = open('googleplaystore.csv')
read_file = reader(opened_file)
android = list(read_file)
android_header = android[0]
android = android[1:]

### The App Store data set ###
opened_file = open('AppleStore.csv')
read_file = reader(opened_file)
ios = list(read_file)
ios_header = ios[0]
ios = ios[1:]


def explore_data(dataset, start, end, rows_and_columns=False):
    dataset_slice = dataset[start:end]
    for row in dataset_slice:
        print(row)
        print('\n')  # adds a new (empty) line between rows

    if rows_and_columns:
        print('Number of rows:', len(dataset))
        print('Number of columns:', len(dataset[0]))


print(android_header)
print('\n')
explore_data(android, 10472, 10473, False)

print(ios_header)
print('\n')
explore_data(ios, 0, 3, True)

print(android[10472])  # incorrect row
print('\n')
print(android_header)  # header
print('\n')
print(android[0])      # correct row

print(len(android))
del android[10472]  # don't run this more than once
print(len(android))

for app in android:
    name = app[0]
    if name == 'Instagram':
        print(app)

duplicate_apps = []
unique_apps = []

for app in android:
    name = app[0]
    if name in unique_apps:
        duplicate_apps.append(name)
    else:
        unique_apps.append(name)

print('Number of duplicate apps:', len(duplicate_apps))
print('\n')
print('Examples of duplicate apps:', duplicate_apps[:15])

reviews_max = {}
for app in android:
    name = app[0]
    n_reviews = float(app[3])
    if name in reviews_max and reviews_max[name] < n_reviews:
        reviews_max[name] = n_reviews
    elif name not in reviews_max:
        reviews_max[name] = n_reviews

print('Expected length:', len(android) - 1181)
print('Actual length:', len(reviews_max))

android_clean = []
already_added = []

for app in android:
    name = app[0]
    n_reviews = float(app[3])
    if n_reviews == reviews_max[name] and name not in already_added:
        android_clean.append(app)
        already_added.append(name)

explore_data(android_clean, 0, 3, True)

def is_app_english(app_name: str):
    for char in app_name:
        if ord(char) > 127:
            return False
    return True

print(is_app_english('Instagram'))
print(is_app_english('爱奇艺PPS -《欢乐颂2》电视剧热播'))
print(is_app_english('Docs To Go™ Free Office Suite'))
print(is_app_english('Instachat 😜'))
