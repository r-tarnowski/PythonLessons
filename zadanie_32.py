
def compare_element(element1, element2):
    result = -1
    for j in range(min(len(element1), len(element2))):
        if int(element1[j]) == int(element2[j]):
            result = -1
        elif int(element1[j]) > int(element2[j]):
            result = 0
            break
        else:
            result = 1
            break
    return result


def compare_versions(ver1, ver2):
    result = -1
    for i in range(min(len(ver1), len(ver2))):
        result = compare_element(ver1[i], ver2[i])
        if result != -1:
            break
    return result


versions = input().split(" ")
# print(versions)
version1 = versions[0].split(".")
version2 = versions[1].split(".")
# print(f"version 1: {version1}")
# print(f"version 2: {version2}")
comparison_result = compare_versions(version1, version2)
if comparison_result == -1:
    print("Versions are the same")
else:
    newer_version_index = comparison_result
    if newer_version_index == 0:
        older_version_index = 1
    else:
        older_version_index = 0
    print(f"Wersja {versions[newer_version_index]} jest nowsza niż wersja {versions[older_version_index]}")


