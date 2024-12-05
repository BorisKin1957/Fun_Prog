def get_extensions(file_list):
    results = []

    def _get_extension(file_name):
        if '.' not in file_name:
            return ''
        return file_name.split('.')[-1]

    for file_name in file_list:
        results.append(_get_extension(file_name))
    return results


print(get_extensions(["foo.txt", "bar.mp4", "python3"]))
