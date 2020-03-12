# Markdown basic syntax #
origin: [Writing on GitHub](https://help.github.com/en/github/writing-on-github)

---

## Text ##

`**bold**` or `__bold__`  
**bold** or **bold**

`*italic*` or `_italic_`  
*italic* or _italic_

`***bold italic***`  
***bold italic***

`~~wrapped~~`  
~~wrapped~~

`_You **can** combine them_`  
_You **can** combine them_

`\**Ignoring\** \_Markdown\_ \~~formatting\~~`  
\**Ignoring\** \_Markdown\_ \~~formatting\~~

---

## URLs ##

`[link to Google!](http://google.com)`  
[link to Google!](http://google.com)

or

`http://www.github.com/`  
http://www.github.com/

---

## Lists ##
##### Ordered: #####
```
1. Item 1
1. Item 2
1. Item 3
   1. Item 3a
      1. Item 3b
```

1. Item 1
1. Item 2
1. Item 3
   1. Item 3a
      1. Item 3b

##### Unordered: #####
```
* Item 1
* Item 2
  * Item 2a
    * Item 2b
```

* Item 1
* Item 2
  * Item 2a
    * Item 2b

or

```
- Item 1
- Item 2
  - Item 2a
    - Item 2b
```

- Item 1
- Item 2
  - Item 2a
    - Item 2b

---

## Headers ##

`# Header 1` or `# Header 1 #`  
# Header 1

`## Header 2` or `## Header 2 ##`  
## Header 2

`### Header 3` or `### Header 3 ###`  
### Header 3

`#### Header 4` or `#### Header 4 ####`  
#### Header 4

`##### Header 5` or `##### Header 5 #####`  
##### Header 5

`###### Header 6` or `###### Header 6 ######`  
###### Header 6

---

## Quote ##
```
> Coffee. The finest organic suspension ever devised... I beat the Borg with it.
> - Captain Janeway
```

> Coffee. The finest organic suspension ever devised... I beat the Borg with it.
> - Captain Janeway

---

## Code

Inline code:
```
string: `var example = true`
```

result:

string: `var example = true`

---

block of code:

&#96;&#96;&#96;  
if (isAwesome){  
&nbsp;&nbsp;&nbsp;&nbsp;return true
}  
&#96;&#96;&#96;

result:
```
if (isAwesome){  
    return true
}
```

---

syntax highlighting:

&#96;&#96;&#96;python  
def foo(bar):  
&nbsp;&nbsp;&nbsp;&nbsp;if not bar:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return True  
&#96;&#96;&#96;

result:
```python
def foo(bar):
    if not bar:
        return True
```

---

## Task Lists
```
- [x] @mentions, #refs, [links](), **formatting**, and <del>tags</del> supported
- [x] list syntax required (any unordered or ordered list supported)
- [x] this is a complete item
- [ ] this is an incomplete item
```

result:
- [x] @mentions, #refs, [links](), **formatting**, and <del>tags</del> supported
- [x] list syntax required (any unordered or ordered list supported)
- [x] this is a complete item
- [ ] this is an incomplete item

---

## Tables
code:
```
First Header | Second Header
------------ | -------------
Content from cell 1 | Content from cell 2
Content in the first column | Content in the second column
```

result:

First Header | Second Header
------------ | -------------
Content from cell 1 | Content from cell 2
Content in the first column | Content in the second column

---

or

code:

```
| Left-aligned | Center-aligned | Right-aligned |
| :---         |     :---:      |          ---: |
| git status   | git status     | git status    |
| git diff     | git diff       | git diff      |
```

result:

| Left-aligned | Center-aligned | Right-aligned |
| :---         |     :---:      |          ---: |
| git status   | git status     | git status    |
| git diff     | git diff       | git diff      |

---

or

code:

```
| Name     | Character |
| ---      | ---       |
| Backtick | `         |
| Pipe     | \|        |
```

result:

| Name     | Character |
| ---      | ---       |
| Backtick | `         |
| Pipe     | \|        |

---

## Images
code:
```
![Image of Yaktocat](https://github.com/fluidicon.png)
```
result:

![Image of Yaktocat](https://github.com/fluidicon.png)

---

## Emoji
[emoji-cheat-sheet](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md)

https://www.webfx.com/tools/emoji-cheat-sheet/

---
