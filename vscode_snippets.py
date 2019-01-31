import json
import pathlib
import collections


class Snippet:
    def __init__(self, file):
        self.imports = []
        self.libs = []
        with open(file, 'r', encoding="utf-8") as f:
            is_lib = False
            for s in f:
                s = s.rstrip('\n')
                if s.startswith("import") or s.startswith("from"):
                    self.imports.append(s)
                if s.startswith("def") or s.startswith("class"):
                    is_lib = True
                    self.libs.append([])
                if is_lib and s == '':
                    is_lib = False
                if is_lib:
                    self.libs[-1].append(s)

    def toJson(self):
        self.json = collections.OrderedDict()
        for lib in self.libs:
            snippet = collections.OrderedDict()
            if lib[0].startswith("def"):
                prefix = lib[0].replace("def ", '').rstrip(":")
            elif lib[0].startswith("class"):
                prefix = lib[0].replace("class ", '').rstrip(":")
            snippet["prefix"] = prefix
            snippet["body"] = self.imports + lib
            self.json[prefix] = snippet
        return self.json


def main():
    path = pathlib.Path("src/")
    json_data = []
    for p in path.glob("*.py"):
        json_data.append(Snippet(p).toJson())
    with open("python.json", 'w') as f:
        json.dump(json_data, f, indent=4)


if __name__ == "__main__":
    main()
