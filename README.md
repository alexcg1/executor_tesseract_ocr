# TesseractOCR


## Usage

#### via Docker image (recommended)

```python
from jina import Flow
	
f = Flow().add(uses='jinahub+docker://TesseractOCR')
```

#### via source code

Install [Tesseract](https://tesseract-ocr.github.io/)

```python
from jina import Flow
	
f = Flow().add(uses='jinahub://TesseractOCR')
```

- To override `__init__` args & kwargs, use `.add(..., uses_with: {'key': 'value'})`
- To override class metas, use `.add(..., uses_metas: {'key': 'value})`
