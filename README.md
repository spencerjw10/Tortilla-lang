# Tortilla-lang
A statically typed, easy to read compiled language, with a soft/hard error system.

```

array input = [0, 10, -3, 2, -5]

func aboveZero (array nums) array {
  array output = []
  forEach i in nums:
    if i >= 0:
      output.push(i)
    end
  end
  return output
}

print(aboveZero(input))

```
Tortilla is currently being created. The above code cannot yet run.

* Modern syntax that is easy to read and learn
* A 2-level error system: soft errors allow the code to keep running while hard errors stop compilation
* Class oriented, allowing for easy inheritance, and the ability to run code on instance creation
* Statically typed with a first-class generics system

Tortilla is still in Version 0, with a completed Lexer written in Python.

## Roadmap
- V0 — Working compiler in C++ by 2026
- V0.5 — Full testing and VSCode extension
- V1 — Multiple distribution methods, public release (before Summer 2028)
- V2 — Standard libraries and language additions

Link to complete specifications: https://github.com/spencerjw10/Tortilla-lang/blob/main/spec/Tortilla-spec.md
