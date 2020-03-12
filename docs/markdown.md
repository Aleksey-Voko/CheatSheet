# Markdown basic syntax

## Text
**bold**
__bold__

*italic*
_italic_

***bold italic***

~~wrapped~~

_You **can** combine them_

\**Ignoring\** \_Markdown\_ \~~formatting\~~

## URLs

[link to Google!](http://google.com)

or

http://www.github.com/

## Lists
##### Ordered:
1. Item 1
1. Item 2
1. Item 3
   1. Item 3a
      1. Item 3b

##### Unordered:
* Item 1
* Item 2
  * Item 2a
    * Item 2b

or

- Item 1
- Item 2
  - Item 2a
    - Item 2b

# Header 1
## Header 2
### Header 3
#### Header 4
##### Header 5
###### Header 6

## Quote
> Coffee. The finest organic suspension ever devised... I beat the Borg with it.
> - Captain Janeway


## Code
Inline code: `var example = true`

block of code:
```
if (isAwesome){
  return true
}
```

block of code (4 spaces):

    if (isAwesome){
      return true
    }

syntax highlighting:
```python
def foo(bar):
    if not bar:
        return True
```

## Task Lists
- [x] @mentions, #refs, [links](), **formatting**, and <del>tags</del> supported
- [x] list syntax required (any unordered or ordered list supported)
- [x] this is a complete item
- [ ] this is an incomplete item

## Tables
First Header | Second Header
------------ | -------------
Content from cell 1 | Content from cell 2
Content in the first column | Content in the second column

or

| Left-aligned | Center-aligned | Right-aligned |
| :---         |     :---:      |          ---: |
| git status   | git status     | git status    |
| git diff     | git diff       | git diff      |

or

| Name     | Character |
| ---      | ---       |
| Backtick | `         |
| Pipe     | \|        |

## Images
![Image of Yaktocat](https://github.com/fluidicon.png)

## Emoji
[emoji-cheat-sheet](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md)

https://www.webfx.com/tools/emoji-cheat-sheet/