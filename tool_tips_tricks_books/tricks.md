# Tricks

## Formating in Markdown

[The Only Markdown Cheatsheet You Need](https://github.com/im-luka/markdown-cheatsheet/blob/main/README.md#some-id)

### Center Images
<div style="text-align:center;">
  <img src="./path/to/random.image" alt="Random Image" style="width:300px;height:auto;">
</div>

>[!IMPORTANT]

>[!WARNING]

>[!CAUTION]

>[!TIP]

>[!NOTE]

>[!DANGER]

>[!SUCCESS]

>[!BUG]

>[!EXAMPLE]

>[!QUOTE]

### Toggeling

<details open>
<summary>Click to hide the source</summary>

#### Visible Header
>
>[!IMPORTANT]

- list

</details>

<details>
<summary>Click to see the source</summary>

#### Hidden Header

>[!IMPORTANT]

- list

</details>

```python {.line-numbers} title:test.py
import numpy as np
import pandas as pd
```

### Image styling

<div style="text-align:center;">
  <img src="../fungiIncognita/images/happycodingshroom.webp" alt="Happy coding" title="Coding shroom 🍄" style="width:300px;height:auto;border-radius: 10%;">
</div>

![Fungi](../fungiIncognita/images/happycodingshroom.webp#fungi "Coding shroom 🍄")

<style>img[src$="#fungi"] {
  display: block;
  margin: 0 auto;
  border-radius: 10%;
  width: 300px;
}
</style>
