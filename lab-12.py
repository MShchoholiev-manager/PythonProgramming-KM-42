dirs = [
    ( 'folder1',
        [
            'file1',
            ( 'folder2', 
                [
                    'file2',
                    'file3'
                ] 
            ),
            ( 'folder3', 
                [
                    'file3', 
                    'file4',
                    ('folder4', ['file3'])
                ] 
            ),
            'file5'
        ]
    )
]

# ВАШ КОД ТУТ

def search(dirs, filename, path = ""):
    result = []
    for item in dirs:
        if isinstance(item, str):
            if item == filename:
                result.append(path + "/" + item)
        elif isinstance(item, tuple):
            folder_name, subdirs = item
            result.extend(search(subdirs, filename, path + "/" + folder_name))
    return result
    
# ПЕРЕВІРКА

print(search(dirs, 'file1'))
print(search(dirs, 'file2'))
print(search(dirs, 'file3'))
print(search(dirs, 'file4'))
print(search(dirs, 'file5'))
print(search(dirs, 'file6'))
print(search(dirs, 'folder1'))

assert search(dirs, 'file1') == ['/folder1/file1'], 'Failed test for file1'
assert search(dirs, 'file2') == ['/folder1/folder2/file2'], 'Failed test for file2'
assert search(dirs, 'file3') == ['/folder1/folder2/file3', '/folder1/folder3/file3', '/folder1/folder3/folder4/file3'], 'Failed test for file3'
assert search(dirs, 'file4') == ['/folder1/folder3/file4'], 'Failed test for file4'
assert search(dirs, 'file5') == ['/folder1/file5'], 'Failed test for file5'
assert search(dirs, 'file6') == [], 'Failed test for file6'
assert search(dirs, 'folder1') == [], 'Failed test for folder1'
print('All tests good!')
# assert search(dirs, 'file1') == ['/folder1/file1'], 'Failed test for file1'
# assert search(dirs, 'file2') == ['/folder1//folder2/file2'], 'Failed test for file2'
# assert search(dirs, 'file3') == ['/folder1//folder2/file3', '/folder1//folder3/file3', '/folder1//folder3//folder4/file3'], 'Failed test for file3'
# assert search(dirs, 'file4') == ['/folder1//folder3/file4'], 'Failed test for file4'
# assert search(dirs, 'file5') == ['/folder1/file5'], 'Failed test for file5'
# assert search(dirs, 'file6') == [], 'Failed test for file6'
# assert search(dirs, 'folder1') == [], 'Failed test for folder1'
# print('All tests good!')